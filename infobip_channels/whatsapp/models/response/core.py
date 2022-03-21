from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class WhatsAppResponseError(ResponseBase):
    request_error: RequestError


class ResponseOKStatus(CamelCaseModel):
    group_id: int
    group_name: str
    id: int
    name: str
    description: str
    action: Optional[str] = None


class WhatsAppResponseOKPayload(CamelCaseModel):
    to: str
    message_count: int
    message_id: str
    status: ResponseOKStatus


class WhatsAppResponseOK(WhatsAppResponseOKPayload, ResponseBase):
    pass
