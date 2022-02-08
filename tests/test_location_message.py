import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import LocationMessageBodyFactory, get_random_string
from whatsapp.models.core import MessageBody


def test_location_message_body__is_an_instance_of_message_body():
    assert isinstance(LocationMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("latitude", [None, "", {}, -91.0, 91.0])
def test_when_content_latitude_is_invalid__validation_error_is_raised(latitude):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": {"latitude": latitude}})


@pytest.mark.parametrize("longitude", [None, "", {}, -181.0, 181.0])
def test_when_content_longitude_is_invalid__validation_error_is_raised(longitude):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": {"longitude": longitude}})


@pytest.mark.parametrize("name", [None, "", {}, get_random_string(1001)])
def test_when_content_name_is_invalid__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": {"name": name}})


@pytest.mark.parametrize("address", [None, "", {}, get_random_string(1001)])
def test_when_content_address_is_invalid__validation_error_is_raised(address):
    with pytest.raises(ValidationError):
        LocationMessageBodyFactory.build(**{"content": {"address": address}})
