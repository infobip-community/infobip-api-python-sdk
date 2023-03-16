import pytest
from pydantic import ValidationError

from infobip_platform.app_entities.models.body.modify_entity import ModifyEntityBody


def test_when_name_is_long__validation_error_is_raised():
    with pytest.raises(ValidationError):
        ModifyEntityBody(
            **{
                "entityName": "x" * 256,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ModifyEntityBody(
            **{
                "entityName": "Some Entity",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
