import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import get_random_string
from whatsapp.authentication.models import Authentication
from whatsapp.core.models import BaseMessageBody


@pytest.mark.parametrize(
    "base_url", [
        None, "", "invalid_url", "ftp://123.api.infobip.com", {}
    ]
)
def test_when_base_url_is_invalid__validation_error_is_raised(base_url):
    with pytest.raises(ValidationError):
        Authentication(base_url=base_url, api_key="api_key")


@pytest.mark.parametrize("api_key", [None, "", {}])
def test_when_api_key_is_invalid__validation_error_is_raised(api_key):
    with pytest.raises(ValidationError):
        Authentication(base_url="https://123.api.infobip.com", api_key=api_key)


@pytest.mark.parametrize("from_number", [None, "", {}, get_random_string(25)])
def test_when_from_number_is_invalid__validation_error_is_raised(from_number):
    with pytest.raises(ValidationError):
        BaseMessageBody(**{"from": from_number})


@pytest.mark.parametrize("to", [None, "", {}, get_random_string(25)])
def test_when_to_number_is_invalid__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        BaseMessageBody(**{"to": to})


@pytest.mark.parametrize("callback_data", [{}, get_random_string(4001)])
def test_when_content_callback_data_is_invalid__validation_error_is_raised(callback_data):
    with pytest.raises(ValidationError):
        BaseMessageBody(**{"callbackData": callback_data})
