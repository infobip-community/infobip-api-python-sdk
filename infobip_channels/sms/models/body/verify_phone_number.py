from infobip_channels.core.models import MessageBodyBase, CamelCaseModel


class VerifyPhoneNumberBody(MessageBodyBase, CamelCaseModel):
    pin: str
