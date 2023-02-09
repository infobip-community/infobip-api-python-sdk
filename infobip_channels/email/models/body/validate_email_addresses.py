from infobip_channels.core.models import MessageBodyBase


class ValidateEmailAddressesMessageBody(MessageBodyBase):
    to: str
