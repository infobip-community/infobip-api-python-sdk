import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.body.contact_message import ContactMessageBody
from infobip_channels.whatsapp.models.body.core import MessageBody
from tests.conftest import ContactMessageBodyFactory


def test_contact_message_body__is_an_instance_of_message_body():
    assert isinstance(ContactMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "contacts",
    [
        None,
        "",
        {},
        [{}],
        [
            {
                "addresses": [{"street": "street"}],
                "birthday": "1992-02-22",
                "emails": [{"email": "some_email@gmail.com"}],
                "org": {"company": "company"},
                "phones": [{"phone": "38598765123"}],
                "urls": [{"url": "https://url.com"}],
            }
        ],
    ],
)
def test_when_contacts_is_invalid__validation_error_is_raised(contacts):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(**{"content": {"contacts": contacts}})


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


@pytest.mark.parametrize(
    "name", [None, {}, {"firstName": "test"}, {"formattedName": "text"}]
)
def test_when_name_is_invalid__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(**{"content": {"contacts": [{"name": name}]}})


@pytest.mark.parametrize("first_name", [None, {}])
def test_when_first_name_type_is_invalid__validation_error_is_raised(first_name):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": first_name,
                                "formattedName": "Art Vandelay",
                            },
                        }
                    ]
                }
            }
        )


@pytest.mark.parametrize("formatted_name", [None, {}])
def test_when_formatted_name_type_is_invalid__validation_error_is_raised(
    formatted_name,
):
    with pytest.raises(ValidationError):
        ContactMessageBodyFactory.build(
            **{
                "content": {
                    "contacts": [
                        {
                            "name": {
                                "firstName": "First Name",
                                "formattedName": formatted_name,
                            },
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


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ContactMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "contacts": [
                        {
                            "addresses": [
                                {
                                    "street": "Istarska",
                                    "city": "Vodnjan",
                                    "zip": "52215",
                                    "country": "Croatia",
                                    "countryCode": "HR",
                                    "type": "WORK",
                                },
                                {
                                    "street": "Istarska",
                                    "city": "Vodnjan",
                                    "zip": "52215",
                                    "country": "Croatia",
                                    "countryCode": "HR",
                                    "type": "HOME",
                                },
                            ],
                            "birthday": "2010-01-01",
                            "emails": [
                                {"email": "John.Smith@example.com", "type": "WORK"},
                                {
                                    "email": "John.Smith.priv@example.com",
                                    "type": "HOME",
                                },
                            ],
                            "name": {
                                "firstName": "John",
                                "lastName": "Smith",
                                "middleName": "B",
                                "namePrefix": "Mr.",
                                "formattedName": "Mr. John Smith",
                            },
                            "org": {
                                "company": "Company Name",
                                "department": "Department",
                                "title": "Director",
                            },
                            "phones": [
                                {
                                    "phone": "+441134960019",
                                    "type": "HOME",
                                    "waId": "441134960019",
                                },
                                {
                                    "phone": "+441134960000",
                                    "type": "WORK",
                                    "waId": "441134960000",
                                },
                            ],
                            "urls": [
                                {
                                    "url": "http://example.com/John.Smith",
                                    "type": "WORK",
                                },
                                {
                                    "url": "http://example.com/home/John.Smith",
                                    "type": "HOME",
                                },
                            ],
                        }
                    ],
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
