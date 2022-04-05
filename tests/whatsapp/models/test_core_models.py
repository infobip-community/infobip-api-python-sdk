import pytest
from pydantic import AnyHttpUrl
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from infobip_channels.core.models import Authentication
from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.body.core import MessageBody
from tests.conftest import get_random_string


class MessageBodyFactory(ModelFactory):
    __model__ = MessageBody


@pytest.mark.parametrize(
    "base_url",
    [AnyHttpUrl("123.api.infobip.com", scheme="http"), "https://123.api.infobip.com"],
)
def test_validate_auth_params_returns_authentication_instance(base_url):
    auth_object = WhatsAppChannel.validate_auth_params(base_url, "api_key")
    assert isinstance(auth_object, Authentication) is True


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
