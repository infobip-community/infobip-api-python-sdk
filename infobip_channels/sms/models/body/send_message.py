from enum import Enum
from typing import List, Optional

from infobip_channels.core.models import MessageBodyBase
from infobip_channels.sms.models.body.core import (
    CoreMessage,
    SendingSpeedLimit,
    Tracking,
)


class TransliterationEnum(str, Enum):
    TURKISH = "TURKISH"
    GREEK = "GREEK"
    CYRILLIC = "CYRILLIC"
    SERBIAN_CYRILLIC = "SERBIAN_CYRILLIC"
    CENTRAL_EUROPEAN = "CENTRAL_EUROPEAN"
    BALTIC = "BALTIC"
    NON_UNICODE = "NON_UNICODE"


class LanguageEnum(str, Enum):
    TURKISH = "TR"
    SPANISH = "ES"
    PORTUGUESE = "PORTUGUESE"
    AUTODETECT = "AUTODETECT"


class Message(CoreMessage):
    text: Optional[str] = None
    language: Optional[LanguageEnum] = None
    transliteration: Optional[TransliterationEnum]


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
    tracking: Optional[Tracking] = None
