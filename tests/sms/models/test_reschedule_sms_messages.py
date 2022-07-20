from datetime import date, datetime, timedelta, timezone

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.body.reschedule_sms_messages import (
    RescheduleSMSMessagesMessageBody,
)
from infobip_channels.sms.models.query_parameters.reschedule_messages import (
    RescheduleSMSMessagesQueryParameters,
)


@pytest.mark.parametrize("bulk_id", [{}, None])
def test_when_bulk_id_is_invalid__validation_error_is_raised(bulk_id):
    with pytest.raises(ValidationError):
        RescheduleSMSMessagesQueryParameters(
            **{
                "bulk_id": bulk_id,
            }
        )


def test_when_input_data_is_valid_query__validation_error_is_not_raised():
    try:
        RescheduleSMSMessagesQueryParameters(
            **{
                "bulk_id": "BulkId-xyz-123",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.parametrize(
    "send_at",
    [{}, "Test", "22-03-2022", date.today(), datetime.now() + timedelta(days=181)],
)
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        RescheduleSMSMessagesMessageBody(
            **{
                "sendAt": send_at,
            }
        )


@pytest.mark.parametrize(
    "send_at",
    [datetime.now(timezone.utc) + timedelta(days=1), "2022-07-20T16:00:00.000+0000"],
)
def test_when_input_data_is_valid_body__validation_error_is_not_raised(send_at):
    try:
        RescheduleSMSMessagesMessageBody(
            **{
                "sendAt": send_at,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
