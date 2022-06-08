import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.validate_email_adresses import (
    ValidateEmailAddressesMessageBody,
)


def test_when_to_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        ValidateEmailAddressesMessageBody(
            **{
                "to": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ValidateEmailAddressesMessageBody(
            **{
                "to": "test@test.com",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
