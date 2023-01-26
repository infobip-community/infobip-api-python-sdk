import pytest
from pydantic import ValidationError

from infobip_channels.sms.models.body.update_tfa_application import (
    UpdateTFAApplicationBody,
)


@pytest.mark.parametrize("name", ["", {}])
def test_when_name_is_empty__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        UpdateTFAApplicationBody(
            **{
                "name": name,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        UpdateTFAApplicationBody(
            **{
                "messageText": "some-text",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
