import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.text_message import TextMessageBody
from infobip_channels.whatsapp.models.response.core import MessageBody
from tests.conftest import TextMessageBodyFactory, get_random_string


def test_text_message_body__is_an_instance_of_message_body():
    assert isinstance(TextMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}, {"previewUrl": False}])
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


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        TextMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {"text": "a test message", "previewUrl": True},
                "callbackData": "Some data",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
