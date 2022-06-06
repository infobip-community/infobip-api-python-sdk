from infobip_channels.core.models import ResponseBase


class RescheduleMessagesResponse(ResponseBase):
    bulk_id: str
    send_at: str
