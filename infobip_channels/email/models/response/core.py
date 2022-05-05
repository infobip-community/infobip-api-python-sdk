from infobip_channels.core.models import CamelCaseModel, ResponseBase


class ServiceException(CamelCaseModel):
    message_id: str
    text: str


class RequestError(CamelCaseModel):
    service_exception: ServiceException


class EmailResponseError(ResponseBase):
    request_error: RequestError
