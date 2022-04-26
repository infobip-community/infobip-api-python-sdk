from datetime import date, datetime, timedelta

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.sms.models.query_parameters.sms_send_message import (
    SendSMSMessageQueryParameters,
)


def test_when_username_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": {},
                "password": "Pass123",
                "to": ["41793026727"],
            }
        )


def test_when_password_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": {},
                "to": ["41793026727"],
            }
        )


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "bulkId": {},
            }
        )


def test_when_from_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "from": {},
            }
        )


def test_when_to_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": {},
            }
        )


def test_when_text_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "text": {},
            }
        )


def test_when_flash_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "flash": {},
            }
        )


@pytest.mark.parametrize("transliteration", [{}, "ABC"])
def test_when_transliteration_is_invalid__validation_error_is_raised(transliteration):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "transliteration": transliteration,
            }
        )


def test_when_language_code_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "languageCode": {},
            }
        )


@pytest.mark.parametrize("intermediate_report", [{}, "true"])
def test_when_intermediate_report_is_invalid__validation_error_is_raised(
    intermediate_report,
):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "intermediateReport": intermediate_report,
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "ABC", "www.test.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "notifyUrl": notify_url,
            }
        )


@pytest.mark.parametrize("notify_content_type", [{}, "ABC"])
def test_when_notify_content_type_is_invalid__validation_error_is_raised(
    notify_content_type,
):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "notifyContentType": notify_content_type,
            }
        )


def test_when_callback_data_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "callbackData": {},
            }
        )


@pytest.mark.parametrize("validity_period", [{}, -1, 2881])
def test_when_validity_period_is_invalid__validation_error_is_raised(validity_period):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "validityPeriod": validity_period,
            }
        )


@pytest.mark.parametrize(
    "send_at",
    [{}, "Test", "22-03-2022", date.today(), datetime.now() + timedelta(days=181)],
)
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "sendAt": send_at,
            }
        )


@pytest.mark.parametrize("track", [{}, "ABC"])
def test_when_track_is_invalid__validation_error_is_raised(track):
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "track": track,
            }
        )


def test_when_process_key_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "processKey": {},
            }
        )


def test_when_tracking_type_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "trackingType": {},
            }
        )


def test_when_india_dlt_content_template_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "indiaDltContentTemplateId": {},
            }
        )


def test_when_india_dlt_principal_entity_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "to": ["41793026727"],
                "indiaDltPrincipalEntityId": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        SendSMSMessageQueryParameters(
            **{
                "username": "Test User",
                "password": "Pass123",
                "bulkId": "1478260834465349756",
                "from": "Test message",
                "to": ["41793026727"],
                "text": "Test text",
                "flash": True,
                "transliteration": "TURKISH",
                "languageCode": "TR",
                "intermediateReport": True,
                "notifyUrl": "https://www.example.com",
                "notifyContentType": "application/json",
                "callbackData": "callbackData",
                "validityPeriod": 720,
                "sendAt": datetime.now() + timedelta(days=1),
                "track": "URL",
                "processKey": "processKey",
                "trackingType": "ONE_TIME_PIN",
                "indiaDltContentTemplateId": "indiaDltContentTemplateId",
                "indiaDltPrincipalEntityId": "indiaDltPrincipalEntityId",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
