from typing import List, Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import AnyHttpUrl, Field, confloat, conlist, constr, validator

from infobip_channels.core.models import (
    CamelCaseModel,
    MessageBodyBase,
    UrlLengthValidatorMixin,
)
from infobip_channels.whatsapp.models.body.core import MessageBody


class ButtonQuickReply(CamelCaseModel):
    type: Literal["QUICK_REPLY"]
    parameter: constr(min_length=1, max_length=128)


class ButtonUrl(CamelCaseModel):
    type: Literal["URL"]
    parameter: str


class HeaderLocation(CamelCaseModel):
    type: Literal["LOCATION"]
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


class HeaderDocument(UrlLengthValidatorMixin, CamelCaseModel):
    type: Literal["DOCUMENT"]
    media_url: AnyHttpUrl
    filename: constr(min_length=1, max_length=240)

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class HeaderVideo(UrlLengthValidatorMixin, CamelCaseModel):
    type: Literal["VIDEO"]
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class HeaderImage(UrlLengthValidatorMixin, CamelCaseModel):
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

    @validator("placeholders", pre=True)
    def validate_placeholders(cls, placeholders: List[str]) -> List[str]:
        for placeholder in placeholders:
            if not placeholder:
                raise ValueError("Placeholder value must not be None or empty")

        return placeholders


class TemplateData(CamelCaseModel):
    body: Placeholders
    header: Optional[
        Union[HeaderText, HeaderImage, HeaderDocument, HeaderVideo, HeaderLocation]
    ] = None
    buttons: Optional[
        Union[conlist(ButtonUrl, max_items=1), conlist(ButtonQuickReply, max_items=3)]
    ] = None


class Content(CamelCaseModel):
    template_name: constr(
        min_length=1, max_length=512, regex=r"^[a-z0-9_]+$"  # noqa: F722
    )
    template_data: TemplateData
    language: constr(min_length=1)


class SmsFailover(CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    text: constr(min_length=1, max_length=4096)


class Message(MessageBody):
    content: Content
    sms_failover: Optional[SmsFailover] = None


class TemplateMessageBody(MessageBodyBase):
    messages: List[Message]
    bulk_id: Optional[constr(max_length=100)] = None
