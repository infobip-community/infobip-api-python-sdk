from typing import List, Optional

from infobip_channels.core.models import (
    CamelCaseModel,
    LanguageEnum,
    ResponseBase,
    TransliterationEnum,
)


class Language(CamelCaseModel):
    language_code: LanguageEnum


class Configuration(CamelCaseModel):
    language: Optional[Language] = None
    transliteration: Optional[TransliterationEnum] = None


class Preview(CamelCaseModel):
    text_preview: str
    message_count: int
    characters_remaining: int
    configuration: Configuration


class PreviewSMSMessageResponse(ResponseBase):
    original_text: str
    previews: List[Preview]
