import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.query_parameters.get_sent_bulks import (
    GetSentBulksQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetSentBulksQueryParameters(
            **{
                "bulkId": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetSentBulksQueryParameters(
            **{
                "bulkId": "BULK-ID-123-xyz",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
