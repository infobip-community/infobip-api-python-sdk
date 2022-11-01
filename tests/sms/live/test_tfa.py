import unittest
from infobip_channels.sms.channel import SMSChannel


class TFATestCase(unittest.TestCase):
    def test_get_tfa_applications(self):
        channel = SMSChannel.from_dotenv()
        response = channel.get_tfa_applications()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.raw_response)


if __name__ == '__main__':
    unittest.main()
