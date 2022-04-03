import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.mms.models.query_parameters.get_mms_delivery_reports import (
    GetMMSDeliveryReportsQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetMMSDeliveryReportsQueryParameters(**{"bulkId": {}})


def test_when_message_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetMMSDeliveryReportsQueryParameters(**{"messageId": {}})


@pytest.mark.parametrize("limit", [{}, "ABC"])
def test_when_limit_is_invalid__validation_error_is_raised(limit):
    with pytest.raises(ValidationError):
        GetMMSDeliveryReportsQueryParameters(**{"limit": limit})


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GetMMSDeliveryReportsQueryParameters(
            **{"bulkId": "abc-123", "messageId": "bcd-334", "limit": 2}
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
