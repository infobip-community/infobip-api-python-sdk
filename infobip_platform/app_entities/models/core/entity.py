from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel


class Entity(CamelCaseModel):
    entity_name: Optional[constr(max_length=255)] = None
    entity_id: constr(min_length=1, max_length=255) = None
