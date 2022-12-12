from typing import List

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class Verification(CamelCaseModel):
    msisdn: str
    verified: bool
    verified_at: int # TODO: check datetime
    sent_at: int


class GetTFAVerificationStatusResponse(ResponseBase):
    verifications: List[Verification]
