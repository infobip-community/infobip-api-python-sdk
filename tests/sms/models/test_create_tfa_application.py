import pytest
from pydantic import ValidationError

from infobip_channels.sms.models.body.create_tfa_application import CreateTFAApplicationBody


@pytest.mark.parametrize("name", ["", {}])
def test_when_name_is_none_or_empty__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        CreateTFAApplicationBody(
            **{
                "name": name,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        CreateTFAApplicationBody(
            **{
                "name": "some-application",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
