from typing import List, Optional

from pydantic import StrictBool

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class Error(ResponseStatus):
    permanent: Optional[StrictBool] = None


class Price(CamelCaseModel):
    price_per_message: Optional[float] = None
    currency: Optional[str] = None


class Result(CamelCaseModel):
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    to: Optional[str] = None
    sent_at: Optional[str] = None
    done_at: Optional[str] = None
    sms_count: Optional[int] = None
    price: Optional[Price] = None
    status: Optional[ResponseStatus] = None
    error: Optional[Error] = None


class OutboundDeliveryReportsResponse(ResponseBase):
    results: List[Result]
