import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import ContactMessageBodyFactory
from whatsapp.models.core import MessageBody


def test_contact_message_body__is_an_instance_of_message_body():
    assert isinstance(ContactMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("address_type", ["", {}, "TEST"])
def test_when_addresses_type_is_invalid__validation_error_is_raised(address_type):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "Art",
                                "formattedName": "Art Vandelay",
                            },
                            "addresses": [{"type": address_type}],
                        },
                    ]
                }
            }
        )


@pytest.mark.parametrize("test_type", ["", {}, "TEST"])
def test_when_emails_type_is_invalid__validation_error_is_raised(test_type):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "Art",
                                "formattedName": "Art Vandelay",
                            },
                            "emails": [{"type": test_type}],
                        }
                    ]
                }
            }
        )


@pytest.mark.parametrize("test_type", ["", {}, "TEST"])
def test_when_phones_type_is_invalid__validation_error_is_raised(test_type):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "Art",
                                "formattedName": "Art Vandelay",
                            },
                            "phones": [{"type": test_type}],
                        }
                    ]
                }
            }
        )


@pytest.mark.parametrize("test_type", ["", {}, "TEST"])
def test_when_urls_type_is_invalid__validation_error_is_raised(test_type):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "Art",
                                "formattedName": "Art Vandelay",
                            },
                            "urls": [{"type": test_type}],
                        }
                    ]
                }
            }
        )


@pytest.mark.parametrize("birthday", ["10-28-1950", "13-02-1911"])
def test_when_birthday_is_invalid__validation_error_is_raised(birthday):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "Art",
                                "formattedName": "Art Vandelay",
                            },
                            "birthday": birthday,
                        }
                    ]
                }
            }
        )
