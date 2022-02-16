import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from infobip_channels.whatsapp.models.core import MessageBody
from infobip_channels.whatsapp.models.template_message import Message
from tests.conftest import get_random_string


class MessageBodyFactory(ModelFactory):
    __model__ = Message


def test_template_message_body__is_an_instance_of_message_body():
    assert isinstance(MessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("template_name", [None, "", {}])
def test_when_template_name_is_invalid__validation_error_is_raised(template_name):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": template_name,
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("template_data", [None, "", {}])
def test_when_template_data_is_invalid__validation_error_is_raised(template_data):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "",
                    "templateData": template_data,
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("language", [None, "", {}])
def test_when_language_is_invalid__validation_error_is_raised(language):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                    },
                    "language": language,
                }
            }
        )


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": body,
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("placeholders", [None, {}])
def test_when_placeholders_is_invalid__validation_error_is_raised(placeholders):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": placeholders},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("header_type", [None, "", {}])
def test_when_header_type_is_invalid__validation_error_is_raised(header_type):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": header_type,
                            "mediaUrl": "https://test_file.png",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("placeholder", [None, {}])
def test_when_text_placeholder_is_invalid__validation_error_is_raised(placeholder):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {"type": "TEXT", "placeholder": placeholder},
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("media_url", [None, "", {}])
def test_when_document_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "DOCUMENT",
                            "mediaUrl": media_url,
                            "fileName": "Test",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("filename", [None, "", {}])
def test_when_document_filename_is_invalid__validation_error_is_raised(filename):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "DOCUMENT",
                            "mediaUrl": "https://test_file.png",
                            "fileName": filename,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("media_url", [None, "", {}])
def test_when_image_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": media_url,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("media_url", [None, "", {}])
def test_when_video_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "VIDEO",
                            "mediaUrl": media_url,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("latitude", [None, "", {}, -91, 91])
def test_when_location_latitude_is_invalid__validation_error_is_raised(latitude):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "LOCATION",
                            "latitude": latitude,
                            "longitude": 0,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("longitude", [None, "", {}, -181, 181])
def test_when_location_longitude_is_invalid__validation_error_is_raised(longitude):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "LOCATION",
                            "latitude": 0,
                            "longitude": longitude,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("buttons_type", [None, "", {}])
def test_when_buttons_type_is_invalid__validation_error_is_raised(buttons_type):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                        "buttons": {
                            "type": buttons_type,
                            "parameter": "https://Test.com",
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("buttons_parameter", [None, "", {}, get_random_string(241)])
def test_when_buttons_parameter_is_invalid__validation_error_is_raised(
    buttons_parameter,
):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {
                        "body": {"placeholders": ["123456789"]},
                        "header": {
                            "type": "IMAGE",
                            "mediaUrl": "https://test_file.png",
                        },
                        "buttons": {
                            "type": "QUICK_REPLY",
                            "parameter": buttons_parameter,
                        },
                    },
                    "language": "en",
                }
            }
        )


@pytest.mark.parametrize("sms_failover_from", [None, "", {}])
def test_when_sms_failover_from_is_invalid__validation_error_is_raised(
    sms_failover_from,
):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {"body": {"placeholders": ["123456789"]}},
                    "language": "en",
                },
                "smsFailover": {"from": sms_failover_from, "text": "Test"},
            }
        )


@pytest.mark.parametrize("text", [None, "", {}])
def test_when_sms_failover_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        MessageBodyFactory.build(
            **{
                "content": {
                    "templateName": "boarding_pass",
                    "templateData": {"body": {"placeholders": ["123456789"]}},
                    "language": "en",
                },
                "smsFailover": {"from": "441134960000", "text": text},
            }
        )
