from pydantic_factories import ModelFactory

from infobip_channels.web_rtc.models.body.generate_token import GenerateTokenBody
from infobip_channels.web_rtc.models.body.save_application import SaveApplicationBody


class GenerateTokenFactory(ModelFactory):
    __model__ = GenerateTokenBody


class SaveApplicationFactory(ModelFactory):
    __model__ = SaveApplicationBody


def get_webrtc_body_request():
    return {
        "name": "Application Name",
        "description": "Application Description",
        "android": {"fcmServerKey": "test_key"},
        "appToApp": "true",
        "appToConversations": "false",
        "appToPhone": "false",
    }


def get_webrtc_body_generate_token():
    return {
        "identity": "Alice",
        "applicationId": "2277594c-76ea-4b8e-a299-e2b6db41b9dc",
        "displayName": "Alice in Wonderland",
        "capabilities": {"recording": "ALWAYS"},
        "timeToLive": 43200,
    }


def get_webrtc_generate_token_response():
    return {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVk",
        "expirationTime": "2020-01-17T19:50:38.488589Z",
    }


def get_webrtc_application_response():
    return {
        "id": "894c822b-d7ba-439c-a761-141f591cace7",
        "name": "Application Name",
        "description": "Application Description",
        "ios": {
            "apnsCertificateFileName": "IOS_APNS_certificate.p",
            "apnsCertificatePassword": "IOS_APNS_certificate_password",
        },
        "android": {"fcmServerKey": "test_key"},
        "appToApp": "true",
        "appToConversations": "true",
        "appToPhone": "true",
    }


def get_webrtc_request_error_response():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "BAD_REQUEST",
                "text": "Bad request",
                "validationErrors": "Some Validation error",
            }
        }
    }
