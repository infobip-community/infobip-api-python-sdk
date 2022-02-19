from typing import List, Optional

from pydantic import constr

from infobip_channels.whatsapp.models.core import CamelCaseModel


class SectionBase(CamelCaseModel):
    title: Optional[constr(max_length=24)] = None


class SectionValidatorMixin:
    @classmethod
    def validate_sections(cls, sections: List[SectionBase]) -> List[SectionBase]:
        if len(sections) > 1:
            for section in sections:
                if not section.dict().get("title"):
                    raise ValueError(
                        "When there is more than one section, "
                        "each one of them needs to have a title"
                    )

        return sections
