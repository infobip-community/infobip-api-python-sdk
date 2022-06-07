import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.query_parameters.get_all_domains import (
    GetAllDomainsForAccountQueryParameters,
)


@pytest.mark.parametrize("size", ["", {}, 21, 0])
def test_when_size_is_invalid__validation_error_is_raised(size):
    with pytest.raises(ValidationError):
        GetAllDomainsForAccountQueryParameters(
            **{
                "size": size,
            }
        )


@pytest.mark.parametrize("page", ["", {}, -1])
def test_when_page_is_invalid__validation_error_is_raised(page):
    with pytest.raises(ValidationError):
        GetAllDomainsForAccountQueryParameters(
            **{
                "page": page,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetAllDomainsForAccountQueryParameters(
            **{
                "size": "20",
                "page": "1",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
