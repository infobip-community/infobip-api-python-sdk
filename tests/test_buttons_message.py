import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from tests.conftest import ButtonsMessageBodyFactory, get_random_string


def test_buttons_message_body__is_an_instance_of_message_body():
    assert isinstance(ButtonsMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(**{"content": {"body": body}})


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(**{"content": {"body": {"text": text}}})


@pytest.mark.parametrize("action", [None, "", {}])
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{"content": {"body": {"text": "test"}, "action": action}}
        )


@pytest.mark.parametrize(
    "buttons",
    [None, "", {}, [{"type": "REPLY", "id": "1", "title": "Yes"} for _ in range(4)]],
)
def test_when_action_buttons_is_invalid__validation_error_is_raised(buttons):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{"content": {"body": {"text": "test"}, "action": {"buttons": buttons}}}
        )


@pytest.mark.parametrize("test_type", [None, "", {}, "Test"])
def test_when_buttons_type_is_invalid__validation_error_is_raised(test_type):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": test_type, "id": "1", "title": "Yes"}]
                    },
                }
            }
        )


@pytest.mark.parametrize("test_id", [None, "", {}, get_random_string(257)])
def test_when_buttons_id_is_invalid__validation_error_is_raised(test_id):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": test_id, "title": "Yes"}]
                    },
                }
            }
        )


@pytest.mark.parametrize("title", [None, "", {}, get_random_string(21)])
def test_when_buttons_title_is_invalid__validation_error_is_raised(title):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": title}]
                    },
                }
            }
        )


@pytest.mark.parametrize("test_type", [None, "", {}, "TEST"])
def test_when_header_type_is_invalid__validation_error_is_raised(test_type):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {"type": test_type, "text": "Message"},
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {"type": "TEXT", "text": text},
                }
            }
        )


@pytest.mark.parametrize(
    "media_url", [None, "", {}, "www.infobip.com", get_random_string(2049)]
)
def test_when_video_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {"type": "VIDEO", "mediaUrl": media_url},
                }
            }
        )


@pytest.mark.parametrize(
    "media_url", [None, "", {}, "www.infobip.com", get_random_string(2049)]
)
def test_when_image_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {"type": "IMAGE", "mediaUrl": media_url},
                }
            }
        )


@pytest.mark.parametrize(
    "media_url", [None, "", {}, "www.infobip.com", get_random_string(2049)]
)
def test_when_document_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {"type": "DOCUMENT", "mediaUrl": media_url},
                }
            }
        )


@pytest.mark.parametrize("filename", [get_random_string(241)])
def test_when_document_filename_is_invalid__validation_error_is_raised(filename):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "header": {
                        "type": "DOCUMENT",
                        "mediaUrl": "http://infobip.com/docs.pdf",
                        "filename": filename,
                    },
                }
            }
        )
