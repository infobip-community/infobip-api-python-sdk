import unittest

import pytest

from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)


@pytest.mark.skip(reason="credentials needed, server state dependent")
class WhatsAppTestCase(unittest.TestCase):
    def test_get_templates(self):
        channel = WhatsAppChannel.from_dotenv()
        path_parameter = ManageTemplatesPathParameters(sender="447860099299")
        response = channel.get_templates(path_parameter)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.raw_response)
