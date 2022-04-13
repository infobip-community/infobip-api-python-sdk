from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class RcsResponseError(ResponseBase):
    request_error: RequestError


class SendRcsResponseMessage(CamelCaseModel):
    to: Optional[str] = None
    message_count: Optional[int] = None
    message_id: Optional[str] = None
    status: ResponseStatus


class RcsResponseOK(ResponseBase):
    messages: List[SendRcsResponseMessage]


class Message(CamelCaseModel):
    messages: List[SendRcsResponseMessage]


class RcsResponseOKList(ResponseBase):
    list: List[Message]
