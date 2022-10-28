import unittest
from infobip_channels.sms.channel import SMSChannel


class TFATestCase(unittest.TestCase):
    def test_get_tfa_applications(self):
        channel = SMSChannel.from_env()
        response = channel.get_tfa_applications()

        print(f"Response: {response.status_code}: {response.json()}")


if __name__ == '__main__':
    unittest.main()
