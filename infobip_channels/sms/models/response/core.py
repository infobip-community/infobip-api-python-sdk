from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class SMSResponseError(ResponseBase):
    request_error: RequestError
