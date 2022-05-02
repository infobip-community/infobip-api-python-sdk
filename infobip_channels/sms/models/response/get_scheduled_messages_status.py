from infobip_channels.sms.models.response.core import ScheduledSMSMessages


class GetScheduledSMSMessagesStatusResponse(ScheduledSMSMessages):
    status: str
