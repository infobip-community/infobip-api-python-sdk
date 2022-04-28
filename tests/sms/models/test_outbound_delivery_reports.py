import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.get_outbound_delivery_reports import (
    GetOutboundSMSDeliveryReportsQueryParameters,
)


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSDeliveryReportsQueryParameters(
            **{
                "bulkId": {},
                "messageId": "MESSAGE-ID-123-xyz",
                "limit": 2,
            }
        )


def test_when_message_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSDeliveryReportsQueryParameters(
            **{
                "bulkId": "BULK-ID-123-xyz",
                "messageId": {},
                "limit": 2,
            }
        )


def test_when_limit_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        GetOutboundSMSDeliveryReportsQueryParameters(
            **{
                "bulkId": "BULK-ID-123-xyz",
                "messageId": "MESSAGE-ID-123-xyz",
                "limit": {},
            }
        )
