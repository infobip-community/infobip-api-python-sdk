import unittest
from http import HTTPStatus

import pytest

from infobip_channels.sms.channel import SMSChannel


@pytest.mark.skip(reason="credentials needed, server state dependent")
class TFATestCase(unittest.TestCase):
    channel = SMSChannel.from_dotenv()

    def test_get_tfa_applications(self):
        response = TFATestCase.channel.get_tfa_applications()

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_create_tfa_application(self):
        application = {
            "name": "2fa application test",
            "enabled": "true",
            "configuration": {
                "pinAttempts": 7,
                "allowMultiplePinVerifications": "true",
                "pinTimeToLive": "11m",
                "verifyPinLimit": "2/4s",
                "sendPinPerApplicationLimit": "5000/12h",
                "sendPinPerPhoneNumberLimit": "2/1d"
            }
        }
        response = TFATestCase.channel.create_tfa_application(application)

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertIsNotNone(response)

    def test_get_tfa_application(self):
        response = TFATestCase.channel.get_tfa_application("02CC3CAAFD733136AA15DFAC720A0C42")

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_update_tfa_application(self):
        application = {
            "name": "test-tfa_application-3",
            "enabled": "true",
            "configuration": {
                "pinAttempts": 9,
                "allowMultiplePinVerifications": "true",
                "pinTimeToLive": "11m",
                "verifyPinLimit": "2/4s",
                "sendPinPerApplicationLimit": "5000/12h",
                "sendPinPerPhoneNumberLimit": "2/1d"
            }
        }

        response = TFATestCase.channel.update_tfa_application("02CC3CAAFD733136AA15DFAC720A0C42", application)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_get_tfa_message_templates(self):
        response = TFATestCase.channel.get_tfa_message_templates("02CC3CAAFD733136AA15DFAC720A0C42")

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_create_tfa_message_template(self):
        app_id = "02CC3CAAFD733136AA15DFAC720A0C42"
        request_body = {
            "pinType": "NUMERIC",
            "pinPlaceholder": "{{pin}}",
            "messageText": "Your pin is {{pin}}",
            "pinLength": 4,
            "language": "en",
            "senderId": "Infobip 2FA",
            "repeatDTMF": "1#",
            "speechRate": 1
        }

        response = TFATestCase.channel.create_tfa_message_template(app_id, request_body)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_get_tfa_message_template(self):
        app_id = "02CC3CAAFD733136AA15DFAC720A0C42"
        message_id = "2140E0A55D9E4A46429D65E218091C64"

        response = TFATestCase.channel.get_tfa_message_template(app_id, message_id)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_update_tfa_message_template(self):
        app_id = "02CC3CAAFD733136AA15DFAC720A0C42"
        message_id = "2140E0A55D9E4A46429D65E218091C64"
        request_body = {
            "pinType": "NUMERIC",
            "pinPlaceholder": "{{pin}}",
            "messageText": "The PIN is {{pin}}",
            "pinLength": 6,
            "language": "en",
            "senderId": "Infobip 2FA",
            "repeatDTMF": "2#",
            "speechRate": 1
        }

        response = TFATestCase.channel.update_tfa_message_template(app_id, message_id, request_body)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_send_pin_over_sms(self):
        query_parameters = {"ncNeeded": "false"}
        request_body = {
            "applicationId": "43D78365E3257420D78752A62845A8CB",
            "messageId": "9AD26BD115AB45657A0FEACACCC918BE",
            "from": "InfoSMS",
            "to": "555555555555",
            "placeholders": {
                "name": "John",
            }
        }

        response = TFATestCase.channel.send_pin_over_sms(query_parameters, request_body)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_resend_pin_over_sms(self):
        placeholders = {
            "placeholders": {"name": "John"}
        }

        response = TFATestCase.channel.resend_pin_over_sms("B147E121929711EC4163A6FB5B44CD59", placeholders)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_send_pin_over_voice(self):
        query_parameters = {"ncNeeded": "false"}
        request_body = {
            "applicationId": "02CC3CAAFD733136AA15DFAC720A0C42",
            "messageId": "2140E0A55D9E4A46429D65E218091C64",
            "from": "InfoSMS",
            "to": "555555555555",
        }

        response = TFATestCase.channel.send_pin_over_voice(query_parameters, request_body)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_resend_pin_over_voice(self):
        placeholders = {
            "placeholders": {"name": "John"}
        }

        response = TFATestCase.channel.resend_pin_over_voice("B147E121929711EC4163A6FB5B44CD59", placeholders)

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())
