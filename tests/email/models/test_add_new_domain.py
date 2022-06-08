import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.add_new_domain import AddNewDomainMessageBody


def test_when_domain_name_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        AddNewDomainMessageBody(
            **{
                "domainName": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        AddNewDomainMessageBody(
            **{
                "domainName": "newDomain.com",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
