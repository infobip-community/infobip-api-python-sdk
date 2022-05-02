from datetime import date, datetime, timedelta

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.body.send_binary_message import BinarySMSMessageBody
from tests.conftest import get_random_string
from tests.sms.conftest import GenerateBinarySMSMessageBodyFactory


@pytest.mark.parametrize("messages", ["", None, {}])
def test_when_messages_is_invalid__validation_error_is_raised(messages):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(**{"messages": [messages]})


@pytest.mark.parametrize("destinations", ["", None, {}])
def test_when_destinations_is_invalid__validation_error_is_raised(destinations):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [destinations],
                    }
                ]
            }
        )


@pytest.mark.parametrize("destinations_to", [None, {}, get_random_string(51)])
def test_when_destinations_to_is_invalid__validation_error_is_raised(destinations_to):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [
                            {"to": destinations_to},
                        ],
                    }
                ]
            }
        )


@pytest.mark.parametrize("calback_data", [{}, get_random_string(4001)])
def test_when_calback_data_is_invalid__validation_error_is_raised(calback_data):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
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
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "deliveryTimeWindow": delivery_time_window,
                        "destinations": [{"to": "41793026727"}],
                    }
                ]
            }
        )


@pytest.mark.parametrize("flash", ["", {}, "true"])
def test_when_flash_is_invalid__validation_error_is_raised(flash):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [{"to": "41793026727"}],
                        "flash": flash,
                    }
                ]
            }
        )


@pytest.mark.parametrize("notify_content_type", ["", {}, "Test"])
def test_when_notify_content_type_is_invalid__validation_error_is_raised(
    notify_content_type,
):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [{"to": "41793026727"}],
                        "notifyContentType": notify_content_type,
                    }
                ]
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "myserver.com", "www.myserver.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [{"to": "41793026727"}],
                        "notifyUrl": notify_url,
                    }
                ]
            }
        )


@pytest.mark.parametrize(
    "send_at",
    [{}, "Test", "22-03-2022", date.today(), datetime.now() + timedelta(days=181)],
)
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [{"to": "41793026727"}],
                        "sendAt": send_at,
                    }
                ]
            }
        )


@pytest.mark.parametrize("validity_period", ["", {}, "Test", 2881])
def test_when_validity_period_is_invalid__validation_error_is_raised(validity_period):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
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
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
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
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [{"to": "41793026727"}],
                    }
                ],
                "sendingSpeedLimit": {"amount": amount, "timeUnit": "MINUTE"},
            }
        )


@pytest.mark.parametrize("time_unit", ["", {}, "test"])
def test_when_time_unit_is_invalid__validation_error_is_raised(time_unit):
    with pytest.raises(ValidationError):
        GenerateBinarySMSMessageBodyFactory.build(
            **{
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "destinations": [
                            {"to": "41793026727"},
                        ],
                    }
                ],
                "sendingSpeedLimit": {"amount": 22, "timeUnit": time_unit},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        BinarySMSMessageBody(
            **{
                "bulkId": "BULK-ID-123-xyz",
                "messages": [
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                        },
                        "callbackData": "DLR callback data",
                        "destinations": [
                            {"messageId": "MESSAGE-ID-123-xyz", "to": "41793026727"},
                            {"to": "41793026834"},
                        ],
                        "from": "InfoSMS",
                        "intermediateReport": True,
                        "notifyContentType": "application/json",
                        "notifyUrl": "https://www.example.com/sms/advanced",
                        "validityPeriod": 720,
                    },
                    {
                        "binary": {
                            "dataCoding": 0,
                            "esmClass": 0,
                            "hex": "41 20 6C 6F 6E 67 20 74 20 45 6D 70 69 72 65 2E",
                        },
                        "deliveryTimeWindow": {
                            "days": [
                                "MONDAY",
                                "TUESDAY",
                                "WEDNESDAY",
                                "THURSDAY",
                                "FRIDAY",
                                "SATURDAY",
                                "SUNDAY",
                            ],
                            "from": {"hour": 6, "minute": 0},
                            "to": {"hour": 15, "minute": 30},
                        },
                        "destinations": [{"to": "41793026700"}],
                        "from": "41793026700",
                        "sendAt": datetime.now() + timedelta(days=1),
                    },
                ],
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
