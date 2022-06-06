from infobip_channels.core.models import MessageBodyBase, MessageStatus


class UpdateScheduledStatusMessageBody(MessageBodyBase):
    status: MessageStatus
