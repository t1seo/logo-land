from __future__ import annotations

import struct
import sys
import zlib
from io import BytesIO
from typing import TYPE_CHECKING

import pytest
from PIL import Image, ImageCms
from PIL._imagingcms import createProfile
from PIL.PngImagePlugin import PngInfo

from logo_helper.models import ProjectError
from logo_helper.reference_models import RegionOfInterest
from logo_helper.references import extract_palette, inspect_reference

if TYPE_CHECKING:
    from collections.abc import Callable


def png_bytes(image: Image.Image, *, profile: bytes | None = None) -> bytes:
    with BytesIO() as stream:
        image.save(stream, format="PNG", icc_profile=profile)
        return stream.getvalue()


def test_white_is_kept_and_hidden_red_excluded() -> None:
    # Given
    with Image.new("RGBA", (32, 16), (255, 0, 0, 0)) as image:
        image.paste((255, 255, 255, 255), (0, 0, 16, 16))
        data = png_bytes(image)
    # When
    result = extract_palette(data)
    # Then
    assert [(s.hex, s.samples) for s in result.swatches] == [("#FFFFFF", 256)]
    assert result.sampling.visible_samples == 256
    assert result.profile_treatment == "assumed_srgb"


@pytest.mark.parametrize("alpha", [0, 1, 249])
def test_insufficient_core_is_reported(alpha: int) -> None:
    # Given
    with Image.new("RGBA", (16, 16), (255, 255, 255, alpha)) as image:
        data = png_bytes(image)
    # When
    result = extract_palette(data)
    # Then
    assert result.status == "indeterminate"
    assert result.reasons


def test_median_cut_is_deterministic_with_share_then_hex_order() -> None:
    # Given
    with Image.new("RGB", (32, 16), "#F6F3EC") as image:
        image.paste("#000000", (0, 0, 16, 16))
        data = png_bytes(image)
    # When
    results = tuple(extract_palette(data, max_colors=2) for _ in range(2))
    # Then
    assert results[0] == results[1]
    assert [(s.hex, s.share) for s in results[0].swatches] == [("#000000", 0.5), ("#F6F3EC", 0.5)]


@pytest.mark.parametrize("profile_kind", ["srgb", "malformed", "lab"])
def test_embedded_profiles_have_honest_treatment(profile_kind: str) -> None:
    # Given
    profiles = {
        "srgb": ImageCms.ImageCmsProfile(createProfile("sRGB")).tobytes(),
        "malformed": b"invalid ICC bytes",
        "lab": ImageCms.ImageCmsProfile(createProfile("LAB")).tobytes(),
    }
    with Image.new("RGB", (16, 16), "#247A52") as image:
        data = png_bytes(image, profile=profiles[profile_kind])
    # When
    result = extract_palette(data)
    # Then
    assert result.profile_treatment == (
        "converted_icc" if profile_kind == "srgb" else "unsupported"
    )
    assert result.status == ("extracted" if profile_kind == "srgb" else "indeterminate")


@pytest.mark.parametrize("declared_srgb", [False, True])
def test_gamma_only_is_indeterminate_unless_srgb_declared(declared_srgb: bool) -> None:
    # Given
    info = PngInfo()
    info.add(b"gAMA", struct.pack(">I", 100000))
    if declared_srgb:
        info.add(b"sRGB", b"\x00")
    with Image.new("RGB", (16, 16), "white") as image, BytesIO() as stream:
        image.save(stream, format="PNG", pnginfo=info)
        data = stream.getvalue()
    # When
    result = extract_palette(data)
    # Then
    assert result.profile_treatment == ("declared_srgb" if declared_srgb else "unsupported")


def test_jpeg_exif_orientation_defines_roi_coordinates() -> None:
    # Given
    exif = Image.Exif()
    exif[274] = 6
    with Image.new("RGB", (32, 16), "red") as image, BytesIO() as stream:
        image.paste("blue", (16, 0, 32, 16))
        image.save(stream, format="JPEG", exif=exif, quality=100, subsampling=0)
        data = stream.getvalue()
    roi = RegionOfInterest(x=0, y=16, width=16, height=16)
    # When
    facts, result = inspect_reference(data, roi=roi), extract_palette(data, roi=roi)
    # Then
    assert (facts.format, facts.width, facts.height, facts.exif_orientation) == ("JPEG", 32, 16, 6)
    assert result.sampling.width == 16
    assert result.sampling.height == 32
    assert result.swatches[0].hex == "#0000FE"


