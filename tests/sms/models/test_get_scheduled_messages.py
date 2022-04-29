import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.get_scheduled_messages import (
    GetScheduledSMSMessagesQueryParameters,
)


@pytest.mark.parametrize("bulk_id", [{}, None])
def test_when_bulk_id_is_invalid__validation_error_is_raised(bulk_id):
    with pytest.raises(ValidationError):
        GetScheduledSMSMessagesQueryParameters(
            **{
                "bulk_id": bulk_id,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetScheduledSMSMessagesQueryParameters(
            **{
                "bulk_id": "BulkId-xyz-123",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
