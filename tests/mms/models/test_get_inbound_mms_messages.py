import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.mms.models.query_parameters.get_inbound_mms_messages import (
    GetInboundMMSMessagesQueryParameters,
)


@pytest.mark.parametrize("limit", [{}, "ABC"])
def test_when_limit_is_invalid__validation_error_is_raised(limit):
    with pytest.raises(ValidationError):
        GetInboundMMSMessagesQueryParameters(**{"limit": limit})


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetInboundMMSMessagesQueryParameters(**{"limit": 2})
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
