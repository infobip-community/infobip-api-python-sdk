from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import AnyUrl, Field, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class ButtonTypeEnum(str, Enum):
    reply = "REPLY"


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class HeaderDocument(CamelCaseModel):
    header_type: Literal["document"]
    media_url: AnyUrl
    filename: constr(min_length=1, max_length=240) = None


class HeaderVideo(CamelCaseModel):
    header_type: Literal["video"]
    media_url: AnyUrl


class HeaderImage(CamelCaseModel):
    header_type: Literal["image"]
    media_url: AnyUrl


class HeaderText(CamelCaseModel):
    header_type: Literal["text"]
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
    header: Optional[Union[HeaderText, HeaderImage, HeaderDocument, HeaderVideo]] = None
    footer: Optional[Footer] = None


class ButtonsMessageBody(MessageBody):
    content: Content
