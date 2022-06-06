from typing import List

from infobip_channels.email.models.response.core import BulkBase, BulksBase


class Bulk(BulkBase):
    send_at: str


class GetSentEmailBulksResponse(BulksBase):
    bulks: List[Bulk]
