from infobip_channels.core.models import MessageBodyBase, MessageStatus


class UpdateScheduledSMSMessagesMessageBody(MessageBodyBase):
    status: MessageStatus
