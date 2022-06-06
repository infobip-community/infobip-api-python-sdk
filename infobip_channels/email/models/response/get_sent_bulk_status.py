from typing import List

from infobip_channels.email.models.response.core import BulkBase, BulksBase


class Bulk(BulkBase):
    status: str


class GetSentEmailBulksStatusResponse(BulksBase):
    bulks: List[Bulk]
