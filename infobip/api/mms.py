from collections.abc import Awaitable

from httpx import Response, AsyncClient

from infobip.models.mms_get_inbound_messages_query_parameters import GetInboundMessagesQueryParameters


class MMSClient:
    PATH_GET_INBOUND_MESSAGES = "/mms/1/inbox/reports"

    def __init__(self, client: AsyncClient):
        self.client = client

    def get_inbound_messages(
            self,
            query_parameters: GetInboundMessagesQueryParameters,
    ) -> Awaitable[Response]:
        """Get inbound messages

        :param query_parameters: Query parameters for getting inbound messages
        """

        return self.client.get(
            self.PATH_GET_INBOUND_MESSAGES,
            params=query_parameters.to_dict(),
        )
