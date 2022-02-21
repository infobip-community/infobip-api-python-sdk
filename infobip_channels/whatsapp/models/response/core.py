from http import HTTPStatus
from typing import Dict, List, Optional

import requests
from pydantic import AnyHttpUrl, BaseModel, Field, constr, validator


def to_camel_case(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]


class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class ValidateUrlLengthMixin:
    MAX_URL_LENGTH = 2048

    @classmethod
    def validate_url_length(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if len(value) > cls.MAX_URL_LENGTH:
            raise ValueError(f"Url length must be less than {cls.MAX_URL_LENGTH}")

        return value


class MessageBody(ValidateUrlLengthMixin, CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    to: constr(min_length=1, max_length=24)
    message_id: Optional[constr(max_length=50)] = None
    callback_data: Optional[constr(max_length=4000)] = None
    notify_url: Optional[AnyHttpUrl] = None

    @validator("notify_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class PathParameter(CamelCaseModel):
    path_parameter: str


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


class WhatsAppResponseOK(WhatsAppResponse):
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

    @validator("base_url", pre=True)
    def validate_scheme(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if value.startswith(("http://", "https://")):
            return value

        return f"https://{value}"
