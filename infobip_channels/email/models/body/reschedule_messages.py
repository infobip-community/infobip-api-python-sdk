from infobip_channels.core.models import MessageBodyBase


class RescheduleMessagesMessageBody(MessageBodyBase):
    send_at: str
