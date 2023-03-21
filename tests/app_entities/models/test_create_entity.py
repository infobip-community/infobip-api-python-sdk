import pytest
from pydantic import ValidationError

from infobip_platform.app_entities.models.body.create_entity import CreateEntityBody


def test_when_name_is_long__validation_error_is_raised():
    with pytest.raises(ValidationError):
        CreateEntityBody(
            **{
                "entityName": "x" * 256,
                "entityId": "some-entity",
            }
        )


def test_when_id_is_long__validation_error_is_raised():
    with pytest.raises(ValidationError):
        CreateEntityBody(
            **{
                "entityId": "x" * 256,
            }
        )


@pytest.mark.parametrize("entity_id", ["", {}])
def test_when_id_is_empty__validation_error_is_raised(entity_id):
    with pytest.raises(ValidationError):
        CreateEntityBody(
            **{
                "entityId": entity_id,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        CreateEntityBody(
            **{
                "entityName": "Some entity",
                "entityId": "some-entity",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
