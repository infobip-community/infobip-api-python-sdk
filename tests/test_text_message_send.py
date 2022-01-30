import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from whatsapp.authentication.models import Authentication
from whatsapp.text_message.models import MessageBody
from whatsapp.text_message.send import send_message


class MessageBodyFactory(ModelFactory):
    __model__ = MessageBody


@pytest.fixture
def message_body():
    return MessageBodyFactory.build()


@pytest.fixture
def base_url():
    return "https://123.api.infobip.com"


@pytest.fixture
def api_key():
    return "secret_key"


@pytest.mark.parametrize(
    "base_url,api_key",
    [
        ("invalid_url", "secret_key"),
        (None, "secret_key"),
        ("", "secret_key"),
        ("ftp://123.api.infobip.com", "secret_key"),
        ("https://123.api.infobip.com", None),
        ("https://123.api.infobip.com", ""),
    ]
)
def test_when_authentication_parameters_invalid__validation_error(
    base_url,
    api_key,
    message_body,
):
    with pytest.raises(ValidationError):
        send_message(Authentication(base_url=base_url, api_key=api_key), message_body)
