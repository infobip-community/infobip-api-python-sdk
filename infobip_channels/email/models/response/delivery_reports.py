from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class Error(CamelCaseModel):
    groupId: int
    groupName: str
    id: int
    name: str
    description: str
    permanent: bool


class Price(CamelCaseModel):
    pricePerMessage: int
    currency: str


class Result(CamelCaseModel):
    bulkId: Optional[str] = None
    messageId: str
    to: str
    sentAt: str
    doneAt: str
    messageCount: int
    price: Price
    status: ResponseStatus
    error: Error
    channel: str


class DeliveryReportsResponse(ResponseBase):
    results: List[Result]
