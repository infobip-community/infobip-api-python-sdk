from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr, validator

from infobip_channels.whatsapp.models.action_sections import (
    SectionBase,
    SectionTitleValidatorMixin,
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


class Action(SectionTitleValidatorMixin, CamelCaseModel):
    title: constr(min_length=1, max_length=20)
    sections: conlist(Section, min_items=1, max_items=10)

    @validator("sections")
    def validate_section_titles(cls, sections: List[Section]) -> List[SectionBase]:
        super().validate_section_titles(sections)

        row_ids = []
        for section in sections:
            for row in section.rows:
                if row.id in row_ids:
                    raise ValueError("Row ids must be unique across all sections")
                row_ids.append(row.id)

        return sections


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class ListMessageBody(MessageBody):
    content: Content
