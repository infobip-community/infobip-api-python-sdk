import json
import os
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from enum import Enum
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
from pydantic import AnyHttpUrl, BaseModel, constr, validator
from urllib3 import encode_multipart_formdata


def to_camel_case(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]


def to_header_specific_case(string: str) -> str:
    return "-".join(word.capitalize() for word in string.split("_"))


def url_encoding(string_to_encode: str, safe: str = "", encoding: str = "utf-8") -> str:
    """
    Special characters and user credentials are properly encoded.
    Use a URL encoding reference as a guide:
    https://www.w3schools.com/tags/ref_urlencode.asp

    The optional safe parameter specifies additional ASCII characters
    that should not be quoted — its default value is '/'.
    """
    return urllib.parse.quote(
        string_to_encode, safe=safe, encoding=encoding, errors=None
    )


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
    _MAX_URL_LENGTH = 2048

    @classmethod
    def validate_url_length(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if len(value) > cls._MAX_URL_LENGTH:
            raise ValueError(f"Url length must be less than {cls._MAX_URL_LENGTH}")

        return value


class FromAndToTimeValidator:
    _MINIMUM_DELIVERY_WINDOW_MINUTES = 60

    @classmethod
    def _validate_time_differences(cls, from_time, to_time):
        from_time_in_minutes = from_time.hour * 60 + from_time.minute
        to_time_in_minutes = to_time.hour * 60 + to_time.minute

        if (
            to_time_in_minutes - from_time_in_minutes
            < cls._MINIMUM_DELIVERY_WINDOW_MINUTES
        ):
            raise ValueError(
                f"Minimum of {cls._MINIMUM_DELIVERY_WINDOW_MINUTES} minutes has to pass "
                f"between from and to delivery window times."
            )

    @classmethod
    def validate_from_and_to(cls, values):
        if not values.get("from_time") and not values.get("to"):
            return values

        if values.get("from_time") and not values.get("to"):
            raise ValueError("If 'from_time' is set, 'to' has to be set also")

        if values.get("to") and not values.get("from_time"):
            raise ValueError("If 'to' is set, 'from_time' has to be set also")

        cls._validate_time_differences(values["from_time"], values["to"])

        return values


class DateTimeValidator:
    _MAX_TIME_LIMIT = 180
    _EXPECTED_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    @classmethod
    def convert_to_date_time_format(cls, value):
        if not value:
            return
        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        return value

    @classmethod
    def convert_time_to_correct_format(cls, value) -> str:
        date_time_format = cls.convert_to_date_time_format(value)

        return date_time_format.strftime(cls._EXPECTED_TIME_FORMAT)

    @classmethod
    def convert_time_to_correct_format_validate_limit(cls, value):

        date_time_format = cls.convert_to_date_time_format(value)

        if date_time_format > datetime.now() + timedelta(days=cls._MAX_TIME_LIMIT):
            raise ValueError(
                "Scheduled message must be sooner than 180 days from today"
            )

        return value.strftime(cls._EXPECTED_TIME_FORMAT)


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
    pass


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


class LanguageEnum(str, Enum):
    TURKISH = "TR"
    SPANISH = "ES"
    PORTUGUESE = "PT"
    AUTODETECT = "AUTODETECT"


class TransliterationEnum(str, Enum):
    TURKISH = "TURKISH"
    GREEK = "GREEK"
    CYRILLIC = "CYRILLIC"
    SERBIAN_CYRILLIC = "SERBIAN_CYRILLIC"
    CENTRAL_EUROPEAN = "CENTRAL_EUROPEAN"
    BALTIC = "BALTIC"
    NON_UNICODE = "NON_UNICODE"


class GeneralStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    PENDING = "PENDING"
    UNDELIVERABLE = "UNDELIVERABLE"
    DELIVERED = "DELIVERED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class MessageStatus(str, Enum):
    PENDING = "PENDING"
    PAUSED = "PAUSED"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class DaysEnum(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class ContentTypeEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"


class MultipartMixin:
    """Mixin used for allowing models to export their fields to a multipart/form-data
    format. Field types currently supported are listed in the
    _FIELD_TYPE_TO_MULTIPART_INFO_MAP attribute. All other BaseModel type fields are
    covered with the _JSON_INFO attribute.
    """

    _FIELD_TYPE_TO_MULTIPART_INFO_MAP: Dict = {
        "str": {"is_file": False, "content_type": "text/plain"},
        "int": {"is_file": False, "content_type": "text/plain"},
        "AnyHttpUrl": {"is_file": False, "content_type": "text/plain"},
        "StrictBool": {"is_file": False, "content_type": "text/plain"},
        "ContentTypeEnum": {"is_file": False, "content_type": "text/plain"},
        "ConstrainedStrValue": {"is_file": False, "content_type": "text/plain"},
        "datetime": {"is_file": False, "content_type": "text/plain"},
        "IOBase": {"is_file": True, "content_type": ""},
        "XML": {"is_file": False, "content_type": "application/xml"},
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
                field_object.alias,
                getattr(self, field_name),
                field_object.type_,
            )

        return encode_multipart_formdata(multipart_fields)

    def _add_multipart_tuple(
        self, multipart_fields: Dict, field_name: str, field_value: Any, field_type: Any
    ) -> None:
        if not field_value:
            return

        """
        In case of Union we have complex field type
        str(field_type) is 'typing.Union[str, int, NoneType]'
        """
        if "Union" in str(field_type):
            """
            field_subtypes gives ['str', 'int', 'NoneType']
            """
            field_subtypes = str(field_type).split("[")[1].strip("]").split(", ")
            for f in field_subtypes:
                if f in self._FIELD_TYPE_TO_MULTIPART_INFO_MAP:
                    field_info = self._FIELD_TYPE_TO_MULTIPART_INFO_MAP[f]
                    break
            else:
                field_info = self._JSON_INFO
        else:
            field_info = self._FIELD_TYPE_TO_MULTIPART_INFO_MAP.get(
                field_type.__name__, self._JSON_INFO
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
