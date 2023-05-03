from collections.abc import Awaitable

from httpx import AsyncClient, Response

from models import SendSMSRequestBody
from models.sms_preview_request import PreviewSMSRequestBody


class SMSClient:
    PATH_PREVIEW_SMS = "/sms/1/preview"
    PATH_SEND_SMS = "/sms/2/text/advanced"

    def __init__(self, client: AsyncClient):
        self.client = client
        self.client.headers.update({"content-type": "application/json"})

    def preview_message(
        self, request_body: PreviewSMSRequestBody
    ) -> Awaitable[Response]:
        """Check how different message configurations will affect your message text, number of characters and message
        parts.

        :param request_body: Request body for previewing an SMS message
        """

        return self.client.post(
            self.PATH_PREVIEW_SMS,
            json=request_body.to_dict(),
        )

    def send(
        self,
        request_body: SendSMSRequestBody,
    ) -> Awaitable[Response]:
        """Send SMS message

        :param request_body: Request body for sending an SMS message
        """

        return self.client.post(
            self.PATH_SEND_SMS,
            json=request_body.to_dict(),
        )
