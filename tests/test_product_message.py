import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import ProductMessageBodyFactory, get_random_string
from whatsapp.models.core import MessageBody


def test_buttons_message_body__is_an_instance_of_message_body():
    assert isinstance(ProductMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ProductMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("action", [None, "", {}])
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
