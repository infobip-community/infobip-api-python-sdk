from pydantic_factories import ModelFactory

from infobip_channels.sms.models.body.send_binary_message import BinarySMSMessageBody
from infobip_channels.sms.models.body.send_message import SMSMessageBody
from infobip_channels.sms.models.response.send_message import SendSMSResponse


class GenerateSMSMessageBodyFactory(ModelFactory):
    __model__ = SMSMessageBody


class GenerateSMSMessageBodyFactoryIntegration(ModelFactory):
    __model__ = SMSMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return SMSMessageBody(**get_send_sms_message_body())


class GenerateBinarySMSMessageBodyFactory(ModelFactory):
    __model__ = BinarySMSMessageBody


class GenerateBinarySMSMessageBodyFactoryIntegration(ModelFactory):
    __model__ = BinarySMSMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return BinarySMSMessageBody(**get_send_binary_sms_message_body())


class GenerateSendSMSMessageResponse(ModelFactory):
    __model__ = SendSMSResponse


def get_send_sms_message_body():
    return {
        "messages": [
            {
                "destinations": [{"to": "41793026727"}],
                "from": "InfoSMS",
                "text": "This is a sample message",
            }
        ]
    }


def get_send_binary_sms_message_body():
    return {
        "bulkId": "BULK-ID-123-xyz",
        "messages": [
            {
                "binary": {
                    "dataCoding": 0,
                    "esmClass": 0,
                    "hex": "54 65 73 74 20 6d 65 73 73 61 67 65 2e",
                },
                "callbackData": "DLR callback data",
                "destinations": [
                    {"messageId": "MESSAGE-ID-123-xyz", "to": "41793026727"},
                    {"to": "41793026834"},
                ],
                "from": "InfoSMS",
                "intermediateReport": True,
                "notifyContentType": "application/json",
                "notifyUrl": "https://www.example.com/sms/advanced",
                "validityPeriod": 720,
            },
        ],
    }


def get_sms_request_response():
    return {
        "bulkId": "2034072219640523072",
        "messages": [
            {
                "messageId": "41793026727",
                "status": {
                    "description": "Message sent to next instance",
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 26,
                    "name": "MESSAGE_ACCEPTED",
                },
                "to": "2250be2d4219-3af1-78856-aabe-1362af1edfd2",
            }
        ],
    }


def get_sms_request_error_response():
    return {
        "bulkId": "",
        "messages": [],
        "errorMessage": "Head part is mandatory. Check API documentation",
    }