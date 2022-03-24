import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.audio_message import AudioMessageBody
from infobip_channels.whatsapp.models.body.core import MessageBody
from tests.whatsapp.conftest import AudioMessageBodyFactory
from tests.conftest import get_random_string


def test_audio_message_body__is_an_instance_of_message_body():
    assert isinstance(AudioMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        AudioMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "media_url",
    [None, "", {}, "ftp://myfile.com", f"http://myfile.com/{get_random_string(2031)}"],
)
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        AudioMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        AudioMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {"media_url": "https://audio_file.com"},
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
