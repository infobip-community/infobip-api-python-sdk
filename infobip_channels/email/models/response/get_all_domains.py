from typing import List

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class Paging(CamelCaseModel):
    page: int
    size: int
    total_pages: int
    total_results: int


class Tracking(CamelCaseModel):
    clicks: int
    opens: int
    unsubscribe: int


class DnsRecord(CamelCaseModel):
    record_type: str
    name: str
    expected_value: str
    verified: bool


class Result(CamelCaseModel):
    domain_id: int
    domain_name: str
    active: bool
    tracking: Tracking
    dns_records: List[DnsRecord]
    blocked: int
    created_at: str


class GetAllDomainsForAccountResponse(ResponseBase):
    paging: Paging
    results: List[Result]
