from infobip_channels.core.models import QueryParameter


class VerifyPhoneNumberQueryParameters(QueryParameter):
    pin_id: str
