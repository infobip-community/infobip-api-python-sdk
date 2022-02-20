from enum import Enum
from typing import List, Optional

from pydantic import conlist, constr, validator

from infobip_channels.whatsapp.models.core import CamelCaseModel, MessageBody


class HeaderTypeEnum(str, Enum):
    TEXT = "TEXT"


class Section(CamelCaseModel):
    title: Optional[constr(max_length=24)]
    product_retailer_ids: conlist(str, min_items=1)


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Action(CamelCaseModel):
    catalog_id: str
    sections: conlist(Section, min_items=1, max_items=10)

    @validator("sections")
    def validate_sections(cls, sections: List[Section]) -> List[Section]:
        if len(sections) > 1:
            for section in sections:
                if not section.dict().get("title"):
                    raise ValueError(
                        "When there is more than one section, "
                        "each one of them needs to have a title"
                    )

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
