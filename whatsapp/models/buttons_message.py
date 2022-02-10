from enum import Enum
from typing import Dict, List, Optional

from pydantic import AnyUrl, Field, constr, validator

from whatsapp.models.core import CamelCaseModel, MessageBody


class ButtonTypeEnum(str, Enum):
    reply = "REPLY"


class HeaderTypeEnum(str, Enum):
    text = "TEXT"
    video = "VIDEO"
    image = "IMAGE"
    document = "DOCUMENT"


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class HeaderDocument(CamelCaseModel):
    header_type: HeaderTypeEnum = Field(alias="type")
    media_url: AnyUrl
    filename: constr(min_length=1, max_length=240) = None


class HeaderVideo(CamelCaseModel):
    header_type: HeaderTypeEnum = Field(alias="type")
    media_url: AnyUrl


class HeaderImage(CamelCaseModel):
    header_type: HeaderTypeEnum = Field(alias="type")
    media_url: AnyUrl


class HeaderText(CamelCaseModel):
    header_type: HeaderTypeEnum = Field(alias="type")
    text: constr(min_length=1, max_length=60)


class Button(CamelCaseModel):
    button_type: ButtonTypeEnum = Field(alias="type")
    id: constr(min_length=1, max_length=256)
    title: constr(min_length=1, max_length=20)


class Action(CamelCaseModel):
    buttons: List[Button]


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Dict[str, str]] = None
    footer: Optional[Footer] = None

    @validator("header")
    def validate_header(cls, value):
        if value:
            header_value = value.get("type")

            if header_value == HeaderTypeEnum.text:
                return HeaderText(**value)
            elif header_value == HeaderTypeEnum.image:
                return HeaderImage(**value)
            elif header_value == HeaderTypeEnum.video:
                return HeaderVideo(**value)
            elif header_value == HeaderTypeEnum.document:
                return HeaderDocument(**value)

            raise ValueError("Unsupported header type")


class ButtonsMessageBody(MessageBody):
    content: Content
