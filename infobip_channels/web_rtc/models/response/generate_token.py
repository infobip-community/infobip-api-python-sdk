from infobip_channels.core.models import ResponseBase


class GenerateToken(ResponseBase):
    token: str
    expiration_time: str
