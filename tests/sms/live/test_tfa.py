import os
import unittest
from http import HTTPStatus

from infobip_channels.sms.channel import SMSChannel


class TFATestCase(unittest.TestCase):
    def test_get_tfa_applications(self):
        channel = SMSChannel.from_dotenv()
        response = channel.get_tfa_applications()

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.json())

    def test_create_tfa_application(self):
        channel = SMSChannel.from_dotenv()
        response = channel.create_tfa_application({"name": "test-tfa-application"})

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
