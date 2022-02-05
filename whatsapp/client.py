from typing import Any, Dict, Union

import requests
from pydantic.error_wrappers import ValidationError

from whatsapp.models.core import (
    Authentication,
    RequestHeaders,
    WhatsAppResponse,
    WhatsAppResponseError,
    WhatsAppResponseOK,
)
from whatsapp.models.document_message import DocumentMessageBody
from whatsapp.models.text_message import TextMessageBody


class HttpClient:
    """Default HTTP client used by the WhatsAppChannel for making HTTP requests."""

    def __init__(self, auth: Authentication):
        self.auth = auth
        self.headers = RequestHeaders(authorization=self.auth.api_key)

    def post(
        self, endpoint: str, body: Dict
    ) -> Union[WhatsAppResponse, requests.Response]:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        response = requests.post(
            url=url, json=body, headers=self.headers.dict(by_alias=True)
        )

        return self._construct_response(response)

    def _construct_response(
        self, response: requests.Response
    ) -> Union[WhatsAppResponse, requests.Response]:
        response_body = {
            "status_code": response.status_code,
            "raw_response": response,
            **response.json(),
        }

        try:
            response_class = self._get_response_class(response)
            return response_class(**response_body)

        except ValidationError:
            return response

    @staticmethod
    def _get_response_class(response):
        if 200 <= response.status_code < 300:
            return WhatsAppResponseOK

        elif 400 <= response.status_code < 500:
            return WhatsAppResponseError

        raise ValidationError


class WhatsAppChannel:
    """Client used for interaction with the Infobip's WhatsApp API."""

    SEND_MESSAGE_URL_TEMPLATE = "/whatsapp/1/message/"

    def __init__(self, client: Union[HttpClient, Any]) -> None:
        self._client = client

    @classmethod
    def from_auth_params(cls, auth_params: Dict[str, str]) -> "WhatsAppChannel":
        """Create an Authentication instance from the provided dictionary and
        use it to instantiate WhatsAppChannel. Dictionary has to contain "base_url" and
        "api_key" to be able to authenticate with the Infobip's API.
        WhatsAppChannel instantiated this way will use the default HttpClient class for
        making HTTP requests.

        :param auth_params: Dictionary containing "base_url" and "api_key"
        :return: Instance of this class
        """
        client = HttpClient(Authentication(**auth_params))
        return cls(client)

    @classmethod
    def from_auth_instance(cls, auth_instance: Authentication) -> "WhatsAppChannel":
        """Instantiate WhatsAppChannel with the provided auth object.
        WhatsAppChannel instantiated this way will use the default HttpClient class for
        making HTTP requests.

        :param auth_instance: Authentication class instance
        :return: Instance of this class
        """
        client = HttpClient(auth_instance)
        return cls(client)

    @classmethod
    def from_provided_client(cls, client: Any) -> "WhatsAppChannel":
        """Instantiate WhatsAppChannel with the provided client object.
        WhatsAppChannel instantiated this way will use the provided client for making
        HTTP requests. This client can implement its own retry mechanisms, timeouts,
        etc., but it has to implement all the methods used in the default HttpClient
        class.

        :param client: Client used for making HTTP requests
        :return: Instance of this class
        """
        return cls(client)

    def send_text_message(
        self, message: Union[TextMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send a text message to a single recipient. Text messages can only be
        successfully delivered, if the recipient has contacted the business within the
        last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        if not isinstance(message, TextMessageBody):
            message = TextMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "text", message.dict(by_alias=True)
        )

    def send_document_message(
        self, message: Union[DocumentMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send a document to a single recipient. Document messages can only be
        successfully delivered, if the recipient has contacted the business within the
        last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        if not isinstance(message, DocumentMessageBody):
            message = DocumentMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "document", message.dict(by_alias=True)
        )
