from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class Error(CamelCaseModel):
    group_id: int
    group_name: str
    id: int
    name: str
    description: str
    permanent: bool


class Price(CamelCaseModel):
    price_per_message: int
    currency: str


class Result(CamelCaseModel):
    bulk_id: Optional[str] = None
    message_id: str
    to: str
    sent_at: str
    done_at: str
    message_count: int
    price: Price
    status: ResponseStatus
    error: Error
    channel: str


class DeliveryReportsResponse(ResponseBase):
    results: List[Result]
