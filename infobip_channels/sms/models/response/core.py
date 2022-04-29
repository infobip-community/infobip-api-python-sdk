from typing import Dict, List, Optional

from pydantic import StrictBool

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class SMSResponseError(ResponseBase):
    request_error: RequestError


class Error(ResponseStatus):
    permanent: Optional[StrictBool] = None


class Price(CamelCaseModel):
    price_per_message: Optional[float] = None
    currency: Optional[str] = None


class CoreResult(CamelCaseModel):
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    to: Optional[str] = None
    sent_at: Optional[str] = None
    done_at: Optional[str] = None
    sms_count: Optional[int] = None
    price: Optional[Price] = None
    status: Optional[ResponseStatus] = None
    error: Optional[Error] = None


class ScheduledSMSMessages(ResponseBase):
    bulk_id: str