@pytest.mark.parametrize("format_name", ["GIF", "BMP", "WEBP"])
def test_other_decodable_formats_are_rejected(format_name: str) -> None:
    # Given
    with Image.new("RGB", (16, 16), "white") as image, BytesIO() as stream:
        image.save(stream, format=format_name)
        data = stream.getvalue()
    # When / Then
    with pytest.raises(ProjectError, match="invalid_reference"):
        _ = inspect_reference(data)


def oversized_header() -> bytes:
    header = struct.pack(">IIBBBBB", 40000001, 1, 8, 2, 0, 0, 0)
    chunk = b"IHDR" + header
    return (
        b"\x89PNG\r\n\x1a\n"
        + struct.pack(">I", len(header))
        + chunk
        + struct.pack(">I", zlib.crc32(chunk))
        + bytes.fromhex("0000000049454e44ae426082")
    )


@pytest.mark.parametrize("make_data", [oversized_header, lambda: bytes(64 * 1024 * 1024 + 1)])
def test_large_inputs_reject_before_pixel_loading(make_data: Callable[[], bytes]) -> None:
    # Given
    data = make_data()
    # When / Then
    with pytest.raises(ProjectError, match="limit"):
        _ = inspect_reference(data)


def test_roi_outside_image_is_rejected() -> None:
    # Given
    with Image.new("RGB", (16, 16), "white") as image:
        data = png_bytes(image)
    # When / Then
    with pytest.raises(ProjectError, match="invalid_roi"):
        _ = extract_palette(data, roi=RegionOfInterest(x=10, y=0, width=16, height=16))


def test_supported_rgb_icc_conversion_changes_only_analysis_values() -> None:
    # Given
    profile = bytearray(ImageCms.ImageCmsProfile(createProfile("sRGB")).tobytes())
    tags: dict[bytes, tuple[int, int]] = {}
    for position in range(132, 132 + int.from_bytes(profile[128:132]) * 12, 12):
        tags[bytes(profile[position : position + 4])] = struct.unpack(
            ">II", profile[position + 4 : position + 12]
        )
    red, length = tags[b"rXYZ"]
    green, _ = tags[b"gXYZ"]
    red_data = bytes(profile[red : red + length])
    profile[red : red + length] = profile[green : green + length]
    profile[green : green + length] = red_data
    with Image.new("RGB", (16, 16), "red") as image:
        data = png_bytes(image, profile=bytes(profile))
    original = bytes(data)
    # When
    result = extract_palette(data)
    # Then
    assert result.profile_treatment == "converted_icc"
    assert result.swatches[0].hex == "#00FF00"
    assert data == original


@pytest.mark.parametrize("max_colors", [0, 9])
def test_invalid_extraction_count_is_rejected(max_colors: int) -> None:
    # Given
    with Image.new("RGB", (16, 16), "white") as image:
        data = png_bytes(image)
    # When
    with pytest.raises(ProjectError, match="invalid_color_count"):
        _ = extract_palette(data, max_colors=max_colors)


@pytest.mark.parametrize("mode", ["P", "L"])
def test_palette_and_grayscale_transparency_is_respected(mode: str) -> None:
    # Given
    with Image.new(mode, (32, 16), 0) as image, BytesIO() as stream:
        if mode == "P":
            image.putpalette([255, 0, 0, 255, 255, 255] + [0] * 762)
        image.paste(1 if mode == "P" else 255, (0, 0, 16, 16))
        image.save(stream, format="PNG", transparency=0)
        data = stream.getvalue()
    # When
    result = extract_palette(data)
    # Then
    assert result.swatches[0].hex == "#FFFFFF"
    assert result.sampling.visible_samples == 256


def test_grid_uses_original_centers_without_interpolating() -> None:
    # Given
    with Image.new("RGB", (256, 256), "black") as image:
        for y in range(1, 256, 2):
            for x in range(1, 256, 2):
                image.putpixel((x, y), (255, 0, 0))
        data = png_bytes(image)
    # When
    result = extract_palette(data)
    # Then
    assert [(s.hex, s.share) for s in result.swatches] == [("#FF0000", 1)]
    assert result.sampling.sampled_positions == 16384
    assert result.sampling.sampled_fraction == 0.25


def test_missing_icc_support_returns_indeterminate(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    profile = ImageCms.ImageCmsProfile(createProfile("sRGB")).tobytes()
    with Image.new("RGB", (16, 16), "red") as image:
        data = png_bytes(image, profile=profile)
    monkeypatch.setitem(sys.modules, "PIL._imagingcms", None)
    # When
    result = extract_palette(data)
    # Then
    assert result.profile_treatment == "unsupported"
    assert result.status == "indeterminate"
