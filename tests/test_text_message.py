import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from tests.conftest import get_random_string
from whatsapp.client import WhatsappClient
from whatsapp.models.core import MessageBody
from whatsapp.models.text_message import TextMessageBody


class TextMessageBodyFactory(ModelFactory):
    __model__ = TextMessageBody


def test_text_message_body__is_an_instance_of_message_body():
    assert isinstance(TextMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(4097)])
def test_when_content_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(**{"content": {"text": text}})


@pytest.mark.parametrize("preview_url", ["", {}])
def test_when_content_preview_url_is_invalid__validation_error_is_raised(preview_url):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(
            **{"content": {"text": "text", "previewUrl": preview_url}}
        )


def test_when_bad_request_is_sent__400_response_is_received(
    httpserver, http_test_client, bad_request_response
):
    httpserver.expect_request(
        "/whatsapp/1/message/text", method="POST"
    ).respond_with_json(bad_request_response)

    whatsapp_client = WhatsappClient.from_provided_client(
        http_test_client(httpserver.url_for("/"))
    )
    response = whatsapp_client.send_text_message(TextMessageBodyFactory.build())

    assert response.json() == bad_request_response
