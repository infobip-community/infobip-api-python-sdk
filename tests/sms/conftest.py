from pydantic_factories import ModelFactory

from infobip_channels.sms.models.body.create_tfa_application import (
    CreateTFAApplicationBody,
)
from infobip_channels.sms.models.body.create_tfa_message_template import (
    CreateTFAMessageTemplateBody,
)
from infobip_channels.sms.models.body.preview_message import PreviewSMSMessage
from infobip_channels.sms.models.body.reschedule_sms_messages import (
    RescheduleSMSMessagesMessageBody,
)
from infobip_channels.sms.models.body.resend_pin_over_sms import ResendPINOverSMSBody
from infobip_channels.sms.models.body.resend_pin_over_voice import (
    ResendPINOverVoiceBody,
)
from infobip_channels.sms.models.body.send_binary_message import BinarySMSMessageBody
from infobip_channels.sms.models.body.send_message import SMSMessageBody
from infobip_channels.sms.models.body.send_pin_over_sms import SendPINOverSMSBody
from infobip_channels.sms.models.body.send_pin_over_voice import SendPINOverVoiceBody
from infobip_channels.sms.models.body.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesMessageBody,
)
from infobip_channels.sms.models.body.update_tfa_application import (
    UpdateTFAApplicationBody,
)
from infobip_channels.sms.models.body.update_tfa_message_template import (
    UpdateTFAMessageTemplateBody,
)
from infobip_channels.sms.models.body.verify_phone_number import VerifyPhoneNumberBody
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


class GeneratePreviewSMSMessageBodyFactory(ModelFactory):
    __model__ = PreviewSMSMessage


class GenerateRescheduleSMSMessagesFactory(ModelFactory):
    __model__ = RescheduleSMSMessagesMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return RescheduleSMSMessagesMessageBody(
            **get_reschedule_sms_messages_message_body()
        )


class GenerateUpdateScheduledSMSMessagesStatusFactory(ModelFactory):
    __model__ = UpdateScheduledSMSMessagesMessageBody


class GenerateCreateTFAApplicationBodyFactoryIntegration(ModelFactory):
    __model__ = CreateTFAApplicationBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return CreateTFAApplicationBody(**get_create_tfa_application_body())


class GenerateUpdateTFAApplicationBodyFactoryIntegration(ModelFactory):
    __model__ = UpdateTFAApplicationBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return UpdateTFAApplicationBody(**get_update_tfa_application_body())


class GenerateCreateTFAMessageTemplateBodyFactoryIntegration(ModelFactory):
    __model__ = CreateTFAMessageTemplateBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return CreateTFAMessageTemplateBody(**get_create_tfa_message_template_body())


class GenerateUpdateTFAMessageTemplateBodyFactoryIntegration(ModelFactory):
    __model__ = UpdateTFAMessageTemplateBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return UpdateTFAMessageTemplateBody(**get_update_tfa_message_template_body())


class GenerateResendPINOverSMSBodyFactoryIntegration(ModelFactory):
    __model__ = ResendPINOverSMSBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return ResendPINOverSMSBody(**get_resend_pin_over_sms_response())


class GenerateResendPINOverVoiceBodyFactoryIntegration(ModelFactory):
    __model__ = ResendPINOverVoiceBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return ResendPINOverVoiceBody(**get_resend_pin_over_voice_response())


class GenerateSendPINOverSMSBodyFactoryIntegration(ModelFactory):
    __model__ = SendPINOverSMSBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return SendPINOverSMSBody(**get_send_pin_over_sms_body())


class GenerateSendPINOverVoiceBodyFactoryIntegration(ModelFactory):
    __model__ = SendPINOverVoiceBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return SendPINOverVoiceBody(**get_send_pin_over_voice_body())


class GenerateVerifyPhoneNumberBodyFactoryIntegration(ModelFactory):
    __model__ = VerifyPhoneNumberBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return VerifyPhoneNumberBody(**get_verify_phone_number_body())


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


def get_reschedule_sms_messages_query_parameters():
    return {"bulkId": "35122736310703571952"}


def get_reschedule_sms_messages_message_body():
    return {"sendAt": "2022-07-20T16:00:00.000+0000"}


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


def get_scheduled_sms_messages_response():
    return {"bulkId": "BulkId-xyz-123", "sendAt": "2022-07-20T16:00:00.000+0000"}


def get_update_scheduled_sms_messages_status_response():
    return {"bulkId": "BulkId-xyz-123", "status": "PAUSED"}


def get_scheduled_sms_messages_status_response():
    return {"bulkId": "BulkId-xyz-123", "status": "PENDING"}


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


