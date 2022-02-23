import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from infobip_channels.whatsapp.models.product_message import ProductMessageBody
from tests.conftest import ProductMessageBodyFactory, get_random_string


def test_product_message_body__is_an_instance_of_message_body():
    assert isinstance(ProductMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {"body": {"text": "test"}},
        {"footer": {"text": "footer"}},
        {"body": {"text": "test"}, "footer": {"text": "footer"}},
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "action",
    [
        None,
        "",
        {},
        {"catalogId": "1"},
        {"productRetailerId": "2"},
    ],
)
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(**{"content": {"action": action}})


@pytest.mark.parametrize("catalog_id", [None, {}])
def test_when_action_catalog_id_is_invalid__validation_error_is_raised(catalog_id):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {"catalogId": catalog_id, "productRetailerId": "1"}
                }
            }
        )


@pytest.mark.parametrize("product_retailer_id", [None, {}])
def test_when_action_product_retailer_id_is_invalid__validation_error_is_raised(
    product_retailer_id,
):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {
                        "catalogId": "1",
                        "productRetailerId": product_retailer_id,
                    }
                }
            }
        )


@pytest.mark.parametrize("body", ["", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {"catalogId": "1", "productRetailerId": "2"},
                    "body": body,
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {"catalogId": "1", "productRetailerId": "2"},
                    "body": {"text": text},
                }
            }
        )


@pytest.mark.parametrize("footer", ["", {}])
def test_when_footer_is_invalid__validation_error_is_raised(footer):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {"catalogId": "1", "productRetailerId": "2"},
                    "footer": footer,
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_footer_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(
            **{
                "content": {
                    "action": {"catalogId": "1", "productRetailerId": "2"},
                    "footer": {"text": text},
                }
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ProductMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "body": {"text": "Body text"},
                    "action": {
                        "catalogId": "1",
                        "productRetailerId": "2",
                    },
                    "footer": {"text": "footer text"},
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
