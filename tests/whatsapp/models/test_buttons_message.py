import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.buttons_message import ButtonsMessageBody
from infobip_channels.whatsapp.models.body.core import MessageBody
from tests.whatsapp.conftest import ButtonsMessageBodyFactory
from tests.conftest import get_random_string


def test_buttons_message_body__is_an_instance_of_message_body():
    assert isinstance(ButtonsMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {
            "body": {"text": "test"},
            "header": {"type": "TEXT", "text": "header"},
            "footer": {"text": "footer"},
        },
        {
            "action": {"buttons": [{"type": "REPLY", "id": "1", "title": "title"}]},
            "header": {"type": "TEXT", "text": "header"},
            "footer": {"text": "footer"},
        },
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": body,
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "title"}]
                    },
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": text},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "title"}]
                    },
                },
            }
        )


@pytest.mark.parametrize("action", [None, "", {}])
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{"content": {"body": {"text": "test"}, "action": action}}
        )


@pytest.mark.parametrize(
    "buttons",
    [
        None,
        "",
        {},
        [],
        [{"type": "REPLY", "id": "1", "title": "Yes"} for _ in range(4)],
        [{"type": "REPLY", "id": "1"}],
        [{"type": "REPLY", "title": "Yes"}],
        [{"id": "1", "title": "Yes"}],
    ],
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
def test_when_header_text_is_invalid__validation_error_is_raised(text):
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
    "media_url",
    [
        None,
        "",
        {},
        "www.infobip.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
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
    "media_url",
    [
        None,
        "",
        {},
        "www.infobip.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
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
    "media_url",
    [
        None,
        "",
        {},
        "www.infobip.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
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


@pytest.mark.parametrize("footer", ["", {}])
def test_when_footer_is_invalid__validation_error_is_raised(footer):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "footer": footer,
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_footer_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ButtonsMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [{"type": "REPLY", "id": "1", "title": "Yes"}]
                    },
                    "footer": {"text": text},
                }
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ButtonsMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "buttons": [
                            {"type": "REPLY", "id": "1", "title": "Yes"},
                            {"type": "REPLY", "id": "2", "title": "No"},
                        ]
                    },
                    "header": {
                        "type": "DOCUMENT",
                        "mediaUrl": "http://infobip.com/docs.pdf",
                        "filename": "file",
                    },
                    "footer": {"text": "footer text"},
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
