import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.core import MessageBody
from infobip_channels.whatsapp.models.body.location_message import LocationMessageBody
from tests.conftest import get_random_string
from tests.whatsapp.conftest import LocationMessageBodyFactory


def test_location_message_body__is_an_instance_of_message_body():
    assert isinstance(LocationMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {"latitude": 42, "name": "test", "address": "address one"},
        {"longitude": 120, "name": "test", "address": "address one"},
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("latitude", [None, "", {}, -90.001, 90.0001])
def test_when_content_latitude_is_invalid__validation_error_is_raised(latitude):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(
            **{"content": {"latitude": latitude, "longitude": 120.53}}
        )


@pytest.mark.parametrize("longitude", [None, "", {}, -181.0, 181.0])
def test_when_content_longitude_is_invalid__validation_error_is_raised(longitude):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(
            **{"content": {"longitude": longitude, "latitude": -50.934}}
        )


@pytest.mark.parametrize("name", [{}, get_random_string(1001)])
def test_when_content_name_is_invalid__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(
            **{"content": {"longitude": 130.5541, "latitude": -50.934, "name": name}}
        )


@pytest.mark.parametrize("address", [{}, get_random_string(1001)])
def test_when_content_address_is_invalid__validation_error_is_raised(address):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(
            **{
                "content": {
                    "longitude": -165.33,
                    "latitude": -89.205,
                    "address": address,
                }
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        LocationMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "latitude": 83,
                    "longitude": -103,
                    "name": "test",
                    "address": "test",
                },
                "callbackData": "Callback data",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
