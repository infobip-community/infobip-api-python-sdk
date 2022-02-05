from http import HTTPStatus
from typing import Dict, List, Optional

import requests
from pydantic import AnyHttpUrl, BaseModel, Field, constr


def to_camel_case(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]


class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class MessageBody(CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    to: constr(min_length=1, max_length=24)
    message_id: Optional[constr(max_length=50)] = None
    callback_data: Optional[constr(max_length=4000)] = None
    notify_url: Optional[AnyHttpUrl] = None


class WhatsappResponse(CamelCaseModel):
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


class WhatsappResponseError(WhatsappResponse):
    request_error: RequestError


class ResponseOKStatus(CamelCaseModel):
    group_id: int
    group_name: str
    id: int
    name: str
    description: str
    action: Optional[str] = None


class WhatsappResponseOK(WhatsappResponse):
    to: str
    message_count: int
    message_id: str
    status: ResponseOKStatus


def to_header_specific_case(string: str) -> str:
    return "-".join(word.capitalize() for word in string.split("_"))


class RequestHeaders(BaseModel):
    authorization: str
    content_type: Optional[str] = "application/json"
    accept: Optional[str] = "application/json"

    class Config:
        alias_generator = to_header_specific_case
        allow_population_by_field_name = True

    def __init__(self, **data: str) -> None:
        super().__init__(**data)
        self.authorization = f"App {self.authorization}"


class Authentication(BaseModel):
    base_url: AnyHttpUrl
    api_key: constr(min_length=1)
