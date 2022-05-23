from typing import List

from pydantic import Field

from infobip_channels.core.models import ResponseBase
from infobip_channels.email.models.response.core import ResultBase


class Result(ResultBase):
    from_email: str = Field(alias="from")
    text: str


class GetLogsResponse(ResponseBase):
    results: List[Result]
