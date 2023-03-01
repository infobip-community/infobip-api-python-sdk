from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_platform.app_entities.models.core.entity import Entity
from infobip_platform.app_entities.models.response.core import Paging


class GetEntitiesResponse(ResponseBase):
    results: List[Entity]
    paging: Paging
