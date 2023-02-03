from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.core.tfa_pin_verification import PINVerification


class VerifyPhoneNumberResponse(ResponseBase, PINVerification):
    pass
