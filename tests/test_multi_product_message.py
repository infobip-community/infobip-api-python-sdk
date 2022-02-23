import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from infobip_channels.whatsapp.models.multi_product_message import (
    MultiProductMessageBody,
)
from tests.conftest import MultiProductMessageBodyFactory, get_random_string


def test_multi_product_message_body__is_an_instance_of_message_body():
    assert isinstance(MultiProductMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {
            "header": {"type": "TEXT", "text": "test"},
            "body": {"text": "test"},
            "footer": {"text": "test"},
        },
        {
            "header": {"type": "TEXT", "text": "test"},
            "action": {
                "catalogId": "1",
                "sections": [{"title": "title", "productRetailerIds": ["1"]}],
            },
            "footer": {"text": "test"},
        },
        {
            "body": {"text": "test"},
            "action": {
                "catalogId": "1",
                "sections": [{"title": "title", "productRetailerIds": ["1"]}],
            },
            "footer": {"text": "test"},
        },
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": content,
            }
        )


@pytest.mark.parametrize("header", [None, "", {}, {"type": "TEXT"}, {"text": "test"}])
def test_when_header_is_invalid__validation_error_is_raised(header):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": header,
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("header_type", [None, "", {}, "TEST"])
def test_when_header_type_is_invalid__validation_error_is_raised(header_type):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": header_type, "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_header_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": text},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": body,
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": text},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize(
    "action",
    [
        None,
        "",
        {},
        {"catalogId": "1"},
        {"sections": [{"title": "title", "productRetailerIds": ["1", "2"]}]},
    ],
)
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": action,
                },
            }
        )


@pytest.mark.parametrize("catalog_id", [None, {}])
def test_when_action_catalog_id_is_invalid__validation_error_is_raised(catalog_id):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": catalog_id,
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize(
    "sections",
    [
        None,
        "",
        {},
        [],
        [{"title": "Title", "productRetailerIds": ["1", "2"]} for _ in range(11)],
        [
            {"title": "", "productRetailerIds": ["1", "2"]},
            {"title": "Title 1", "productRetailerIds": ["3", "4"]},
        ],
        [
            {"title": None, "productRetailerIds": ["1", "2"]},
            {"title": "Title 1", "productRetailerIds": ["3", "4"]},
        ],
    ],
)
def test_when_action_sections_is_invalid__validation_error_is_raised(sections):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": sections,
                    },
                },
            }
        )


@pytest.mark.parametrize("sections_title", [{}, get_random_string(25)])
def test_when_sections_title_is_invalid__validation_error_is_raised(sections_title):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": sections_title,
                                "productRetailerIds": ["id 2"],
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("product_retailer_id", [None, "", {}])
def test_when_sections_product_retailer_id_is_invalid__validation_error_is_raised(
    product_retailer_id,
):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": product_retailer_id,
                            },
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("footer_text", [None, "", {}, get_random_string(61)])
def test_when_footer_text_is_invalid__validation_error_is_raised(footer_text):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                        ],
                    },
                    "footer": {"text": footer_text},
                },
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                        ],
                    },
                    "footer": {"text": "footer"},
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
