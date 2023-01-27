from pydantic.types import constr

from infobip_channels.core.models import QueryParameter


class VerifyPhoneNumberQueryParameters(QueryParameter):
    pin_id: constr(min_length=1)
