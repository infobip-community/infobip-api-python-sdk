from pydantic_factories import ModelFactory

from infobip_channels.web_rtc.models.body.generate_token import GenerateTokenBody
from infobip_channels.web_rtc.models.body.save_application import SaveApplicationBody
from infobip_channels.web_rtc.models.body.update_application import (
    UpdateApplicationBody,
)


class GenerateTokenFactory(ModelFactory):
    __model__ = GenerateTokenBody


class SaveApplicationFactory(ModelFactory):
    __model__ = SaveApplicationBody


class UpdateApplicationFactory(ModelFactory):
    __model__ = UpdateApplicationBody


def get_expected_path_parameters():
    return {"id": "894c822b-d7ba-439c-a761-141f591cace7"}


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
        "appToApp": True,
        "appToConversations": True,
        "appToPhone": True,
    }


def get_webrtc_application_request():
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
                "validationErrors": {
                    "request.message.content.media.file.url": [
                        "is not a valid url",
                    ]
                },
            }
        }
    }


def get_webrtc_get_applications_response():
    return [
        {
            "id": "894c822b-d7ba-439c-a761-141f591cace7",
            "name": "Application Name 1",
            "description": "Application Description",
            "ios": {
                "apnsCertificateFileName": "IOS_APNS_certificate.p",
                "apnsCertificatePassword": "IOS_APNS_certificate_password",
            },
            "appToApp": True,
            "appToConversations": False,
            "appToPhone": True,
        },
        {
            "id": "988c411a-a2db-227a-c563-245a159dcbe2",
            "name": "Application Name 2",
            "description": "Application Description",
            "android": {"fcmServerKey": "AAAAtm7JlCY:APA91bEe02qZQbfcTtmnPOHlQ431tDPm"},
            "appToApp": True,
            "appToConversations": False,
            "appToPhone": True,
        },
        {
            "id": "454d142b-a1ad-239a-d231-227fa335aadc3",
            "name": "Application Name 3",
            "description": "Application Description",
            "appToApp": True,
            "appToConversations": False,
            "appToPhone": True,
        },
    ]
