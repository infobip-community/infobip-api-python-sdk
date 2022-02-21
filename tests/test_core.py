import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from infobip_channels.whatsapp.models.response.core import Authentication, MessageBody
from tests.conftest import get_random_string


class MessageBodyFactory(ModelFactory):
    __model__ = MessageBody


@pytest.mark.parametrize("base_url", [None, "", "ftp://123.api.infobip.com", {}])
def test_when_base_url_is_invalid__validation_error_is_raised(base_url):
    with pytest.raises(ValidationError):
        Authentication(base_url=base_url, api_key="api_key")


@pytest.mark.parametrize("api_key", [None, "", {}])
def test_when_api_key_is_invalid__validation_error_is_raised(api_key):
    with pytest.raises(ValidationError):
        Authentication(base_url="https://123.api.infobip.com", api_key=api_key)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://123.api.infobip.com",
        "https://123.api.infobip.com",
        "123.api.infobip.com",
    ],
)
def test_base_url_in_different_forms__validation_passes(base_url):
    try:
        Authentication(base_url=base_url, api_key="api_key")
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.parametrize("from_number", [None, "", {}, get_random_string(25)])
def test_when_from_number_is_invalid__validation_error_is_raised(from_number):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"from": from_number})


@pytest.mark.parametrize("to", [None, "", {}, get_random_string(25)])
def test_when_to_number_is_invalid__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"to": to})


@pytest.mark.parametrize("callback_data", [{}, get_random_string(4001)])
def test_when_callback_data_is_invalid__validation_error_is_raised(
    callback_data,
):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"callbackData": callback_data})


@pytest.mark.parametrize("message_id", [{}, get_random_string(51)])
def test_when_message_id_is_invalid__validation_error_is_raised(message_id):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"messageId": message_id})


@pytest.mark.parametrize(
    "notify_url", [{}, f"http://myserver.com/{get_random_string(2029)}"]
)
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"notifyUrl": notify_url})
