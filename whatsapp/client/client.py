from typing import Any, Dict, Optional, Union

import requests
from core.models import Authentication

from whatsapp.core.models import RequestHeaders, Response
from whatsapp.core.utils import construct_response_model
from whatsapp.text_message.models import TextMessageBody


class HttpClient:
    """Default HTTP client used by the WhatsappClient for making HTTP requests."""

    def __init__(self, auth: Authentication):
        self.auth = auth
        self.headers = RequestHeaders(authorization=self.auth.api_key)

    def post(self, endpoint: str, body: Dict) -> Response:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :return: Response instance
        """
        url = self.auth.base_url + endpoint
        response = requests.post(
            url=url, json=body, headers=self.headers.dict(by_alias=True)
        )

        return construct_response_model(response)


class WhatsappClient:
    """Client used for interaction with the Infobip's Whatsapp API."""

    def __init__(self, client: Optional[HttpClient, Any]) -> None:
        self._client = client

    @classmethod
    def from_auth_params(cls, auth_params: Dict[str, str]) -> "WhatsappClient":
        """Create an Authentication instance from the provided dictionary and
        use it to instantiate WhatsappClient. Dictionary has to contain "base_url" and
        "api_key" to be able to authenticate with the Infobip's API.
        WhatsappClient instantiated this way will use the default HttpClient class for
        making HTTP requests.

        :param auth_params: Dictionary containing "base_url" and "api_key"
        :return: Instance of this class
        """
        client = HttpClient(Authentication(**auth_params))
        return cls(client)

    @classmethod
    def from_auth_instance(cls, auth_instance: Authentication) -> "WhatsappClient":
        """Instantiate WhatsappClient with the provided auth object.
        WhatsappClient instantiated this way will use the default HttpClient class for
        making HTTP requests.

        :param auth_instance: Authentication class instance
        :return: Instance of this class
        """
        client = HttpClient(auth_instance)
        return cls(client)

    @classmethod
    def from_provided_client(cls, client: Any) -> "WhatsappClient":
        """Instantiate WhatsappClient with the provided client object.
        WhatsappClient instantiated this way will use the provided client for making
        HTTP requests. This client can implement its own retry mechanisms, timeouts,
        etc., but it has to implement all the methods used in the default HttpClient
        class.

        :param client: Client used for making HTTP requests
        :return: Instance of this class
        """
        return cls(client)

    def send_text_message(
        self, message: Union[TextMessageBody, Dict]
    ) -> Union[Response, Any]:
        if not isinstance(message, TextMessageBody):
            message = TextMessageBody(**message)

        return self._client.post(
            "/whatsapp/1/message/text", message.dict(by_alias=True)
        )
