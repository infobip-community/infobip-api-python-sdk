from typing import List

from infobip_channels.core.models import CamelCaseModel, ResponseBase
from infobip_channels.email.models.response.core import ResultBase


class Error(CamelCaseModel):
    group_id: int
    group_name: str
    id: int
    name: str
    description: str
    permanent: bool


class Result(ResultBase):
    error: Error
    channel: str


class DeliveryReportsResponse(ResponseBase):
    results: List[Result]
