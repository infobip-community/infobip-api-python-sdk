import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import TextMessageBodyFactory, get_random_string
from whatsapp.models.core import MessageBody


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
