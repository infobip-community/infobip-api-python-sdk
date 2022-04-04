from typing import List, Optional

from pydantic import Field

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus
from infobip_channels.mms.models.response.core import Price


class Error(CamelCaseModel):
    group_id: Optional[int] = None
    group_name: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None


class Result(CamelCaseModel):
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    to: Optional[str] = None
    from_id: Optional[str] = Field(default=None, alias="from")
    sent_at: Optional[str] = None
    done_at: Optional[str] = None
    mms_count: Optional[int] = None
    mcc_mnc: Optional[str] = None
    callback_data: Optional[str] = None
    price: Optional[Price] = None
    status: Optional[ResponseStatus] = None
    error: Optional[Error] = None


class GetMMSDeliveryReportsResponse(ResponseBase):
    results: Optional[List[Result]] = None
