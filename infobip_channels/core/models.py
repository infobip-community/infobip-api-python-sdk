import json
import os
import xml.etree.ElementTree as ET
from http import HTTPStatus
from io import IOBase
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
from pydantic import AnyHttpUrl, BaseModel, constr, validator
from urllib3 import encode_multipart_formdata


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


class ResponseStatus(CamelCaseModel):
    group_id: int
    group_name: str
    id: int
    name: str
    description: str
    action: Optional[str] = None


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


class PutHeaders(RequestHeaders):
    content_type: Optional[str] = "application/json"


class DeleteHeaders(RequestHeaders):
    pass


class PathParameter(CamelCaseModel):
    sender: str


class QueryParameter(CamelCaseModel):
    pass


class XML(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("String required")

        if not value:
            return

        try:
            ET.fromstring(value)
        except ET.ParseError:
            raise ValueError("Invalid XML string sent")

        return cls(value)


class MultipartMixin:
    """Mixin used for allowing models to export their fields to a multipart/form-data
    format. Field types currently supported are listed in the
    _FIELD_TYPE_TO_MULTIPART_INFO_MAP attribute. All other BaseModel type fields are
    covered with the _JSON_INFO attribute.
    """

    _FIELD_TYPE_TO_MULTIPART_INFO_MAP: Dict = {
        str: {"is_file": False, "content_type": "text/plain"},
        IOBase: {"is_file": True, "content_type": ""},
        XML: {"is_file": False, "content_type": "application/xml"},
    }

    _JSON_INFO: Dict = {"is_file": False, "content_type": "application/json"}

    def to_multipart(self) -> Tuple[bytes, str]:
        """Export model's fields to a multipart/form-data format. The method returns
        a tuple of binary type body to send via POST request, and the content_type
        of the body including the multipart boundary.
        The resulting multipart_fields dictionary will have the model's field names as
        its keys and the tuples describing fields' multipart format as their values.

        For a Pydantic model with a "name: str" field and an "address: Address" field,
        the resulting multipart_fields dictionary would look like:

         multipart_fields = {
            "name": (None, "some name", "text/plain"),
            "address:" (None, {"street": "...", "city": "..."}, "application/json")
        }

        The tuple format is enforced by the urllib3's encode_multipart_formdata
        function: (filename, data, MIME type), where the MIME type is optional.
        The filename is None for all non-file types.

        :return: Tuple of binary encoded body and the multipart's content_type
        """
        multipart_fields = {}

        for field_name, field_object in self.__fields__.items():
            self._add_multipart_tuple(
                multipart_fields,
                to_camel_case(field_name),
                getattr(self, field_name),
                field_object.type_,
            )

        return encode_multipart_formdata(multipart_fields)

    def _add_multipart_tuple(
        self, multipart_fields: Dict, field_name: str, field_value: Any, field_type: Any
    ) -> None:
        if not field_value:
            return

        field_info = self._FIELD_TYPE_TO_MULTIPART_INFO_MAP.get(
            field_type, self._JSON_INFO
        )
        multipart_fields[field_name] = self._get_multipart_tuple(
            field_value, field_info
        )

    def _get_multipart_tuple(self, field_value: Any, field_info: Dict) -> Tuple:
        if field_info["is_file"]:
            return os.path.basename(field_value.name), field_value.read()

        if field_info["content_type"] == "application/json":
            field_value = self._get_json_for_field(field_value)

        return None, field_value, field_info["content_type"]

    @staticmethod
    def _get_json_for_field(model: Union[CamelCaseModel, List[CamelCaseModel]]) -> str:
        if isinstance(model, list):
            model_aliased = [item.dict(by_alias=True) for item in model]
        else:
            model_aliased = model.dict(by_alias=True)

        return json.dumps(model_aliased)
