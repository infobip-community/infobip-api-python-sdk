from datetime import datetime
from typing import List, Optional, Union

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
    send_at: Optional[Union[datetime, str]] = None
    done_at: Optional[Union[datetime, str]] = None
    sms_count: Optional[int] = None
    price: Optional[Price] = None
    status: Optional[ResponseStatus] = None
    error: Optional[Error] = None


class OutboundDeliveryReportsResponse(ResponseBase):
    results: List[Result]
