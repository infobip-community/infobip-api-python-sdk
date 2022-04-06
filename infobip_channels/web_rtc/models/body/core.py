from typing import Optional

from pydantic import constr

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class AndroidServerKey(CamelCaseModel):
    fcm_server_key: constr(min_length=1)


class IosCertificates(CamelCaseModel):
    apns_certificate_file_name: constr(min_length=1)
    apns_certificate_file_content: constr(min_length=1)
    apns_certificate_password: Optional[str] = None


class ApplicationBody(MessageBodyBase):
    name: constr(min_length=1)
    description: Optional[constr(max_length=160)] = None
    ios: Optional[IosCertificates] = None
    android: Optional[AndroidServerKey] = None
    app_to_app: Optional[bool] = None
    app_to_conversations: Optional[bool] = None
    app_to_phone: Optional[bool] = None
