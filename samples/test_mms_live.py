import unittest

from client import InfobipAPIClient
from models import MMSInboundReportResponse
from models.mms_get_inbound_messages_query_parameters import GetInboundMessagesQueryParameters


class MMSTestCase(unittest.IsolatedAsyncioTestCase):
    client = InfobipAPIClient()

    async def test_preview_message(self):
        # Create query parameters object and validate its contents.
        params = GetInboundMessagesQueryParameters(
            limit=10,
        )

        # Call the endpoint and await returned Coroutine
        response = await self.client.MMS.get_inbound_messages(params)

        # Parse and validate response if needed.
        response_body = MMSInboundReportResponse.from_json(response.text)

        # Do something with the response.
        print(response)
        print(response_body.results)

        self.assertEqual(response.status_code, 200)
