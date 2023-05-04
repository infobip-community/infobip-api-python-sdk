# Test for validations

import unittest

from infobip.client import InfobipAPIClient
from http_server_mock import HttpServerMock


class TestSMS(unittest.IsolatedAsyncioTestCase):
    client = InfobipAPIClient()

    async def test_preview_message(self):
        expected_response = {
            "bulkId": "2034072219640523072",
            "messages": [
                {
                    "messageId": "2250be2d4219-3af1-78856-aabe-1362af1edfd2",
                    "status": {
                        "description": "Message sent to next instance",
                        "groupId": 1,
                        "groupName": "PENDING",
                        "id": 26,
                        "name": "MESSAGE_ACCEPTED"
                    },
                    "to": "41793026727"
                }
            ]
        }

        # Start the mock server
        mock_server = HttpServerMock("localhost", 5000)

        with mock_server.run():
            client = InfobipAPIClient(base_url="http://localhost:5000")

            # Call the endpoint and await returned Coroutine
            response = await self.client.SMS.preview_message("test")

            # Do something with the response.
            print(response)

            self.assertEquals(response.status_code, 200)
            self.assertEquals(response.json(), expected_response)
