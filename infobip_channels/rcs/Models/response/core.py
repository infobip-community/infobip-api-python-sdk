from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class RCSResponseError(ResponseBase):
    request_error: RequestError


class SendRcsResponseMessage(CamelCaseModel):
    to: Optional[str] = None
    message_count: Optional[int] = None
    message_id: Optional[str] = None
    status: ResponseStatus


class RCSResponseOK(ResponseBase):
    messages: List[SendRcsResponseMessage]


class Message(CamelCaseModel):
    messages: List[SendRcsResponseMessage]


class RCSResponseOKList(ResponseBase):
    list: List[Message]
