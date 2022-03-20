from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr, validator

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.whatsapp.models.body.action_sections import (
    SectionBase,
    SectionTitleValidatorMixin,
)
from infobip_channels.whatsapp.models.body.core import MessageBody


class HeaderTypeEnum(str, Enum):
    TEXT = "TEXT"


class Section(SectionBase):
    product_retailer_ids: List[str]


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Action(SectionTitleValidatorMixin, CamelCaseModel):
    catalog_id: str
    sections: conlist(Section, min_items=1, max_items=10)

    @validator("sections")
    def validate_section_titles(cls, sections: List[Section]) -> List[SectionBase]:
        super().validate_section_titles(sections)
        return sections


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
