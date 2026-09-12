"""Brand intent with exact lettering and optional requested lockup."""

from typing import Annotated

from pydantic import Field

from logo_helper.lockup_models import LockupIntent
from logo_helper.model_base import Background, FrozenModel, LogoType, Text


class Brief(FrozenModel):
    """Brand intent; exact_text and slogan are preserved verbatim."""

    brand_name: Text
    exact_text: Annotated[str, Field(max_length=2000)]
    industry: Text
    audience: Text
    slogan: str = ""
    logo_type: LogoType = "combination"
    styles: tuple[Text, ...] = ()
    palette: tuple[Text, ...] = ()
    forbidden: tuple[Text, ...] = ()
    use_cases: tuple[Text, ...] = ()
    assumptions: tuple[Text, ...] = ()
    lockup: LockupIntent | None = None
    background: Background = "opaque"
    concept_count: Annotated[int, Field(ge=1)] = 3
