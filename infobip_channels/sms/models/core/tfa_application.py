from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase
from infobip_channels.sms.models.core.tfa_application_configuration import (
    TFAApplicationConfiguration,
)


class TFAApplication(MessageBodyBase, CamelCaseModel):
    application_id: Optional[str]
    name: constr(min_length=1) = None
    configuration: Optional[TFAApplicationConfiguration] = None
    enabled: Optional[bool]
