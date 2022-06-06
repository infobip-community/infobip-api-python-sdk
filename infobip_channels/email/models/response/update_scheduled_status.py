from infobip_channels.core.models import ResponseBase


class UpdateScheduledStatusResponse(ResponseBase):
    bulk_id: str
    status: str
