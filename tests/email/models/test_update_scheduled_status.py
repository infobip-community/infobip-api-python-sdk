import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.update_scheduled_status import (
    UpdateScheduledStatusMessageBody,
)
from infobip_channels.email.models.query_parameters.update_scheduled_status import (
    UpdateScheduledStatusQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        UpdateScheduledStatusQueryParameters(
            **{
                "bulkId": {},
            }
        )


def test_when_input_data_query_is_valid__validation_error_is_not_raised():
    try:
        UpdateScheduledStatusQueryParameters(
            **{
                "bulkId": "BULK-ID-123-xyz",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


def test_when_status_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        UpdateScheduledStatusMessageBody(
            **{
                "status": {},
            }
        )


def test_when_input_data_body_is_valid__validation_error_is_not_raised():
    try:
        UpdateScheduledStatusMessageBody(
            **{
                "status": "PAUSED",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
