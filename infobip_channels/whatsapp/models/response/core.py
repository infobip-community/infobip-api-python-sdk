from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class WhatsAppResponseError(ResponseBase):
    request_error: RequestError


class WhatsAppResponseOKPayload(CamelCaseModel):
    to: str
    message_count: int
    message_id: str
    status: ResponseStatus


class WhatsAppResponseOK(WhatsAppResponseOKPayload, ResponseBase):
    pass
