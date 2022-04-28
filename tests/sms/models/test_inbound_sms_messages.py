import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.get_inbound_sms_messages import (
    GetInboundSMSMessagesQueryParameters,
)


@pytest.mark.parametrize("limit", ["", {}, -2, 1001])
def test_when_limit_is_invalid__validation_error_is_raised(limit):
    with pytest.raises(ValidationError):
        GetInboundSMSMessagesQueryParameters(
            **{
                "limit": limit,
            }
        )
