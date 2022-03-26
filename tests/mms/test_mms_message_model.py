from datetime import date

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.mms.models import MMSMessageBody
from tests.conftest import get_random_string
from tests.mms.conftest import MMSMessageBodyFactory


@pytest.mark.parametrize(
    "head",
    [
        None,
        "",
        {},
        {"from": "38599854312"},
        {"to": "38598764321"},
    ],
)
def test_when_head_is_invalid__validation_error_is_raised(head):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(**{"head": head})


@pytest.mark.parametrize("from_number", [None, {}])
def test_when_from_number_is_invalid__validation_error_is_raised(from_number):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{"head": {"from": from_number, "to": "38598764321"}}
        )


@pytest.mark.parametrize("to", [None, {}])
def test_when_to_number_is_invalid__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(**{"head": {"from": "38599854312", "to": to}})


@pytest.mark.parametrize("callback_data", [{}, get_random_string(201)])
def test_when_callback_data_is_invalid__validation_error_is_raised(callback_data):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "callbackData": callback_data,
                }
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "string", "ftp://url.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "notifyUrl": notify_url,
                }
            }
        )


@pytest.mark.parametrize("send_at", [{}, "22-03-2022", date.today()])
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "sendAt": send_at,
                }
            }
        )


@pytest.mark.parametrize("intermediate_report", [{}, "", 0, "True"])
def test_when_intermediate_report_is_invalid__validation_error_is_raised(
    intermediate_report,
):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "intermediateReport": intermediate_report,
                }
            }
        )


@pytest.mark.parametrize(
    "delivery_time_window",
    [
        {},
        {"from": {"hour": 12, "minute": 0}, "to": {"hour": 14, "minute": 0}},
        {"from": {"hour": 12, "minute": 0}, "days": ["FRIDAY"]},
        {"to": {"hour": 12, "minute": 0}, "days": ["FRIDAY"]},
        {
            "from": {"hour": 12, "minute": 0},
            "to": {"hour": 12, "minute": 40},
            "days": ["FRIDAY"],
        },
    ],
)
def test_when_delivery_time_window_is_invalid__validation_error_is_raised(
    delivery_time_window,
):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "deliveryTimeWindow": delivery_time_window,
                }
            }
        )


@pytest.mark.parametrize(
    "externally_hosted_media",
    [
        {},
        [{}],
        [{"contentType": "test", "contentId": "2"}],
        [{"contentType": "test", "contentUrl": "http://url.com"}],
        [{"contentId": "3", "contentUrl": "http://url.com"}],
    ],
)
def test_when_externally_hosted_media_is_invalid__validation_error_is_raised(
    externally_hosted_media,
):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                },
                "externallyHostedMedia": externally_hosted_media,
            }
        )


@pytest.mark.parametrize("content_url", [{}, "string", "ftp://url.com"])
def test_when_content_url_is_invalid__validation_error_is_raised(content_url):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                },
                "externallyHostedMedia": [
                    {
                        "contentType": "test",
                        "contentId": "3",
                        "contentUrl": content_url,
                    }
                ],
            }
        )


@pytest.mark.parametrize("hour", [None, -2, 24])
def test_when_hour_is_invalid__validation_error_is_raised(hour):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "deliveryTimeWindow": {
                        "from": {"hour": hour, "minute": 30},
                        "days": ["MONDAY"],
                    },
                }
            }
        )


@pytest.mark.parametrize("minute", [None, -2, 60])
def test_when_minute_is_invalid__validation_error_is_raised(minute):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "deliveryTimeWindow": {
                        "to": {"hour": 12, "minute": minute},
                        "days": ["MONDAY"],
                    },
                }
            }
        )


@pytest.mark.parametrize("days", [[], "MONDAY", ["TEST"]])
def test_when_days_is_invalid__validation_error_is_raised(days):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "deliveryTimeWindow": {"days": days},
                }
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        MMSMessageBody(
            **{
                "head": {
                    "from": "38598743321",
                    "to": "38599876543",
                    "validityPeriodMinutes": 300,
                    "callbackData": "test",
                    "delivery_time_window": {
                        "days": ["MONDAY", "THURSDAY"],
                        "from_time": {"hour": 10, "minute": 30},
                    },
                },
                "externallyHostedMedia": [
                    {
                        "contentType": "some type",
                        "contentId": "331",
                        "contentUrl": "https://someurl.com",
                    }
                ],
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
