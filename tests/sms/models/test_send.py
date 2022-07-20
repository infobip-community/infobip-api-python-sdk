from datetime import datetime, timedelta, timezone

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.body.send_message import SMSMessageBody
from tests.conftest import get_random_string
from tests.sms.conftest import GenerateSMSMessageBodyFactory


@pytest.mark.parametrize("messages", ["", None, {}])
def test_when_messages_is_invalid__validation_error_is_raised(messages):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(**{"messages": [messages]})


@pytest.mark.parametrize("destinations", ["", None, {}])
def test_when_destinations_is_invalid__validation_error_is_raised(destinations):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [destinations],
                    }
                ]
            }
        )


@pytest.mark.parametrize("destinations_to", [None, {}, get_random_string(51)])
def test_when_destinations_to_is_invalid__validation_error_is_raised(destinations_to):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": destinations_to}],
                    }
                ]
            }
        )


@pytest.mark.parametrize("calback_data", [{}, get_random_string(4001)])
def test_when_calback_data_to_is_invalid__validation_error_is_raised(calback_data):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "callbackData": calback_data,
                        "destinations": [{"to": "41793026727"}],
                    }
                ]
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
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "deliveryTimeWindow": delivery_time_window,
                        "destinations": [{"to": "41793026727"}],
                    }
                ]
            }
        )


@pytest.mark.parametrize("language_code", ["", {}, "Test"])
def test_when_language_code_is_invalid__validation_error_is_raised(language_code):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {"destinations": [{"to": "41793026727"}], "language": language_code}
                ]
            }
        )


@pytest.mark.parametrize("flash", ["", {}, "true"])
def test_when_flash_is_invalid__validation_error_is_raised(flash):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{"messages": [{"destinations": [{"to": "41793026727"}], "flash": flash}]}
        )


@pytest.mark.parametrize("notify_content_type", ["", {}, "Test"])
def test_when_notify_content_type_is_invalid__validation_error_is_raised(
    notify_content_type,
):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "notifyContentType": notify_content_type,
                    }
                ]
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "myserver.com", "www.myserver.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "notifyUrl": notify_url,
                    }
                ]
            }
        )


@pytest.mark.parametrize(
    "send_at",
    [
        {},
        "Test",
        "22-03-2022",
        datetime.now(),
        datetime.now(timezone.utc) + timedelta(days=181),
    ],
)
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {"destinations": [{"to": "41793026727"}], "sendAt": send_at}
                ]
            }
        )


@pytest.mark.parametrize("transliteration", ["", {}, "Test"])
def test_when_transliteration_is_invalid__validation_error_is_raised(transliteration):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "transliteration": transliteration,
                    }
                ]
            }
        )


@pytest.mark.parametrize("validity_period", ["", {}, "Test", 2881])
def test_when_validity_period_is_invalid__validation_error_is_raised(validity_period):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "validityPeriod": validity_period,
                    }
                ]
            }
        )


@pytest.mark.parametrize("principal_entity_id", [None, {}])
def test_when_principal_entity_id_is_invalid__validation_error_is_raised(
    principal_entity_id,
):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "regional": {
                            "indiaDlt": {"principalEntityId": principal_entity_id}
                        },
                    }
                ]
            }
        )


@pytest.mark.parametrize("amount", ["", None, {}, "test"])
def test_when_amount_is_invalid__validation_error_is_raised(amount):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                    }
                ],
                "sendingSpeedLimit": {"amount": amount, "timeUnit": "MINUTE"},
            }
        )


@pytest.mark.parametrize("time_unit", ["", {}, "test"])
def test_when_time_unit_is_invalid__validation_error_is_raised(time_unit):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                    }
                ],
                "sendingSpeedLimit": {"amount": 22, "timeUnit": time_unit},
            }
        )


@pytest.mark.parametrize("track", ["", {}, "test"])
def test_when_track_is_invalid__validation_error_is_raised(track):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                    }
                ],
                "tracking": {
                    "track": track,
                },
            }
        )


@pytest.mark.parametrize("tracking_type", ["", {}, "test"])
def test_when_tracking_type_is_invalid__validation_error_is_raised(tracking_type):
    with pytest.raises(ValidationError):
        GenerateSMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                    }
                ],
                "tracking": {
                    "type": tracking_type,
                },
            }
        )


@pytest.mark.parametrize(
    "send_at",
    [datetime.now(timezone.utc) + timedelta(days=1), "2022-07-20T16:00:00.000+0000"],
)
def test_when_input_data_is_valid__validation_error_is_not_raised(send_at):
    try:
        SMSMessageBody(
            **{
                "messages": [
                    {
                        "destinations": [{"to": "41793026727"}],
                        "from": "InfoSMS",
                        "text": "This is a sample message",
                        "sendAt": datetime.now(timezone.utc) + timedelta(days=1),
                    }
                ]
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
