import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import get_random_string
from tests.sms.conftest import GeneratePreviewSMSMessageBodyFactory


@pytest.mark.parametrize("language_code", [{}, get_random_string(4)])
def test_when_language_code_is_invalid__validation_error_is_raised(language_code):
    with pytest.raises(ValidationError):
        GeneratePreviewSMSMessageBodyFactory.build(
            **{
                "languageCode": language_code,
                "text": "Let's see how many characters remain unused in "
                "this message",
                "transliteration": "TURKISH",
            }
        )


@pytest.mark.parametrize("text", [None, {}])
def test_when_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        GeneratePreviewSMSMessageBodyFactory.build(
            **{
                "languageCode": "AUTODETECT",
                "text": text,
                "transliteration": "TURKISH",
            }
        )


@pytest.mark.parametrize("transliteration", [{}, "ABC"])
def test_when_transliteration_is_invalid__validation_error_is_raised(transliteration):
    with pytest.raises(ValidationError):
        GeneratePreviewSMSMessageBodyFactory.build(
            **{
                "languageCode": "AUTODETECT",
                "text": "Let's see how many characters remain unused in "
                "this message",
                "transliteration": transliteration,
            }
        )
