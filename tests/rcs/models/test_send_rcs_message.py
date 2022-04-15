import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.rcs.Models.body.send_rcs_message import RCSMessageBody
from tests.conftest import get_random_numbers, get_random_string
from tests.rcs.conftest import RCSMessageBodyModelFactory


@pytest.mark.parametrize("to", [None, {}])
def test_when_to_is_invalid__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": to,
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REPLY",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "url": "https://www.example.test",
                            "type": "OPEN_URL",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("content", ["", None, {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": content,
            }
        )


@pytest.mark.parametrize("content_text", ["", None, {}])
def test_when_content_text_is_invalid__validation_error_is_raised(content_text):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {"text": content_text, "type": "TEXT"},
            }
        )


@pytest.mark.parametrize("reply_text", ["", None, {}, get_random_string(26)])
def test_when_reply_text_is_invalid__validation_error_is_raised(reply_text):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": reply_text,
                            "postbackData": "examplePostbackData",
                            "type": "REPLY",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "url": "https://www.example.test",
                            "type": "OPEN_URL",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("reply_postback_data", ["", None, {}, get_random_string(2049)])
def test_when_reply_postback_data_is_invalid__validation_error_is_raised(
    reply_postback_data,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": reply_postback_data,
                            "type": "REPLY",
                        }
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("open_url_text", ["", None, {}, get_random_string(26)])
def test_when_open_url_text_is_invalid__validation_error_is_raised(open_url_text):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": open_url_text,
                            "postbackData": "examplePostbackData",
                            "url": "https://www.example.test",
                            "type": "OPEN_URL",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "open_url_postback_data", ["", None, {}, get_random_string(2049)]
)
def test_when_open_url_postback_data_is_invalid__validation_error_is_raised(
    open_url_postback_data,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": open_url_postback_data,
                            "url": "https://www.example.test",
                            "type": "OPEN_URL",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "open_url_url",
    [
        "",
        None,
        {},
        get_random_string(1000),
        "www.example.test",
        f"http://myfile.com/{get_random_string(983)}",
    ],
)
def test_when_open_url_url_postback_data_is_invalid__validation_error_is_raised(
    open_url_url,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "url": open_url_url,
                            "type": "OPEN_URL",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("dial_phone_text", ["", None, {}, get_random_string(26)])
def test_when_dial_phone_text_is_invalid__validation_error_is_raised(dial_phone_text):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": dial_phone_text,
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "dial_phone_postback_data", ["", None, {}, get_random_string(2049)]
)
def test_when_dial_phone_postback_data_is_invalid__validation_error_is_raised(
    dial_phone_postback_data,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": dial_phone_postback_data,
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "dial_phone_phone_number",
    [get_random_string(2049), get_random_numbers(4), "097 888 9191"],
)
def test_when_dial_phone_phone_number_is_invalid__validation_error_is_raised(
    dial_phone_phone_number,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": dial_phone_phone_number,
                            "type": "DIAL_PHONE",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("show_location_text", ["", None, {}, get_random_string(26)])
def test_when_show_location_text_is_invalid__validation_error_is_raised(
    show_location_text,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": show_location_text,
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "show_location_postback_data", ["", None, {}, get_random_string(2049)]
)
def test_when_show_location_postback_data_is_invalid__validation_error_is_raised(
    show_location_postback_data,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": show_location_postback_data,
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("show_location_latitude", [None, "", {}, -90.001, 90.0001])
def test_when_show_location_latitude_is_invalid__validation_error_is_raised(
    show_location_latitude,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": show_location_latitude,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("show_location_longitude", [None, "", {}, -181.0, 181.0])
def test_when_show_location_longitude_is_invalid__validation_error_is_raised(
    show_location_longitude,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": show_location_longitude,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("show_location_label", [{}, get_random_string(101)])
def test_when_show_location_label_is_invalid__validation_error_is_raised(
    show_location_label,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": show_location_label,
                            "type": "SHOW_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("request_location_text", [None, "", {}, get_random_string(26)])
def test_when_request_location_text_is_invalid__validation_error_is_raised(
    request_location_text,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": request_location_text,
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION",
                        }
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize(
    "request_location_postback_data", [None, "", {}, get_random_string(2049)]
)
def test_when_request_location_postback_data_is_invalid__validation_error_is_raised(
    request_location_postback_data,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": request_location_postback_data,
                            "type": "REQUEST_LOCATION",
                        }
                    ],
                    "type": "TEXT",
                },
            }
        )


@pytest.mark.parametrize("file", [None, "", {}])
def test_when_file_is_invalid__validation_error_is_raised(file):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "file": file,
                    "thumbnail": {"url": "http://www.thumbnail.example.url"},
                    "type": "FILE",
                },
            }
        )


