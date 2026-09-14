"""Decode originals and construct in-memory review aids without rewriting artwork."""

from __future__ import annotations

import hashlib
import io
import os
import stat
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Final

from PIL import Image, UnidentifiedImageError
from pydantic import Field, ValidationError

from .checks import review_view
from .models import StudioError as HostError
from .models_base import FrozenModel

if TYPE_CHECKING:
    from pathlib import Path

MAX_BYTES: Final = 32 * 1024 * 1024
RECEIPT_LIMIT: Final = 32 * 1024
NativeText = Annotated[str, Field(max_length=24000)]


class NativeReceipt(FrozenModel):
    """The installed native image result, including its observed Codex metadata."""

    success: bool
    image: NativeText | None
    provider: NativeText = ""
    model: NativeText = ""
    error: NativeText | None = None
    error_type: NativeText | None = None
    prompt: NativeText | None = None
    aspect_ratio: NativeText | None = None
    modality: NativeText | None = None
    size: NativeText | None = None
    quality: NativeText | None = None
    input_image_count: Annotated[int, Field(ge=0, le=6)] | None = None
    image_source: NativeText | None = None
    requested_size: NativeText | None = None
    pixel_size: NativeText | None = None


@dataclass(frozen=True, slots=True)
class PngEvidence:
    """Original bytes and a width-specific preview share an immutable identity."""

    original: bytes
    sha256: str
    view: bytes
    view_sha256: str
    width: int


def read_png(path: Path) -> bytes:
    if not path.is_absolute() or path.is_symlink() or not path.is_file():
        raise HostError("invalid_png", f"Expected a local regular PNG file: {path}")
    try:
        with path.open("rb") as source:
            if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
                raise HostError("invalid_png", f"Image is not a regular file: {path}")
            data = source.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise HostError("invalid_png", "PNG exceeds the 32 MiB input limit")
        with Image.open(io.BytesIO(data)) as decoded:
            if decoded.format != "PNG":
                raise HostError("invalid_png", "Expected a decoded PNG")
            decoded.verify()
        with Image.open(io.BytesIO(data)) as decoded:
            _ = decoded.load()
            try:
                decoded.seek(1)
            except EOFError:
                return data
    except (OSError, SyntaxError, UnidentifiedImageError, Image.DecompressionBombError) as exc:
        raise HostError("invalid_png", f"PNG decoding failed: {exc}") from exc
    raise HostError("invalid_png", "Expected a single-frame decoded PNG")


def image_evidence(path: Path, width: int) -> PngEvidence:
    data = read_png(path)
    view_data = review_view(path, width)
    if read_png(path) != data:
        raise HostError("image_changed", "Image changed while preparing the target view")
    return PngEvidence(
        data,
        hashlib.sha256(data).hexdigest(),
        view_data,
        hashlib.sha256(view_data).hexdigest(),
        width,
    )


def parse_receipt(raw: str) -> NativeReceipt:
    if len(raw.encode("utf-8")) > RECEIPT_LIMIT:
        raise HostError("invalid_receipt", "Native receipt exceeds 32 KiB")
    try:
        result = NativeReceipt.model_validate_json(raw)
    except ValidationError as exc:
        raise HostError("invalid_receipt", str(exc), (raw,)) from exc
    if not result.success:
        raise HostError(
            "native_image_failed", result.error or "Native image generation failed", (raw,)
        )
    if not result.image or not result.provider.strip() or not result.model.strip() or result.error:
        raise HostError(
            "invalid_receipt", "Successful receipt lacks valid image/attribution", (raw,)
        )
    return result


def verify_unchanged(
    path: Path,
    expected_digest: str,
    raw_reports: tuple[str, ...],
    *,
    parent: bool = False,
) -> None:
    try:
        data = read_png(path)
    except HostError as exc:
        raise HostError(exc.code, exc.detail, raw_reports) from exc
    if hashlib.sha256(data).hexdigest() != expected_digest:
        code = "parent_changed" if parent else "image_changed"
        raise HostError(code, "Original changed during critique", raw_reports)
