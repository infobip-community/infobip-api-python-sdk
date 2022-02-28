import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.create_template import CreateTemplate
from tests.whatsapp.conftest import (
    CreateTemplateBodyFactory,
    CreateTemplatesPathParametersFactory,
    get_random_string,
)


@pytest.mark.parametrize("sender", [None, {}])
def test_when_sender_is_invalid__validation_error_is_raised(sender):
    with pytest.raises(ValidationError):
        CreateTemplatesPathParametersFactory.build(**{"sender": sender})


@pytest.mark.parametrize(
    "name",
    [
        None,
        "",
        {},
        "template name !!",
        "template_name_example 2",
        "Template_Name_Example",
    ],
)
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


@pytest.mark.parametrize("language", [None, "", {}, "bla"])
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


@pytest.mark.parametrize("category", [None, "", {}, "INVALID"])
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


@pytest.mark.parametrize(
    "structure",
    [
        None,
        "",
        {},
        {
            "header": {"format": "IMAGE"},
            "footer": "text",
            "buttons": [{"type": "QUICK_REPLY", "text": "test"}],
        },
    ],
)
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


@pytest.mark.parametrize("header", ["", {}, {"format": "INVALID"}, {"format": "TEXT"}])
def test_when_header_is_invalid__validation_error_is_raised(header):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": header,
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


@pytest.mark.parametrize("footer", [{}, get_random_string(61)])
def test_when_footer_is_invalid__validation_error_is_raised(footer):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "text",
                    "footer": footer,
                },
            }
        )


@pytest.mark.parametrize(
    "buttons",
    [
        [{"type": "QUICK_REPLY", "text": "test"} for _ in range(4)],
        [
            {"type": "QUICK_REPLY", "text": "test"},
            {"type": "URL", "text": "test url", "url": "http://url.com"},
        ],
        [
            {"type": "URL", "text": "test url", "url": "http://url.com"},
            {"type": "URL", "text": "test url 2", "url": "http://url2.com"},
        ],
        [
            {"type": "PHONE_NUMBER", "text": "number", "phoneNumber": "456321"},
            {"type": "PHONE_NUMBER", "text": "number 2", "phoneNumber": "456322"},
        ],
    ],
)
def test_when_buttons_is_invalid__validation_error_is_raised(buttons):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {"body": "text", "buttons": buttons},
            }
        )


@pytest.mark.parametrize("button_type", [None, "", {}, "TEST"])
def test_when_button_type_is_invalid__validation_error_is_raised(button_type):
    with pytest.raises(ValidationError):
        CreateTemplateBodyFactory.build(
            **{
                "name": "examplename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {"body": "text", "buttons": [{"type": button_type}]},
            }
        )


@pytest.mark.parametrize("text", [None, {}, get_random_string(201)])
def test_when_quick_reply_button_text_is_invalid__validation_error_is_raised(text):
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


@pytest.mark.parametrize("text", [None, {}, get_random_string(201)])
def test_when_phone_number_button_text_is_invalid__validation_error_is_raised(text):
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
                        {"type": "PHONE_NUMBER", "text": text, "phoneNumber": "324561"}
                    ],
                },
            }
        )


@pytest.mark.parametrize("number", [None, {}])
def test_when_phone_number_button_number_is_invalid__validation_error_is_raised(number):
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
                        {"type": "PHONE_NUMBER", "text": "test", "phoneNumber": number}
                    ],
                },
            }
        )


@pytest.mark.parametrize("text", [None, {}, get_random_string(201)])
def test_when_url_button_text_is_invalid__validation_error_is_raised(text):
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
                        {"type": "URL", "text": text, "url": "https://url.com"}
                    ],
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
def test_when_url_button_url_is_invalid__validation_error_is_raised(url):
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


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        CreateTemplate(
            **{
                "name": "exampl_ename",
                "language": "en",
                "category": "ACCOUNT_UPDATE",
                "structure": {
                    "header": {"format": "TEXT", "text": "Text example"},
                    "body": "example {{1}} body",
                    "footer": "some footer",
                    "buttons": [
                        {"type": "URL", "text": "url", "url": "http://url.com"},
                        {
                            "type": "PHONE_NUMBER",
                            "text": "number",
                            "phone_number": "38595873341",
                        },
                    ],
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
