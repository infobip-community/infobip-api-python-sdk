from pydantic.types import constr

from infobip_channels.core.models import MessageBodyBase, CamelCaseModel


class VerifyPhoneNumberBody(MessageBodyBase, CamelCaseModel):
    pin: constr(min_length=1)
