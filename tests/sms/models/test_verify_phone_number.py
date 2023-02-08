import pytest
from pydantic import ValidationError

from infobip_channels.sms.models.body.verify_phone_number import VerifyPhoneNumberBody


@pytest.mark.parametrize("pin", ["", {}])
def test_when_pin_is_empty__validation_error_is_raised(pin):
    with pytest.raises(ValidationError):
        VerifyPhoneNumberBody(
            **{
                "pin": pin,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        VerifyPhoneNumberBody(
            **{
                "pin": "1234",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
