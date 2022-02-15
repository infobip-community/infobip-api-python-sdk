import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from tests.conftest import LocationMessageBodyFactory, get_random_string


def test_location_message_body__is_an_instance_of_message_body():
    assert isinstance(LocationMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("latitude", [None, "", {}, -90.001, 90.0001])
def test_when_content_latitude_is_invalid__validation_error_is_raised(latitude):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(
            **{"content": {"latitude": latitude}, "longitude": 120.53}
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
