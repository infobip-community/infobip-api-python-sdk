from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.core.tfa_pin_status import PINStatus


class SendPINOverVoiceResponse(ResponseBase, PINStatus):
    pass
