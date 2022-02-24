import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import (
    CreateTemplateBodyFactory,
    CreateTemplatesPathParametersFactory,
    get_random_string,
)


@pytest.mark.parametrize("sender", [None, {}])
def test_when_sender_is_invalid__validation_error_is_raised(sender):
    with pytest.raises(ValidationError):
        CreateTemplatesPathParametersFactory.build(**{"sender": sender})


@pytest.mark.parametrize("name", [None, {}])
def test_when_name_is_invalid__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": name,
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {"body": "example {{1}} body"},
            }
        )


@pytest.mark.parametrize("language", [None, "", {}])
def test_when_language_is_invalid__validation_error_is_raised(language):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": language,
                "category": "ACCOUNT_UPDATE",
                "structure": {"body": "example {{1}} body"},
            }
        )


@pytest.mark.parametrize("category", [None, "", {}])
def test_when_category_is_invalid__validation_error_is_raised(category):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": category,
                "structure": {"body": "example {{1}} body"},
            }
        )


@pytest.mark.parametrize("structure", [None, "", {}])
def test_when_structure_is_invalid__validation_error_is_raised(structure):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": structure,
            }
        )


@pytest.mark.parametrize("header_format", [None, "", {}])
def test_when_header_format_is_invalid__validation_error_is_raised(header_format):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": header_format, "text": "Text example"},
                    "body": "example {{1}} body",
                },
            }
        )


@pytest.mark.parametrize("body", [None, {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": body,
                },
            }
        )


@pytest.mark.parametrize("text", [None, {}])
def test_when_buttons_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "example {{1}} body",
                    "buttons": [{"type": "QUICK_REPLY", "text": text}],
                },
            }
        )


@pytest.mark.parametrize(
    "url",
    [
        None,
        "",
        {},
        "www.infobip.com/test",
        f"http://infobip.com/{get_random_string(2030)}",
    ],
)
def test_when_buttons_url_is_invalid__validation_error_is_raised(url):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "example {{1}} body",
                    "buttons": [{"type": "URL", "text": "Text example", "url": url}],
                },
            }
        )


@pytest.mark.parametrize("phone_number", [None, {}])
def test_when_buttons_phone_number_is_invalid__validation_error_is_raised(phone_number):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "example {{1}} body",
                    "buttons": [
                        {
                            "type": "PHONE_NUMBER",
                            "text": "Text example",
                            "phoneNumber": phone_number,
                        }
                    ],
                },
            }
        )


@pytest.mark.parametrize(
    "buttons_number",
    ["", {}, [{"type": "QUICK_REPLY", "text": "Text example"} for _ in range(4)]],
)
def test_when_buttons_number_is_invalid__validation_error_is_raised(buttons_number):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "example {{1}} body",
                    "buttons": buttons_number,
                },
            }
        )
