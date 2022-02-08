from typing import Any, Dict, Union

import requests
from pydantic.error_wrappers import ValidationError

from whatsapp.models.audio_message import AudioMessageBody
from whatsapp.models.core import (
    Authentication,
    RequestHeaders,
    WhatsAppResponse,
    WhatsAppResponseError,
    WhatsAppResponseOK,
)
from whatsapp.models.document_message import DocumentMessageBody
from whatsapp.models.image_message import ImageMessageBody
from whatsapp.models.location_message import LocationMessageBody
from whatsapp.models.sticker_message import StickerMessageBody
from whatsapp.models.text_message import TextMessageBody
from whatsapp.models.video_message import VideoMessageBody


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
        try:
            response_class = self._get_response_class(response)
            return response_class(
                **{
                    "status_code": response.status_code,
                    "raw_response": response,
                    **response.json(),
                }
            )

        except (ValueError, ValidationError):
            return response

    @staticmethod
    def _get_response_class(response):
        if 200 <= response.status_code < 300:
            return WhatsAppResponseOK

        elif 400 <= response.status_code < 500:
            return WhatsAppResponseError

        raise ValueError


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
        """Instantiate WhatsAppChannel class with the provided auth object.
        WhatsAppChannel instantiated this way will use the default HttpClient class for
        making HTTP requests.

        :param auth_instance: Authentication class instance
        :return: Instance of this class
        """
        client = HttpClient(auth_instance)
        return cls(client)

    @classmethod
    def from_provided_client(cls, client: Any) -> "WhatsAppChannel":
        """Instantiate WhatsAppChannel class with the provided client object.
        WhatsAppChannel instantiated this way will use the provided client for making
        HTTP requests. This client can implement its own retry mechanisms, timeouts,
        etc., but it has to implement all the methods used in the default HttpClient
        class. When using WhatsAppChannel in this way, the user has to take care of
        providing a valid base_url and constructing headers to be used for every
        WhatsAppChannel request.

        :param client: Client used for making HTTP requests
        :return: Instance of this class
        """
        return cls(client)

    @staticmethod
    def validate_auth_params(base_url: str, api_key: str):
        """Validate the provided base_url and api_key. This validation is purely client
        side. If the parameters are validated successfully, an instance of the
        Authentication class is returned which holds the base_url and api_key values.

        :param base_url: Base url which the requests will call for each endpoint
        :param api_key: Secret used for authenticating the user
        :return: Authentication class instance
        """
        return Authentication(base_url=base_url, api_key=api_key)

    @staticmethod
    def build_request_headers(api_key: str):
        """Build the request headers dictionary which has to be used for each of the
        WhatsAppChannel requests.

        :param api_key: Key used for populating Authorization header
        :return: Dictionary of headers to be used for WhatsAppChannel requests
        """
        return RequestHeaders(authorization=api_key).dict(by_alias=True)

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

    def send_image_message(
        self, message: Union[ImageMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """
        Send an image to a single recipient. Image messages can only be successfully
        delivered, if the recipient has contacted the business within the last 24
        hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        if not isinstance(message, ImageMessageBody):
            message = ImageMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "image", message.dict(by_alias=True)
        )

    def send_sticker_message(
        self, message: Union[StickerMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send a sticker to a single recipient. Sticker messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        if not isinstance(message, StickerMessageBody):
            message = StickerMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "sticker", message.dict(by_alias=True)
        )

    def send_video_message(
        self, message: Union[VideoMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send a video to a single recipient. Video messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """

        if not isinstance(message, VideoMessageBody):
            message = VideoMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "video", message.dict(by_alias=True)
        )

    def send_audio_message(
        self, message: Union[AudioMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send an audio to a single recipient. Audio messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """

        if not isinstance(message, AudioMessageBody):
            message = AudioMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "audio", message.dict(by_alias=True)
        )

    def send_location_message(
        self, message: Union[LocationMessageBody, Dict]
    ) -> Union[WhatsAppResponse, Any]:
        """Send a location to a single recipient. Location messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """

        if not isinstance(message, LocationMessageBody):
            message = LocationMessageBody(**message)

        return self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "location", message.dict(by_alias=True)
        )
