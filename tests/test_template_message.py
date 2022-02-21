import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from infobip_channels.whatsapp.models.template_message import (
    Message,
    TemplateMessageBody,
)
from tests.conftest import get_random_string


def test_templates_message_body__is_an_instance_of_message_body():
    assert (
        isinstance(
            Message(
                **{
                    "from": "441134960000",
                    "to": "38595671032",
                    "content": {
                        "template_name": "template_name",
                        "template_data": {
                            "body": {"placeholders": ["value 1", "value 2"]},
                            "buttons": [
                                {"type": "QUICK_REPLY", "parameter": "button 1"},
                                {"type": "QUICK_REPLY", "parameter": "button 2"},
                            ],
                        },
                        "language": "en",
                    },
                    "sms_failover": {"from_number": "38599543122", "text": "help!"},
                },
            ),
            MessageBody,
        )
        is True
    )


@pytest.mark.parametrize("messages", [None, {}, [{}]])
def test_when_messages_are_invalid__validation_error_is_raised(messages):
    with pytest.raises(ValidationError):
        TemplateMessageBody(**{"messages": messages})


@pytest.mark.parametrize("bulk_id", [{}, get_random_string(101)])
def test_when_bulk_id_is_invalid__validation_error_is_raised(bulk_id):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "template_name",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                            },
                            "language": "en",
                        },
                    },
                ],
                "bulkId": bulk_id,
            }
        )


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {"templateName": "name"},
        {"templateData": {"body": {"placeholders": ["First Value"]}}},
        {"language": "en"},
        {
            "templateName": "name",
            "templateData": {"body": {"placeholders": ["First Value"]}},
        },
        {"templateName": "name", "language": "en"},
        {
            "language": "en",
            "templateData": {"body": {"placeholders": ["First Value"]}},
        },
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {"from": "441134960000", "to": "38595671032", "content": content},
                ],
            }
        )


