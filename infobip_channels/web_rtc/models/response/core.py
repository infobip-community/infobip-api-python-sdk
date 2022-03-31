from typing import Dict, List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class ServiceException(CamelCaseModel):
    message_id: str
    text: str
    validation_errors: Optional[Dict[str, List[str]]] = None


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class WebRtcResponseError(ResponseBase):
    request_error: RequestError


class AndroidServerKey(CamelCaseModel):
    fcm_server_key: str


class IosCertificate(CamelCaseModel):
    apns_certificate_file_name: str
    apns_certificate_password: str


class WebRtcResponseOKPayload(CamelCaseModel):
    id: str
    name: str
    description: str
    ios: Optional[IosCertificate] = None
    android: Optional[AndroidServerKey] = None
    app_to_app: bool
    app_to_conversations: bool
    app_to_phone: bool


class WebRtcResponseOK(WebRtcResponseOKPayload, ResponseBase):
    pass
