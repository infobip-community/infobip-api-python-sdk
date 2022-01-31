import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from tests.conftest import get_random_string
from whatsapp.authentication.models import Authentication
from whatsapp.document_message.models import MessageBody
from whatsapp.document_message.send import send_message


class MessageBodyFactory(ModelFactory):
    __model__ = MessageBody


@pytest.mark.parametrize(
    "base_url", [
        None, "", "invalid_url", "ftp://123.api.infobip.com", {}
    ]
)
def test_when_base_url_is_invalid__validation_error_is_raised(base_url):
    with pytest.raises(ValidationError):
        send_message(
            Authentication(base_url=base_url, api_key="api_key"),
            MessageBodyFactory.build(),
        )


@pytest.mark.parametrize("api_key", [None, "", {}])
def test_when_api_key_is_invalid__validation_error_is_raised(api_key):
    with pytest.raises(ValidationError):
        send_message(
            Authentication(
                base_url="https://123.api.infobip.com",
                api_key=api_key
            ),
            MessageBodyFactory.build(),
        )


@pytest.mark.parametrize("from_number", [None, "", {}, get_random_string(25)])
def test_when_from_number_is_invalid__validation_error_is_raised(
    from_number,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(authentication, MessageBodyFactory.build(**{"from": from_number}))


@pytest.mark.parametrize("to", [None, "", {}, get_random_string(25)])
def test_when_to_number_is_invalid__validation_error_is_raised(to, authentication):
    with pytest.raises(ValidationError):
        send_message(authentication, MessageBodyFactory.build(**{"to": to}))


@pytest.mark.parametrize("message_id", [{}, get_random_string(51)])
def test_when_message_id_is_invalid__validation_error_is_raised(
    message_id,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"messageId": message_id}),
        )


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content, authentication):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"content": content}),
        )


@pytest.mark.parametrize("media_url", [None, "", {}, get_random_string(2048), get_random_string(2049),
                                       "www.infobip.com/document"])
def test_when_content_media_url_is_invalid__validation_error_is_raised(
    media_url,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"content": {"mediaUrl": media_url}}),
        )


@pytest.mark.parametrize("caption", [None, "", {}, get_random_string(3001)])
def test_when_content_caption_is_invalid__validation_error_is_raised(
    caption,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"content": {"caption": caption}}),
        )


@pytest.mark.parametrize("filename", [None, "", {}, get_random_string(241)])
def test_when_content_filename_is_invalid__validation_error_is_raised(
    filename,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"content": {"filename": filename}}),
        )


@pytest.mark.parametrize("callback_data", [{}, get_random_string(4001)])
def test_when_content_callback_data_is_invalid__validation_error_is_raised(
    callback_data,
    authentication,
):
    with pytest.raises(ValidationError):
        send_message(
            authentication,
            MessageBodyFactory.build(**{"callbackData": callback_data}),
        )
