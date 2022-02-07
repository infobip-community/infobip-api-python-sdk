import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import ImageMessageBodyFactory, get_random_string
from whatsapp.models.core import MessageBody


def test_image_message_body__is_an_instance_of_message_body():
    assert isinstance(ImageMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ImageMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("media_url", [None, "", {}, get_random_string(4097)])
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        ImageMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


@pytest.mark.parametrize("caption", [None, "", {}, get_random_string(3001)])
def test_when_content_caption_is_invalid__validation_error_is_raised(caption):
    with pytest.raises(ValidationError):
        ImageMessageBodyFactory.build(**{"content": {"caption": caption}})
