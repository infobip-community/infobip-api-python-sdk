from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel


class Entity(CamelCaseModel):
    entityName: Optional[constr(max_length=255)] = None
    entityId: Optional[constr(max_length=255)] = None
