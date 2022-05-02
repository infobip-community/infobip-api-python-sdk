from typing import List, Optional

from infobip_channels.core.models import (
    LanguageEnum,
    MessageBodyBase,
    TransliterationEnum,
)
from infobip_channels.sms.models.body.core import (
    CoreMessage,
    SendingSpeedLimit,
    Tracking,
)


class Message(CoreMessage):
    text: Optional[str] = None
    language: Optional[LanguageEnum] = None
    transliteration: Optional[TransliterationEnum]


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
    tracking: Optional[Tracking] = None
