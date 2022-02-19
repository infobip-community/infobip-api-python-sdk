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


class Section(SectionBase):
    product_retailer_ids: conlist(str, min_items=1)


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Action(SectionValidatorMixin, CamelCaseModel):
    catalog_id: str
    sections: conlist(Section, min_items=1, max_items=10)

    @validator("sections")
    def validate_sections(cls, sections: List[Section]) -> List[SectionBase]:
        return super().validate_sections(sections)


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
