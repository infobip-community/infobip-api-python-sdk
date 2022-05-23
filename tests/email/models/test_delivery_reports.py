import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.query_parameters.delivery_reports import (
    DeliveryReportsQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        DeliveryReportsQueryParameters(
            **{
                "bulkId": {},
            }
        )


def test_when_message_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        DeliveryReportsQueryParameters(
            **{
                "messageId": {},
            }
        )


def test_when_limit_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        DeliveryReportsQueryParameters(
            **{
                "limit": {},
            }
        )
