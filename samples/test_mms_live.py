import unittest

from infobip.client import APIClient
from infobip.models.mms_get_inbound_messages_query_parameters import (
    GetInboundMessagesQueryParameters,
)
from infobip.models.mms_inbound_report_response import GetInboundMessagesResponseBody


class MMSTestCase(unittest.IsolatedAsyncioTestCase):
    client = APIClient()

    async def test_get_inbound_messages(self):
        # Create query parameters object and validate its contents.
        params = GetInboundMessagesQueryParameters(
            limit=10,
        )

        # Call the endpoint and await returned Coroutine
        response = await self.client.MMS.get_inbound_messages(params)

        # Parse and validate response if needed.
        response_body = GetInboundMessagesResponseBody.from_json(response.text)

        # Do something with the response.
        # print(response)
        # print(response_body.results)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_body.results)
