import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.reschedule_messages import (
    RescheduleMessagesMessageBody,
)
from infobip_channels.email.models.query_parameters.reschedule_messages import (
    RescheduleMessagesQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        RescheduleMessagesQueryParameters(
            **{
                "bulkId": {},
            }
        )


def test_when_input_data_query_is_valid__validation_error_is_not_raised():
    try:
        RescheduleMessagesQueryParameters(
            **{
                "bulkId": "BULK-ID-123-xyz",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.parametrize(
    "send_at",
    [
        {},
        "Test",
        "22-03-2022",
    ],
)
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        RescheduleMessagesMessageBody(
            **{
                "sendAt": send_at,
            }
        )


def test_when_input_data_body_is_valid__validation_error_is_not_raised():
    try:
        RescheduleMessagesMessageBody(
            **{
                "sendAt": "2022-06-01T18:00:00.00+00:00",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
