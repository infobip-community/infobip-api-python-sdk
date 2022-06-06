from typing import Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class ServiceException(CamelCaseModel):
    message_id: str
    text: str


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class Price(CamelCaseModel):
    price_per_message: int
    currency: str


class ResultBase(CamelCaseModel):
    bulk_id: Optional[str] = None
    message_id: str
    to: str
    sent_at: str
    done_at: str
    message_count: int
    price: Price
    status: ResponseStatus


class BulksBase(ResponseBase):
    external_bulk_id: str


class BulkBase(CamelCaseModel):
    bulk_id: str


class EmailResponseError(ResponseBase):
    request_error: RequestError
