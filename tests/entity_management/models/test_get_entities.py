import pytest
from pydantic import ValidationError

from infobip_platform.app_entities.models.query_parameters.get_entities import GetEntitiesQueryParameters


def test_when_page_is_negative__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetEntitiesQueryParameters(
            **{
                "page": -1,
            }
        )


@pytest.mark.parametrize("size", [0, 101])
def test_when_size_is_out_of_range__validation_error_is_raised(size):
    with pytest.raises(ValidationError):
        GetEntitiesQueryParameters(
            **{
                "size": size,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetEntitiesQueryParameters(
            **{
                "page": 1,
                "size": 10,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
