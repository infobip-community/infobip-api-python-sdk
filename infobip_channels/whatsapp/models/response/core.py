from http import HTTPStatus
from typing import Dict, List, Optional

import requests

from infobip_channels.whatsapp.models.core import CamelCaseModel


class WhatsAppResponse(CamelCaseModel):
    status_code: HTTPStatus
    raw_response: requests.Response

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class WhatsAppResponseError(WhatsAppResponse):
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


class WhatsAppResponseOK(WhatsAppResponseOKPayload, WhatsAppResponse):
    pass
