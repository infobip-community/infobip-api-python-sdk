from typing import Dict, Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class SendPINOverSMSBody(MessageBodyBase, CamelCaseModel):
    application_id: constr(min_length=1) = None
    message_id: constr(min_length=1) = None
    from_id: Optional[str]
    to: constr(min_length=1) = None
    placeholders: Optional[Dict[str, str]]
