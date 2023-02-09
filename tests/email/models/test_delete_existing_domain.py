import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.path_parameters.delete_existing_domain import (
    DeleteExistingDomainPathParameter,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        DeleteExistingDomainPathParameter(
            **{
                "domainName": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        DeleteExistingDomainPathParameter(
            **{
                "domainName": "newDomain.com",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
