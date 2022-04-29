import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.body.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesMessageBody,
)
from infobip_channels.sms.models.query_parameters.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesQueryParameters,
)


@pytest.mark.parametrize("bulk_id", [{}, None])
def test_when_bulk_id_is_invalid__validation_error_is_raised(bulk_id):
    with pytest.raises(ValidationError):
        UpdateScheduledSMSMessagesQueryParameters(
            **{
                "bulk_id": bulk_id,
            }
        )


def test_when_input_data_is_valid_query__validation_error_is_not_raised():
    try:
        UpdateScheduledSMSMessagesQueryParameters(
            **{
                "bulk_id": "BulkId-xyz-123",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.parametrize("status", [{}, None, "TEST"])
def test_when_status_is_invalid__validation_error_is_raised(status):
    with pytest.raises(ValidationError):
        UpdateScheduledSMSMessagesMessageBody(
            **{
                "status": status,
            }
        )


def test_when_input_data_is_valid_body__validation_error_is_not_raised():
    try:
        UpdateScheduledSMSMessagesMessageBody(
            **{
                "status": "PROCESSING",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