@pytest.mark.parametrize(
    "template_name",
    [
        None,
        "",
        {},
        get_random_string(513),
        "template name !!",
        "template_name_example 2",
    ],
)
def test_when_template_name_is_invalid__validation_error_is_raised(template_name):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": template_name,
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "template_data",
    [
        None,
        "",
        {},
        {"header": {"type": "TEXT", "placeholder": "value"}},
        {"buttons": [{"type": "QUICK_REPLY", "parameter": "test"}]},
    ],
)
def test_when_template_data_is_invalid__validation_error_is_raised(template_data):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": template_data,
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("language", [None, "", {}])
def test_when_language_is_invalid__validation_error_is_raised(language):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                            },
                            "language": language,
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {"body": body},
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("placeholders", [None, "", {}, [""], [None]])
def test_when_placeholders_is_invalid__validation_error_is_raised(placeholders):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {"body": {"placeholders": placeholders}},
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("header_type", [None, "", {}, "INVALID"])
def test_when_header_type_is_invalid__validation_error_is_raised(header_type):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": header_type,
                                    "mediaUrl": "https://test_file.png",
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("placeholder", [None, {}])
def test_when_text_placeholder_is_invalid__validation_error_is_raised(placeholder):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {"type": "TEXT", "placeholder": placeholder},
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "media_url",
    [
        None,
        "",
        {},
        "www.missing-scheme.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
)
def test_when_document_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "DOCUMENT",
                                    "mediaUrl": media_url,
                                    "filename": "Test",
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("filename", [None, "", {}, get_random_string(241)])
def test_when_document_filename_is_invalid__validation_error_is_raised(filename):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "DOCUMENT",
                                    "mediaUrl": "https://test_file.png",
                                    "filename": filename,
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "media_url",
    [
        None,
        "",
        {},
        "www.missing-scheme.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
)
def test_when_image_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": media_url,
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "media_url",
    [
        None,
        "",
        {},
        "www.missing-scheme.com",
        "ftp://myfile.com",
        f"http://myfile.com/{get_random_string(2031)}",
    ],
)
def test_when_video_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "VIDEO",
                                    "mediaUrl": media_url,
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("latitude", [None, "", {}, -91, 91])
def test_when_location_latitude_is_invalid__validation_error_is_raised(latitude):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "LOCATION",
                                    "latitude": latitude,
                                    "longitude": 0,
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("longitude", [None, "", {}, -181, 181])
def test_when_location_longitude_is_invalid__validation_error_is_raised(longitude):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "LOCATION",
                                    "latitude": 0,
                                    "longitude": longitude,
                                },
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "buttons",
    [
        [{"type": "QUICK_REPLY", "parameter": "test"} for _ in range(4)],
        [
            {"type": "QUICK_REPLY", "parameter": "test"},
            {"type": "URL", "parameter": "test url"},
        ],
        [
            {"type": "URL", "parameter": "test url 1"},
            {"type": "URL", "parameter": "test url 2"},
        ],
    ],
)
def test_when_buttons_is_invalid__validation_error_is_raised(buttons):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://test_file.png",
                                },
                                "buttons": buttons,
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("buttons_type", [None, "", {}, "INVALID"])
def test_when_buttons_type_is_invalid__validation_error_is_raised(buttons_type):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://test_file.png",
                                },
                                "buttons": [
                                    {
                                        "type": buttons_type,
                                        "parameter": "https://Test.com",
                                    }
                                ],
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("button_parameter", [None, "", {}, get_random_string(129)])
def test_when_quick_reply_button_parameter_is_invalid__validation_error_is_raised(
    button_parameter,
):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://test_file.png",
                                },
                                "buttons": [
                                    {
                                        "type": "QUICK_REPLY",
                                        "parameter": button_parameter,
                                    }
                                ],
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize("button_parameter", [None, {}])
def test_when_url_button_parameter_is_invalid__validation_error_is_raised(
    button_parameter,
):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://test_file.png",
                                },
                                "buttons": [
                                    {
                                        "type": "URL",
                                        "parameter": button_parameter,
                                    }
                                ],
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


@pytest.mark.parametrize(
    "sms_failover",
    [{}, {"from": "441134960000"}, {"text": "test text"}],
)
def test_when_sms_failover_is_invalid__validation_error_is_raised(sms_failover):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://test_file.png",
                                },
                            },
                            "language": "en",
                        },
                        "smsFailover": sms_failover,
                    },
                ],
            }
        )


@pytest.mark.parametrize("sms_failover_from", [None, "", {}, get_random_string(25)])
def test_when_sms_failover_from_is_invalid__validation_error_is_raised(
    sms_failover_from,
):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                            },
                            "language": "en",
                        },
                        "smsFailover": {"from": sms_failover_from, "text": "Test"},
                    },
                ],
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(4097)])
def test_when_sms_failover_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "boarding_pass",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                            },
                            "language": "en",
                        },
                        "smsFailover": {"from": "441134960000", "text": text},
                    },
                ],
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                        "content": {
                            "template_name": "template_name",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "IMAGE",
                                    "media_url": "https://image.com",
                                },
                                "buttons": [
                                    {"type": "QUICK_REPLY", "parameter": "button 1"},
                                    {"type": "QUICK_REPLY", "parameter": "button 2"},
                                ],
                            },
                            "language": "en",
                        },
                        "sms_failover": {"from_number": "38599543122", "text": "help!"},
                    },
                    {
                        "from": "441134960000",
                        "to": "38598311460",
                        "content": {
                            "templateName": "template_name_2",
                            "templateData": {
                                "body": {"placeholders": []},
                                "header": {
                                    "type": "TEXT",
                                    "placeholder": "placeholder text",
                                },
                                "buttons": [{"type": "URL", "parameter": "url button"}],
                            },
                            "language": "en",
                        },
                    },
                ],
                "bulk_id": "123-456-786",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
