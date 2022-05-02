from infobip_channels.sms.models.response.core import ScheduledSMSMessages


class GetScheduledSMSMessagesResponse(ScheduledSMSMessages):
    send_at: str
