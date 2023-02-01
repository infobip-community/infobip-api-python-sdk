from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.core.tfa_application import TFAApplication


class UpdateTFAApplicationResponse(ResponseBase, TFAApplication):
    pass