@pytest.mark.parametrize(
    "file_url",
    [
        None,
        "",
        {},
        "www.example.url",
        get_random_string(1000),
        f"http://myfile.com/{get_random_string(983)}",
    ],
)
def test_when_file_url_is_invalid__validation_error_is_raised(file_url):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "file": {"url": file_url},
                    "thumbnail": {"url": "http://www.thumbnail.example.url"},
                    "type": "FILE",
                },
            }
        )


@pytest.mark.parametrize(
    "thumbnail_url",
    [
        None,
        "",
        {},
        "www.example.url",
        get_random_string(1000),
        f"http://myfile.com/{get_random_string(983)}",
    ],
)
def test_when_thumbnail_url_is_invalid__validation_error_is_raised(thumbnail_url):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "file": {"url": "http://www.example.url"},
                    "thumbnail": {"url": thumbnail_url},
                    "type": "FILE",
                },
            }
        )


@pytest.mark.parametrize("content_type", [None, "", {}, "TEST"])
def test_when_content_type_is_invalid__validation_error_is_raised(content_type):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "file": {"url": "http://www.example.url"},
                    "thumbnail": {"url": "http://www.thumbnail.example.url"},
                    "type": content_type,
                },
            }
        )


@pytest.mark.parametrize("orientation", [None, "", {}, "TEST"])
def test_when_orientation_is_invalid__validation_error_is_raised(orientation):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": orientation,
                    "alignment": "LEFT",
                    "content": {
                        "title": "title,",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "thumbnail": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("alignment", [None, "", {}, "TEST"])
def test_when_alignment_is_invalid__validation_error_is_raised(alignment):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": alignment,
                    "content": {
                        "title": "title,",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "thumbnail": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("card_content", [None])
def test_when_card_content_is_invalid__validation_error_is_raised(card_content):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": card_content,
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_height", [None, "", {}, "TEST"])
def test_when_content_height_is_invalid__validation_error_is_raised(content_height):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "height": content_height,
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_title", ["", {}, get_random_string(201)])
def test_when_content_title_is_invalid__validation_error_is_raised(content_title):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": content_title,
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_description", ["", {}, get_random_string(2001)])
def test_when_content_description_is_invalid__validation_error_is_raised(
    content_description,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "ExampleTitle",
                        "description": content_description,
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_file", [None, "", {}])
def test_when_content_file_is_invalid__validation_error_is_raised(content_file):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {"file": content_file, "height": "MEDIUM"},
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_file_url", [None, "", {}, "www.example.url"])
def test_when_content_file_url_is_invalid__validation_error_is_raised(content_file_url):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {
                            "file": {"url": content_file_url},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("content_thumbnail_url", [None, "", {}, "www.example.url"])
def test_when_content_thumbnail_url_is_invalid__validation_error_is_raised(
    content_thumbnail_url,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "thumbnail": {"url": content_thumbnail_url},
                            "height": "MEDIUM",
                        },
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize(
    "suggestions_items",
    [
        [
            {
                "text": "exampleText",
                "postbackData": "examplePostbackData",
                "type": "REPLY",
            }
            for _ in range(5)
        ]
    ],
)
def test_when_suggestions_items_is_invalid__validation_error_is_raised(
    suggestions_items,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "thumbnail": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                        "suggestions": suggestions_items,
                    },
                    "type": "CARD",
                },
            }
        )


@pytest.mark.parametrize("carousel_card_with", [None, "", {}, "TEST"])
def test_when_carousel_card_with_is_invalid__validation_error_is_raised(
    carousel_card_with,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "cardWidth": carousel_card_with,
                    "contents": [
                        {
                            "title": "example title 1",
                            "description": "example description",
                            "media": {
                                "file": {"url": "http://www.example.url"},
                                "height": "SHORT",
                            },
                        },
                        {
                            "title": "example title 2",
                            "description": "example description",
                            "media": {
                                "file": {"url": "http://www.example.url"},
                                "height": "SHORT",
                            },
                        },
                    ],
                    "type": "CAROUSEL",
                },
            }
        )


@pytest.mark.parametrize("carousel_contents", [None, "", {}])
def test_when_carousel_contents_is_invalid__validation_error_is_raised(
    carousel_contents,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "cardWidth": "SMALL",
                    "contents": carousel_contents,
                    "type": "CAROUSEL",
                },
            }
        )


