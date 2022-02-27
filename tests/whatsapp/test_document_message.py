import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.core import MessageBody
from infobip_channels.whatsapp.models.body.document_message import DocumentMessageBody
from tests.whatsapp.conftest import DocumentMessageBodyFactory, get_random_string


def test_document_message_body__is_an_instance_of_message_body():
    assert isinstance(DocumentMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content", [None, "", {}, {"caption": "caption", "filename": "test"}]
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "media_url",
    [None, "", {}, "ftp://myfile.com", f"http://myfile.com/{get_random_string(2031)}"],
)
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


@pytest.mark.parametrize("caption", [{}, get_random_string(3001)])
def test_when_content_caption_is_invalid__validation_error_is_raised(caption):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(
            **{"content": {"mediaUrl": "http://mymedia.com", "caption": caption}}
        )


@pytest.mark.parametrize("filename", [{}, get_random_string(241)])
def test_when_content_filename_is_invalid__validation_error_is_raised(filename):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(
            **{"content": {"mediaUrl": "http://mymedia.com", "filename": filename}}
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        DocumentMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "media_url": "http://document.com",
                    "caption": "cool tile",
                    "filename": "doc.pdf",
                },
                "notifyUrl": "https://notify.me",
                "callbackData": "Some callback data",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
