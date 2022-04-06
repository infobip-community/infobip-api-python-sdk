from infobip_channels.core.models import ResponseBase


class GenerateTokenResponseOK(ResponseBase):
    token: str
    expiration_time: str
