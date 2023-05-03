import unittest

from client import InfobipAPIClient
from models import SendSMSRequestBody, Message, Destination
from models.sms_preview_request import PreviewSMSRequestBody
from models.sms_preview_response import PreviewSMSResponseBody


class SMSTestCase(unittest.IsolatedAsyncioTestCase):
    client = InfobipAPIClient()

    async def test_preview_message(self):
        # Create a request body object and validate its contents.
        request_body = PreviewSMSRequestBody(
            text="Let's see how many characters remain unused in this message."
        )

        # Call the endpoint and await returned Coroutine
        response = await self.client.SMS.preview_message(request_body)

        # Parse and validate response if needed.
        response_body = PreviewSMSResponseBody.from_json(response.text)

        # Do something with the response.
        print(response)
        print(response_body.previews)

        self.assertEqual(response.status_code, 200)

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
        response_body = PreviewSMSResponseBody.from_json(response.text)

        # Do something with the response.
        print(response)

        self.assertEqual(response.status_code, 200)
