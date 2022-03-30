import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.web_rtc.models.body.save_application import SaveApplicationBody
from tests.conftest import get_random_string
from tests.webrtc.conftest import SaveApplicationFactory


@pytest.mark.parametrize("name", [None, "", {}])
def test_when_name_is_invalid__validation_error_is_raised(name):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{
                "name": name,
            }
        )


@pytest.mark.parametrize("description", [get_random_string(161)])
def test_when_description_is_invalid__validation_error_is_raised(description):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{"name": "Application name", "description": description}
        )


@pytest.mark.parametrize("apns_certificate_file_name", [None, "", {}])
def test_when_apns_certificate_file_name_is_invalid__validation_error_is_raised(
    apns_certificate_file_name,
):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{
                "name": "Application name",
                "description": "Application Description",
                "ios": {
                    "apnsCertificateFileName": apns_certificate_file_name,
                    "apnsCertificateFileContent": "APNS certificate content",
                },
            }
        )


@pytest.mark.parametrize("apns_certificate_file_content", [None, "", {}])
def test_when_apns_certificate_file_content_is_invalid__validation_error_is_raised(
    apns_certificate_file_content,
):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{
                "name": "Application name",
                "description": "Application Description",
                "ios": {
                    "apnsCertificateFileName": "IOS_APNS_certificate.p",
                    "apnsCertificateFileContent": apns_certificate_file_content,
                },
            }
        )


@pytest.mark.parametrize("fcm_server_key", [None, "", {}])
def test_when_fcm_server_key_is_invalid__validation_error_is_raised(fcm_server_key):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{
                "name": "Application name",
                "description": "Application Description",
                "android": {"fcmServerKey": fcm_server_key},
            }
        )


@pytest.mark.parametrize("app_to_app", ["", {}, "test"])
def test_when_app_to_app_is_invalid__validation_error_is_raised(app_to_app):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{"name": "Application name", "appToApp": app_to_app}
        )


@pytest.mark.parametrize("app_to_conversations", ["", {}, "test"])
def test_when_app_to_conversations_is_invalid__validation_error_is_raised(
    app_to_conversations,
):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{"name": "Application name", "appToConversations": app_to_conversations}
        )


@pytest.mark.parametrize("app_to_phone", ["", {}, "test"])
def test_when_app_to_phone_is_invalid__validation_error_is_raised(app_to_phone):
    with pytest.raises(ValidationError):
        SaveApplicationFactory.build(
            **{"name": "Application name", "appToPhone": app_to_phone}
        )


def test_when_input_data_is_valid_android__validation_error_is_not_raised():
    try:
        SaveApplicationBody(
            **{
                "name": "Application Name",
                "description": "Application Description",
                "android": {
                    "fcmServerKey": "AAAAtm7JlCY:APA91bEe02qZQbfcTtmnPOHlQ431tDPm2GoCjciVmoD3"
                },
                "appToApp": "true",
                "appToConversations": "false",
                "appToPhone": "false",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


def test_when_input_data_is_valid_ios__validation_error_is_not_raised():
    try:
        SaveApplicationBody(
            **{
                "name": "Application Name",
                "description": "Application Description",
                "ios": {
                    "apnsCertificateFileName": "IOS_APNS_certificate.p",
                    "apnsCertificateFileContent": "APNS certificate content",
                },
                "appToApp": "true",
                "appToConversations": "false",
                "appToPhone": "false",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