def get_inbound_sms_messages_response():
    return {
        "results": [
            {
                "messageId": "817790313235066447",
                "from": "385916242493",
                "to": "385921004026",
                "text": "QUIZ Correct answer is Paris",
                "cleanText": "Correct answer is Paris",
                "keyword": "QUIZ",
                "receivedAt": "2019-11-09T16:00:00.000+0000",
                "smsCount": 1,
                "price": {"pricePerMessage": 0.1, "currency": "EUR"},
                "callbackData": "callbackData",
            }
        ],
        "messageCount": 1,
        "pendingMessageCount": 0,
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


def get_inbound_sms_messages_query_parameters():
    return {
        "limit": 2,
    }


def get_scheduled_sms_messages():
    return {
        "bulk_id": "BulkId-xyz-123",
    }


def get_tfa_application():
    return {
        "applicationId": "1234567890",
        "name": "Application name",
        "configuration": {
            "pinAttempts": 5,
            "allowMultiplePinVerifications": True,
            "pinTimeToLive": "10m",
            "verifyPinLimit": "2/4s",
            "sendPinPerApplicationLimit": "5000/12h",
            "sendPinPerPhoneNumberLimit": "2/1d",
        },
        "enabled": True,
    }


def get_create_tfa_application_body():
    return get_tfa_application()


def get_update_tfa_application_body():
    return get_tfa_application()


def get_create_tfa_application_response():
    return get_tfa_application()


def get_tfa_request_error_response():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "BAD_REQUEST",
                "text": "Bad request",
            }
        }
    }


def get_update_tfa_application_response():
    return get_tfa_application()


def get_tfa_application_response():
    return get_tfa_application()


def get_tfa_applications_response():
    return {"applications": [get_tfa_application()]}


def get_create_tfa_message_template_response():
    return get_tfa_message_template()


def get_update_tfa_message_template_response():
    return {"template": get_tfa_message_template()}


def get_tfa_message_template():
    return {
        "pinPlaceholder": "{{pin}}",
        "messageText": "Your pin is {{pin}}",
        "pinLength": 4,
        "pinType": "ALPHANUMERIC",
        "language": "en",
        "senderId": "Infobip 2FA",
        "repeatDTMF": "1#",
        "speechRate": 1,
    }


def get_create_tfa_message_template_body():
    return get_tfa_message_template()


def get_update_tfa_message_template_body():
    return get_tfa_message_template()


def get_send_pin_body():
    return {
        "applicationId": "1234567",
        "messageId": "7654321",
        "from": "Sender 1",
        "to": "41793026727",
        "placeholders": {"firstName": "John"},
    }


def get_send_pin_over_sms_body():
    return get_send_pin_body()


def get_send_pin_over_voice_body():
    return get_send_pin_body()


def get_send_pin_over_sms_status():
    return {
        "pinId": "9C817C6F8AF3D48F9FE553282AFA2B67",
        "to": "41793026727",
        "ncStatus": "NC_DESTINATION_REACHABLE",
        "smsStatus": "MESSAGE_SENT",
    }


def get_send_pin_over_voice_status():
    return {
        "pinId": "9C817C6F8AF3D48F9FE553282AFA2B67",
        "to": "41793026727",
        "callStatus": "PENDING_ACCEPTED",
    }


def get_resend_pin_over_body():
    return {"placeholders": {"firstName": "John"}}


def get_resend_pin_over_sms_body():
    return get_resend_pin_over_body()


def get_resend_pin_over_voice_body():
    return get_resend_pin_over_body()


def get_send_pin_over_sms_response():
    return get_send_pin_over_sms_status()


def get_send_pin_over_voice_response():
    return get_send_pin_over_voice_status()


def get_resend_pin_over_sms_response():
    return get_send_pin_over_sms_status()


def get_resend_pin_over_voice_response():
    return get_send_pin_over_voice_status()


def get_verify_phone_number_body():
    return {"pin": "1598"}


def get_verify_phone_number_response():
    return {
        "pinId": "9C817C6F8AF3D48F9FE553282AFA2B67",
        "msisdn": "41793026727",
        "verified": True,
        "attemptsRemaining": 0,
    }


def get_get_tfa_verification_status_response():
    return {
        "verifications": [
            {
                "msisdn": "41793026727",
                "verified": True,
                "verifiedAt": 1418364366,
                "sentAt": 1418364246,
            },
            {
                "msisdn": "41793026746",
                "verified": False,
                "verifiedAt": 1418364226,
                "sentAt": 1418333246,
            },
        ]
    }


def get_get_tfa_message_templates_response():
    return {"results": [get_tfa_message_template()]}
