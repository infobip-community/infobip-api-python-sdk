from typing import Awaitable

from httpx import AsyncClient, Client, Response

from infobip.models.sms_advanced_textual_request import SendSMSRequestBody
from infobip.models.sms_preview_request import PreviewSMSRequestBody

PATH_PREVIEW_SMS = "/sms/1/preview"
PATH_SEND_SMS = "/sms/2/text/advanced"


class SMSClient:
    def __init__(self, client: AsyncClient):
        self.client = client
        self.client.headers.update({"content-type": "application/json"})

    def preview(self, request_body: PreviewSMSRequestBody) -> Awaitable[Response]:
        """Check how different message configurations will affect your message text, number of characters and message
        parts.

        :param request_body: Request body for previewing an SMS message
        """

        return self.client.post(
            PATH_PREVIEW_SMS,
            json=request_body.to_dict(),
        )

    def send(
        self,
        request_body: SendSMSRequestBody,
    ) -> Awaitable[Response]:
        """Send an SMS message. You can send a simple single message to a single destination, up to batch sending of
        personalized messages to the thousands of recipients with a single API request. Language, transliteration,
        scheduling and every advanced feature you can think of is supported.

        :param request_body: Request body for sending an SMS message
        """

        return self.client.post(
            PATH_SEND_SMS,
            json=request_body.to_dict(),
        )


class SyncSMSClient:
    def __init__(self, client: Client):
        self._client = client
        self._client.headers.update({"content-type": "application/json"})

    def preview(self, request_body: PreviewSMSRequestBody) -> Response:
        """Check how different message configurations will affect your message text, number of characters and message
        parts. This is a synchronous version of the method.

        :param request_body: Request body for previewing an SMS message
        """

        return self._client.post(
            PATH_PREVIEW_SMS,
            json=request_body.to_dict(),
        )
