from datetime import date, datetime

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.get_outbound_logs import (
    GetOutboundSMSLogsQueryParameters,
)


def test_when_from_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "from": {},
            }
        )


def test_when_to_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "to": {},
            }
        )


def test_when_bulk_id_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "bulkId": {},
            }
        )


@pytest.mark.parametrize("message_id", ["", {}])
def test_when_message_id_invalid__validation_error_is_raised(message_id):
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "messageId": message_id,
            }
        )


@pytest.mark.parametrize("general_status", ["", {}])
def test_when_general_status_invalid__validation_error_is_raised(general_status):
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "generalStatus": general_status,
            }
        )


@pytest.mark.parametrize("sent_since", [{}, "Test", "22-03-2022", date.today()])
def test_when_sent_since_invalid__validation_error_is_raised(sent_since):
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "sentSince": sent_since,
            }
        )


@pytest.mark.parametrize("sent_until", [{}, "Test", "22-03-2022", date.today()])
def test_when_sent_until_invalid__validation_error_is_raised(sent_until):
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "sentUntil": sent_until,
            }
        )


@pytest.mark.parametrize("limit", [{}, -1, 1001])
def test_when_limit_invalid__validation_error_is_raised(limit):
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "limit": limit,
            }
        )


def test_when_mcc_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "mcc": {},
            }
        )


def test_when_mnc_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSLogsQueryParameters(
            **{
                "mnc": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetOutboundSMSLogsQueryParameters(
            **{
                "from": "41793026999",
                "to": "41793026727",
                "bulkId": ["BULK-ID-123-xyz"],
                "messageId": ["MESSAGE-ID-123-xyz"],
                "generalStatus": "PENDING",
                "sentSince": datetime.now(),
                "sentUntil": datetime.now(),
                "limit": 2,
                "mcc": "22",
                "mnc": "11",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
