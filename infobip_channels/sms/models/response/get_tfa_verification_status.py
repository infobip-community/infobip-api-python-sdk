from typing import List

from infobip_channels.core.models import ResponseBase


class Verification(ResponseBase):
    msisdn: str
    verified: bool
    verified_at: int
    sent_at: int


class GetTFAVerificationStatusResponse(ResponseBase):
    verifications: List[Verification]
