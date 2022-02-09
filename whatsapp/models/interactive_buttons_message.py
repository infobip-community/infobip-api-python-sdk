from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, constr

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


class Text(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class MediaUrl(CamelCaseModel):
    media_url: AnyUrl


class ImageUrl(CamelCaseModel):
    media_url: AnyUrl


class DocumentUrl(CamelCaseModel):
    media_url: AnyUrl
    filename: constr(min_length=1, max_length=240) = None


class Header(CamelCaseModel):
    type: HeaderTypeEnum


class Button(CamelCaseModel):
    type: ButtonTypeEnum
    id: constr(min_length=1, max_length=256)
    title: constr(min_length=1, max_length=20)


class Action(CamelCaseModel):
    buttons: List[Button]


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class InteractiveButtonsMessageBody(MessageBody):
    content: Content
