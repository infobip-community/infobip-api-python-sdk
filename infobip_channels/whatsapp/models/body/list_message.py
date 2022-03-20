from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr, validator

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.whatsapp.models.body.action_sections import (
    SectionBase,
    SectionTitleValidatorMixin,
)
from infobip_channels.whatsapp.models.body.core import MessageBody

MESSAGE_ROWS_MAXIMUM_NUMBER = 10


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
    def validate_sections(cls, sections: List[Section]) -> List[SectionBase]:
        super().validate_section_titles(sections)
        cls._validate_row_id_uniqueness(sections)
        cls._validate_number_of_rows(sections)

        return sections

    @classmethod
    def _validate_row_id_uniqueness(cls, sections: List[Section]) -> None:
        row_ids = []
        for section in sections:
            for row in section.rows:
                if row.id in row_ids:
                    raise ValueError("Row ids must be unique across all sections")
                row_ids.append(row.id)

    @classmethod
    def _validate_number_of_rows(cls, sections: List[Section]) -> None:
        number_of_rows = 0
        for section in sections:
            number_of_rows += len(section.rows)

        if number_of_rows > MESSAGE_ROWS_MAXIMUM_NUMBER:
            raise ValueError(
                f"Message must have a maximum of {MESSAGE_ROWS_MAXIMUM_NUMBER} rows"
            )


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    body: Body
    action: Action
    header: Optional[Header] = None
    footer: Optional[Footer] = None


class ListMessageBody(MessageBody):
    content: Content
