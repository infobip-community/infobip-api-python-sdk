import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.query_parameters.get_logs import (
    GetLogsQueryParameters,
)


def test_when_message_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "messageId": {},
            }
        )


def test_when_from_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "from": {},
            }
        )


def test_when_to_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "to": {},
            }
        )


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "bulkId": {},
            }
        )


@pytest.mark.parametrize("general_status", [{}, "TEST"])
def test_when_general_status_is_invalid__validation_error_is_raised(general_status):
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "generalStatus": general_status,
            }
        )


# @pytest.mark.parametrize("sent_since", [{}, "22-03-2022", date.today()])
# def test_when_sent_since_is_invalid__validation_error_is_raised(sent_since):
#     with pytest.raises(ValidationError):
#         GetLogsQueryParameters(
#             **{
#                 "sentSince": sent_since,
#             }
#         )
#
#
# @pytest.mark.parametrize("sent_until", [{}, "22-03-2022", date.today()])
# def test_when_sent_until_is_invalid__validation_error_is_raised(sent_until):
#     with pytest.raises(ValidationError):
#         GetLogsQueryParameters(
#             **{
#                 "sentUntil": sent_until,
#             }
#         )


def test_when_limit_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetLogsQueryParameters(
            **{
                "limit": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetLogsQueryParameters(
            **{
                "messageId": "MESSAGE-ID-123-xyz",
                "from": "from@some.com",
                "to": "to@some.com",
                "bulkId": "BULK-ID-123-xyz",
                "generalStatus": "PENDING",
                "sentSince": "2022-03-22",
                "sentUntil": "2022-03-26",
                "limit": 2,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
