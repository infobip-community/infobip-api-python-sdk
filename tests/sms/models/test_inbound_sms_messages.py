import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.get_inbound_messages import (
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


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetInboundSMSMessagesQueryParameters(
            **{
                "limit": 2,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
