import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.core import MessageBody
from infobip_channels.whatsapp.models.body.video_message import VideoMessageBody
from tests.whatsapp.conftest import VideoMessageBodyFactory, get_random_string


def test_video_message_body__is_an_instance_of_message_body():
    assert isinstance(VideoMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}, {"caption": "a caption"}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        VideoMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "media_url",
    [None, "", {}, "ftp://myfile.com", f"http://myfile.com/{get_random_string(2031)}"],
)
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        VideoMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


@pytest.mark.parametrize("caption", [{}, get_random_string(3001)])
def test_when_content_caption_is_invalid__validation_error_is_raised(caption):
    with pytest.raises(ValidationError):
        VideoMessageBodyFactory.build(
            **{"content": {"mediaUrl": "http://mymedia.com", "caption": caption}}
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        VideoMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {"mediaUrl": "http://wap.com"},
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
