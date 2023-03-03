from typing import Optional

from pydantic.types import conint

from infobip_channels.core.models import QueryParameter


class GetEntitiesQueryParameters(QueryParameter):
    page: Optional[conint(ge=0)] = 0
    size: Optional[conint(ge=1, le=100)] = 20
