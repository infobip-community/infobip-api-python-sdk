from typing import List

from infobip_channels.core.models import CamelCaseModel, ResponseBase
from infobip_channels.email.models.response.core import ResultDomain


class Paging(CamelCaseModel):
    page: int
    size: int
    total_pages: int
    total_results: int


class GetAllDomainsForAccountResponse(ResponseBase):
    paging: Paging
    results: List[ResultDomain]
