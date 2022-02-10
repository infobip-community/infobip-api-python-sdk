from enum import Enum
from typing import Optional

from pydantic import Field, constr
from pydantic_collections import BaseCollectionModel

from whatsapp.models.core import CamelCaseModel, MessageBody


class HeaderTypeEnum(str, Enum):
    text = "TEXT"


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Header(CamelCaseModel):
    header_type: HeaderTypeEnum = Field(alias="type")
    text: constr(min_length=1, max_length=60)


class Row(CamelCaseModel):
    id: constr(min_length=1, max_length=200)
    title: constr(min_length=1, max_length=24)
    description: constr(min_length=1, max_length=72) = None


class Rows(BaseCollectionModel[Row]):
    pass


class Section(CamelCaseModel):
    title: constr(min_length=1, max_length=24) = None
    rows: Rows


class Sections(BaseCollectionModel[Section]):
    pass


class Action(CamelCaseModel):
    title: constr(min_length=1, max_length=20)
    sections: Sections


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class ListMessageBody(MessageBody):
    content: Content