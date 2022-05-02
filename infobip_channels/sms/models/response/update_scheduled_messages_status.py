from infobip_channels.sms.models.response.core import ScheduledSMSMessages


class UpdateScheduledSMSMessagesStatusResponse(ScheduledSMSMessages):
    status: str
