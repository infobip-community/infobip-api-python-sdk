from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr

from infobip_channels.whatsapp.models.body.core import CamelCaseModel, MessageBody


class HeaderTypeEnum(str, Enum):
    TEXT = "TEXT"


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Header(CamelCaseModel):
    type: HeaderTypeEnum
    text: constr(min_length=1, max_length=60)


class Row(CamelCaseModel):
    id: constr(min_length=1, max_length=200)
    title: constr(min_length=1, max_length=24)
    description: Optional[constr(max_length=72)] = None


class Section(CamelCaseModel):
    title: constr(max_length=24) = None
    rows: List[Row]


class Action(CamelCaseModel):
    title: constr(min_length=1, max_length=20)
    sections: conlist(Section, min_items=1, max_items=10)


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class ListMessageBody(MessageBody):
    content: Content
