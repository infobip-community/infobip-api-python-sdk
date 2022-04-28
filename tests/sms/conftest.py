from pydantic_factories import ModelFactory

from infobip_channels.sms.models.body.preview_message import PreviewSMSMessage
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


class GeneratePreviewSMSMessageBodyFactory(ModelFactory):
    __model__ = PreviewSMSMessage


def get_preview_send_sms_message_body():
    return {
        "text": "Ως Μεγαρικό ψήφισμα είναι γνωστή η απόφαση της Εκκλησίας του δήμου "
        "των Αθηναίων (πιθανόν γύρω στο 433/2 π.Χ.) να επιβάλει αυστηρό και "
        "καθολικό εμπάργκο στα",
        "transliteration": "GREEK",
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
        "requestError": {
            "serviceException": {
                "messageId": "BAD_REQUEST",
                "text": "Bad request",
                "validationErrors": {
                    "content.text": [
                        "size must be between 1 and 4096",
                        "must not be blank",
                    ]
                },
            }
        }
    }


def get_preview_send_sms_response():
    return {
        "originalText": "Let's see how many characters will remain unused in this "
        "message.",
        "previews": [
            {
                "textPreview": "ΩΣ MEΓAPIKO ΨHΦIΣMA EINAI ΓNΩΣTH H AΠOΦAΣH THΣ "
                "EKKΛHΣIAΣ TOY ΔHMOY TΩN AΘHNAIΩN (ΠIΘANON ΓYPΩ ΣTO "
                "433/2 Π.X.) NA EΠIBAΛEI AYΣTHPO KAI KAΘOΛIKO EMΠAPΓKO "
                "ΣTA",
                "messageCount": 1,
                "charactersRemaining": 5,
                "configuration": {"transliteration": "GREEK"},
            }
        ],
    }


def get_outbound_sms_delivery_reports_response():
    return {
        "results": [
            {
                "bulkId": "BULK-ID-123-xyz",
                "messageId": "MESSAGE-ID-123-xyz",
                "to": "41793026727",
                "sentAt": "2019-11-09T16:00:00.000+0000",
                "doneAt": "2019-11-09T16:00:00.000+0000",
                "smsCount": 1,
                "price": {"pricePerMessage": 0.01, "currency": "EUR"},
                "status": {
                    "groupId": 3,
                    "groupName": "DELIVERED",
                    "id": 5,
                    "name": "DELIVERED_TO_HANDSET",
                    "description": "Message delivered to handset",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "Ok",
                    "id": 0,
                    "name": "NO_ERROR",
                    "description": "No Error",
                    "permanent": False,
                },
            },
        ]
    }


def get_outbound_sms_message_logs_response():
    return {
        "results": [
            {
                "bulkId": "BULK-ID-123-xyz",
                "messageId": "MESSAGE-ID-123-xyz",
                "to": "41793026727",
                "sentAt": "2019-11-09T16:00:00.000+0000",
                "doneAt": "2019-11-09T16:00:00.000+0000",
                "smsCount": 1,
                "mccMnc": "22801",
                "price": {"pricePerMessage": 0.01, "currency": "EUR"},
                "status": {
                    "groupId": 3,
                    "groupName": "DELIVERED",
                    "id": 5,
                    "name": "DELIVERED_TO_HANDSET",
                    "description": "Message delivered to handset",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "Ok",
                    "id": 0,
                    "name": "NO_ERROR",
                    "description": "No Error",
                    "permanent": False,
                },
            },
            {
                "bulkId": "BULK-ID-123-xyz",
                "messageId": "MESSAGE-ID-ijkl-45",
                "to": "41793026834",
                "sentAt": "2019-11-09T17:00:00.000+0000",
                "doneAt": "2019-11-09T17:00:00.000+0000",
                "smsCount": 1,
                "mccMnc": "22801",
                "price": {"pricePerMessage": 0.01, "currency": "EUR"},
                "status": {
                    "groupId": 3,
                    "groupName": "DELIVERED",
                    "id": 5,
                    "name": "DELIVERED_TO_HANDSET",
                    "description": "Message delivered to handset",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "Ok",
                    "id": 0,
                    "name": "NO_ERROR",
                    "description": "No Error",
                    "permanent": False,
                },
            },
        ]
    }


def get_sms_send_message_over_query_parameters():
    return {
        "username": "TestUser",
        "password": "Pass123",
        "to": ["41793026727"],
    }


def get_outbound_sms_delivery_reports_query_parameters():
    return {
        "bulkId": "BULK-ID-123-xyz",
        "messageId": "MESSAGE-ID-123-xyz",
        "limit": 1,
    }


def get_outbound_sms_message_logs_query_parameters():
    return {
        "from": "41793026999",
        "to": "41793026727",
        "bulkId": ["BULK-ID-123-xyz"],
    }
