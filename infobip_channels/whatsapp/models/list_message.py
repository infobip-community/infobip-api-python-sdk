from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr, validator

from infobip_channels.whatsapp.models.action_sections import (
    SectionBase,
    SectionValidatorMixin,
)
from infobip_channels.whatsapp.models.core import CamelCaseModel, MessageBody


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


class Section(SectionBase):
    title: Optional[constr(max_length=24)] = None
    rows: conlist(Row, min_items=1)


class Action(SectionValidatorMixin, CamelCaseModel):
    title: constr(min_length=1, max_length=20)
    sections: conlist(Section, min_items=1, max_items=10)

    @validator("sections")
    def validate_sections(cls, sections: List[Section]) -> List[SectionBase]:
        return super().validate_sections(sections)


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class ListMessageBody(MessageBody):
    content: Content
