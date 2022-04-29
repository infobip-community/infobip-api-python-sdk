from infobip_channels.sms.models.response.core import ScheduledSMSMessages


class RescheduleSMSMessagesResponse(ScheduledSMSMessages):
    send_at: str
