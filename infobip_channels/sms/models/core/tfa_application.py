from typing import Optional

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.sms.models.core.tfa_application_configuration import (
    TFAApplicationConfiguration,
)


class TFAApplication(CamelCaseModel):
    application_id: Optional[str]
    name: str
    configuration: Optional[TFAApplicationConfiguration]
    enabled: Optional[bool]
