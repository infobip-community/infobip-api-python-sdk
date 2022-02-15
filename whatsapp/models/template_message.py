from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import AnyHttpUrl, Field, confloat, constr, validator

from whatsapp.models.core import CamelCaseModel, MessageBody, ValidateUrlLengthMixin


class ButtonTypeEnum(str, Enum):
    QUICK_REPLY = "QUICK_REPLY"
    URL = "URL"


class Buttons(CamelCaseModel):
    type: ButtonTypeEnum
    parameter: str


class HeaderLocation(CamelCaseModel):
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


class HeaderDocument(ValidateUrlLengthMixin, CamelCaseModel):
    type: Literal["DOCUMENT"]
    media_url: AnyHttpUrl
    filename: constr(max_length=240)

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class HeaderVideo(ValidateUrlLengthMixin, CamelCaseModel):
    type: Literal["VIDEO"]
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class HeaderImage(ValidateUrlLengthMixin, CamelCaseModel):
    type: Literal["IMAGE"]
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class HeaderText(CamelCaseModel):
    type: Literal["TEXT"]
    placeholder: str


class Placeholders(CamelCaseModel):
    placeholders: List[str]


class TemplateData(CamelCaseModel):
    body: Placeholders
    header: Optional[
        Union[HeaderText, HeaderImage, HeaderDocument, HeaderVideo, HeaderLocation]
    ] = None
    buttons: Optional[Buttons] = None


class Content(CamelCaseModel):
    template_name: constr(min_length=1, max_length=512)
    template_data: TemplateData
    language: str


class SmsFailover(CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    text: constr(min_length=1, max_length=4096)


class Message(MessageBody):
    content: Content
    sms_failover: Optional[SmsFailover] = None


class TemplateMassageBody(CamelCaseModel):
    messages: List[Message]
    bulkId: Optional[constr(max_length=100)]
