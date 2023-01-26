import unittest
from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)


class WhatsAppTestCase(unittest.TestCase):
    def test_get_tfa_applications(self):
        channel = WhatsAppChannel.from_dotenv()
        path_parameter = ManageTemplatesPathParameters(sender="447860099299")
        response = channel.get_templates(path_parameter)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.raw_response)


if __name__ == "__main__":
    unittest.main()
