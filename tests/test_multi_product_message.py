import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.multi_product_message import (
    MultiProductMessageBody,
)
from infobip_channels.whatsapp.models.response.core import MessageBody
from tests.conftest import MultiProductMessageBodyFactory, get_random_string


def test_multi_product_message_body__is_an_instance_of_message_body():
    assert isinstance(MultiProductMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        MultiProductMessageBody(
            **{
                "from": "1234",
                "to": "6789",
                "content": content,
            }
        )


@pytest.mark.parametrize("action", [None, "", {}])
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


@pytest.mark.parametrize("header_type", [None, "", {}])
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


@pytest.mark.parametrize("product_retailer_id", [None, "", {}, []])
def test_when_action_product_retailer_id_is_invalid__validation_error_is_raised(
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
