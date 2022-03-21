from http import HTTPStatus
from typing import Optional

import requests
from pydantic import AnyHttpUrl, BaseModel, constr, validator


def to_camel_case(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]


def to_header_specific_case(string: str) -> str:
    return "-".join(word.capitalize() for word in string.split("_"))


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


class UrlLengthValidatorMixin:
    MAX_URL_LENGTH = 2048

    @classmethod
    def validate_url_length(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if len(value) > cls.MAX_URL_LENGTH:
            raise ValueError(f"Url length must be less than {cls.MAX_URL_LENGTH}")

        return value


class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class MessageBodyBase(CamelCaseModel):
    pass


class ResponseBase(CamelCaseModel):
    status_code: HTTPStatus
    raw_response: requests.Response

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True


class RequestHeaders(BaseModel):
    authorization: str
    accept: Optional[str] = "application/json"

    class Config:
        alias_generator = to_header_specific_case
        allow_population_by_field_name = True

    def __init__(self, **data: str) -> None:
        super().__init__(**data)
        self.authorization = f"App {self.authorization}"


class GetHeaders(RequestHeaders):
    pass


class PostHeaders(RequestHeaders):
    content_type: Optional[str] = "application/json"
