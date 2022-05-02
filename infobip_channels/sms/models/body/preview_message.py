from typing import Optional

from infobip_channels.core.models import (
    LanguageEnum,
    MessageBodyBase,
    TransliterationEnum,
)


class PreviewSMSMessage(MessageBodyBase):
    language_code: Optional[LanguageEnum] = None
    text: str
    transliteration: Optional[TransliterationEnum]
