from infobip_channels.sms.models.core.tfa_application_configuration import (
    TFAApplicationConfiguration,
)


class TFAApplication:
    application_id: str
    name: str
    configuration: TFAApplicationConfiguration
    enabled: bool
