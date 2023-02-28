from typing import List, Optional

from pydantic.types import constr

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
    entity_id: Optional[constr(max_length=50)] = None
    application_id: Optional[constr(max_length=50)] = None


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
    tracking: Optional[Tracking] = None
