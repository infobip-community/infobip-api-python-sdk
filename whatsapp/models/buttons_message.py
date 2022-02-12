from enum import Enum
from typing import Literal, Optional, Union

from pydantic import AnyUrl, conlist, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class ButtonTypeEnum(str, Enum):
    REPLY = "REPLY"


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class HeaderDocument(CamelCaseModel):
    type: Literal["DOCUMENT"]
    media_url: AnyUrl
    filename: constr(min_length=1, max_length=240) = None


class HeaderVideo(CamelCaseModel):
    type: Literal["VIDEO"]
    media_url: AnyUrl


class HeaderImage(CamelCaseModel):
    type: Literal["IMAGE"]
    media_url: AnyUrl


class HeaderText(CamelCaseModel):
    type: Literal["TEXT"]
    text: constr(min_length=1, max_length=60)


class Button(CamelCaseModel):
    type: ButtonTypeEnum
    id: constr(min_length=1, max_length=256)
    title: constr(min_length=1, max_length=20)


class Action(CamelCaseModel):
    buttons: conlist(Button, min_items=1, max_items=3)


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Union[HeaderText, HeaderImage, HeaderDocument, HeaderVideo]] = None
    footer: Optional[Footer] = None


class ButtonsMessageBody(MessageBody):
    content: Content
