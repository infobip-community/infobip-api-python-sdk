from typing import List, Optional

from pydantic import constr

from infobip_channels.core.models import CamelCaseModel


class SectionBase(CamelCaseModel):
    title: Optional[constr(max_length=24)] = None


class SectionTitleValidatorMixin:
    @classmethod
    def validate_section_titles(cls, sections: List[SectionBase]) -> None:
        if len(sections) > 1:
            for section in sections:
                if not section.title:
                    raise ValueError(
                        "When there is more than one section, "
                        "each one of them needs to have a title"
                    )
