import unittest

from infobip.client import APIClient
from infobip.models.sms_advanced_textual_request import SendSMSRequestBody
from infobip.models.sms_destination import Destination
from infobip.models.sms_preview_request import PreviewSMSRequestBody
from infobip.models.sms_preview_response import PreviewSMSResponseBody
from infobip.models.sms_response import SendSMSResponseBody
from infobip.models.sms_textual_message import Message
from infobip.sync_client import SyncAPIClient


class SMSTestCase(unittest.IsolatedAsyncioTestCase):
    client = APIClient()

    async def test_preview_message(self):
        # Create a request body object and validate its contents.
        request_body = PreviewSMSRequestBody(
            text="Let's see how many characters remain unused in this message."
        )

        # Call the endpoint and await returned Coroutine
        response = await self.client.SMS.preview(request_body)

        # Parse and validate response if needed.
        response_body = PreviewSMSResponseBody.from_json(response.text)

        # Do something with the response.
        # print(response)
        # print(response_body.previews)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_body.previews)

    async def test_send_message(self):
        # Create a request body object and validate its contents.
        request_body = SendSMSRequestBody(
            messages=[
                Message(
                    destinations=[
                        Destination(
                            to="555555555555",
                        ),
                    ],
                    text="Hello from Infobip Python SDK!",
                )
            ]
        )

        # Call the endpoint and await returned Coroutine
        response = await self.client.SMS.send(request_body)

        # (Optional) Parse and validate response if needed.
        response_body = SendSMSResponseBody.from_json(response.text)

        # Do something with the response.
        # print(response)
        # print(response_body)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_body.messages)


class SyncSMSTestCase(unittest.TestCase):
    client = SyncAPIClient()

    def test_preview_message(self):
        # Create a request body object and validate its contents.
        request_body = PreviewSMSRequestBody(
            text="Let's see how many characters remain unused in this message."
        )

        # Call the endpoint and await returned Coroutine
        response = self.client.SMS.preview(request_body)

        # Parse and validate response if needed.
        response_body = PreviewSMSResponseBody.from_json(response.text)

        # Do something with the response.
        # print(response)
        # print(response_body.previews)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_body.previews)