@pytest.mark.parametrize(
    "carousel_contents_size",
    [
        [{"title": "exampleText"} for _ in range(1)],
        [{"title": "exampleText"} for _ in range(11)],
    ],
)
def test_when_carousel_contents_size_is_invalid__validation_error_is_raised(
    carousel_contents_size,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "cardWidth": "SMALL",
                    "contents": carousel_contents_size,
                    "type": "CAROUSEL",
                },
            }
        )


@pytest.mark.parametrize("sms_failover_from", [None, "", {}])
def test_when_sms_failover_from_is_invalid__validation_error_is_raised(
    sms_failover_from,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {"text": "exampleText", "type": "TEXT"},
                "smsFailover": {
                    "from": sms_failover_from,
                    "text": "We could not reach you over RCS messaging.",
                    "validityPeriod": 15,
                    "validityPeriodTimeUnit": "MINUTES",
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId",
            }
        )


@pytest.mark.parametrize("sms_failover_text", [None, "", {}])
def test_when_sms_failover_text_is_invalid__validation_error_is_raised(
    sms_failover_text,
):
    with pytest.raises(ValidationError):
        RCSMessageBodyModelFactory.build(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {"text": "exampleText", "type": "TEXT"},
                "smsFailover": {
                    "from": "myInfoSmsSender",
                    "text": sms_failover_text,
                    "validityPeriod": 15,
                    "validityPeriodTimeUnit": "MINUTES",
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId",
            }
        )


def test_when_input_data_carousel_is_valid_card__validation_error_is_not_raised():
    try:
        RCSMessageBody(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "cardWidth": "SMALL",
                    "contents": [
                        {
                            "title": "title 1",
                            "description": "description 1",
                            "media": {
                                "file": {"url": "http://www.example.url"},
                                "thumbnail": {"url": "http://www.example.url"},
                                "height": "MEDIUM",
                            },
                            "suggestions": [
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "type": "REPLY",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "url": "https://www.example.test",
                                    "type": "OPEN_URL",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "phoneNumber": "385977666618",
                                    "type": "DIAL_PHONE",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "latitude": 45.793418,
                                    "longitude": 15.946297,
                                    "label": "label",
                                    "type": "SHOW_LOCATION",
                                },
                            ],
                        },
                        {
                            "title": "title 2",
                            "description": "description 2",
                            "media": {
                                "file": {"url": "http://www.example.url"},
                                "thumbnail": {"url": "http://www.example.url"},
                                "height": "MEDIUM",
                            },
                            "suggestions": [
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "type": "REPLY",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "url": "https://www.example.test",
                                    "type": "OPEN_URL",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "phoneNumber": "385977666618",
                                    "type": "DIAL_PHONE",
                                },
                                {
                                    "text": "exampleText",
                                    "postbackData": "examplePostbackData",
                                    "latitude": 45.793418,
                                    "longitude": 15.946297,
                                    "label": "label",
                                    "type": "SHOW_LOCATION",
                                },
                            ],
                        },
                    ],
                    "type": "CAROUSEL",
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


def test_when_input_data_is_valid_card__validation_error_is_not_raised():
    try:
        RCSMessageBody(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "orientation": "HORIZONTAL",
                    "alignment": "LEFT",
                    "content": {
                        "title": "title",
                        "description": "description",
                        "media": {
                            "file": {"url": "http://www.example.url"},
                            "thumbnail": {"url": "http://www.example.url"},
                            "height": "MEDIUM",
                        },
                        "suggestions": [
                            {
                                "text": "exampleText",
                                "postbackData": "examplePostbackData",
                                "type": "REPLY",
                            },
                            {
                                "text": "exampleText",
                                "postbackData": "examplePostbackData",
                                "url": "https://www.example.test",
                                "type": "OPEN_URL",
                            },
                            {
                                "text": "exampleText",
                                "postbackData": "examplePostbackData",
                                "phoneNumber": "385977666618",
                                "type": "DIAL_PHONE",
                            },
                            {
                                "text": "exampleText",
                                "postbackData": "examplePostbackData",
                                "latitude": 45.793418,
                                "longitude": 15.946297,
                                "label": "label",
                                "type": "SHOW_LOCATION",
                            },
                        ],
                    },
                    "type": "CARD",
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


def test_when_input_data_is_valid_text__validation_error_is_not_raised():
    try:
        RCSMessageBody(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REPLY",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "url": "https://www.example.test",
                            "type": "OPEN_URL",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION",
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION",
                        },
                    ],
                    "type": "TEXT",
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
