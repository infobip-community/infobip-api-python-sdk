from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr

from infobip_channels.whatsapp.models.core import CamelCaseModel, MessageBody


class HeaderTypeEnum(str, Enum):
    TEXT = "TEXT"


class Section(CamelCaseModel):
    title: Optional[constr(min_length=1, max_length=24)]
    product_retailer_ids: List[str]


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Action(CamelCaseModel):
    catalog_id: str
    sections: conlist(Section, min_items=1, max_items=10)


class Header(CamelCaseModel):
    type: HeaderTypeEnum
    text: constr(min_length=1, max_length=60)


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    header: Header
    body: Body
    action: Action
    footer: Optional[Footer] = None


class MultiProductMessageBody(MessageBody):
    content: Content
