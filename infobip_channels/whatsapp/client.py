from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests
from pydantic import AnyHttpUrl
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.audio_message import AudioMessageBody
from infobip_channels.whatsapp.models.buttons_message import ButtonsMessageBody
from infobip_channels.whatsapp.models.contact_message import ContactMessageBody
from infobip_channels.whatsapp.models.core import (
    Authentication,
    MessageBody,
    RequestHeaders,
    WhatsAppResponse,
    WhatsAppResponseError,
    WhatsAppResponseOK,
)
from infobip_channels.whatsapp.models.document_message import DocumentMessageBody
from infobip_channels.whatsapp.models.image_message import ImageMessageBody
from infobip_channels.whatsapp.models.list_message import ListMessageBody
from infobip_channels.whatsapp.models.location_message import LocationMessageBody
from infobip_channels.whatsapp.models.multi_product_message import (
    MultiProductMessageBody,
)
from infobip_channels.whatsapp.models.product_message import ProductMessageBody
from infobip_channels.whatsapp.models.sticker_message import StickerMessageBody
from infobip_channels.whatsapp.models.template_message import (
    TemplateMessageBody,
    TemplateMessageResponseOK,
)
from infobip_channels.whatsapp.models.text_message import TextMessageBody
from infobip_channels.whatsapp.models.video_message import VideoMessageBody


class HttpClient:
    """Default HTTP client used by the WhatsAppChannel for making HTTP requests."""

    def __init__(self, auth: Authentication):
        self.auth = auth
        self.headers = RequestHeaders(authorization=self.auth.api_key)

    def post(self, endpoint: str, body: Dict) -> requests.Response:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        return requests.post(
            url=url, json=body, headers=self.headers.dict(by_alias=True)
        )


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
    def validate_auth_params(base_url: AnyHttpUrl, api_key: str):
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

    @staticmethod
    def validate_message_body(
        message: Union[MessageBody, TemplateMessageBody, Dict],
        message_type: Union[Type[MessageBody], Type[TemplateMessageBody]],
    ) -> Union[MessageBody, TemplateMessageBody]:
        """Validate the message by trying to instantiate the provided type class.
        If the message passed is already of that type, just return it as is.

        :param message: Message body to validate
        :param message_type: Type of the message body
        :return: Class instance corresponding to the provided message body type
        """
        return message if isinstance(message, message_type) else message_type(**message)

    @staticmethod
    def _construct_response(
        response: Union[requests.Response, Any],
        response_class: Type[WhatsAppResponse],
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        try:
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
    def _get_response_class(
        response: Union[requests.Response, Any],
        response_ok_model: Type[WhatsAppResponse] = WhatsAppResponseOK,
    ) -> Type[WhatsAppResponse]:

        if response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
            return response_ok_model

        elif response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.TOO_MANY_REQUESTS,
            HTTPStatus.FORBIDDEN,
        ):
            return WhatsAppResponseError

        raise ValueError

    def send_template_message(
        self, message: Union[TemplateMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a single or multiple template messages to a one or more recipients.
        Template messages can be sent and delivered at anytime. Each template sent
        needs to be registered and pre-approved by WhatsApp.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, TemplateMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "template",
            message.dict(by_alias=True),
        )
        response_class = self._get_response_class(response, TemplateMessageResponseOK)
        return self._construct_response(response, response_class)

    def send_text_message(
        self, message: Union[TextMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a text message to a single recipient. Text messages can only be
        successfully delivered, if the recipient has contacted the business within the
        last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, TextMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "text", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_document_message(
        self, message: Union[DocumentMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a document to a single recipient. Document messages can only be
        successfully delivered, if the recipient has contacted the business within the
        last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, DocumentMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "document", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_image_message(
        self, message: Union[ImageMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """
        Send an image to a single recipient. Image messages can only be successfully
        delivered, if the recipient has contacted the business within the last 24
        hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ImageMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "image", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_audio_message(
        self, message: Union[AudioMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send an audio to a single recipient. Audio messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, AudioMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "audio", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_video_message(
        self, message: Union[VideoMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a video to a single recipient. Video messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, VideoMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "video", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_sticker_message(
        self, message: Union[StickerMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a sticker to a single recipient. Sticker messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, StickerMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "sticker", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_location_message(
        self, message: Union[LocationMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a location to a single recipient. Location messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, LocationMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "location", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_contact_message(
        self, message: Union[ContactMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send a contact to a single recipient. Contact messages can only be
        successfully delivered, if the recipient has contacted the business within
        the last 24 hours, otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ContactMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "contact", message.dict(by_alias=True)
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_interactive_buttons_message(
        self, message: Union[ButtonsMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send an interactive buttons message to a single recipient. Interactive
        buttons messages can only be successfully delivered, if the recipient has
        contacted the business within the last 24 hours, otherwise template message
        should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ButtonsMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "interactive/buttons",
            message.dict(by_alias=True),
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_interactive_list_message(
        self, message: Union[ListMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send an interactive list message to a single recipient. Interactive list
        messages can only be successfully delivered, if the recipient has contacted
        the business within the last 24 hours, otherwise template message should be
        used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ListMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "interactive/list",
            message.dict(by_alias=True),
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_interactive_product_message(
        self, message: Union[ProductMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send an interactive product message to a single recipient. Interactive
        product messages can only be successfully delivered, if the recipient has
        contacted the business within the last 24 hours, otherwise template message
        should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ProductMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "interactive/product",
            message.dict(by_alias=True),
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)

    def send_interactive_multi_product_message(
        self, message: Union[MultiProductMessageBody, Dict]
    ) -> Union[WhatsAppResponse, requests.Response, Any]:
        """Send an interactive multi-product message to a single recipient.
        Interactive multi-product messages can only be successfully delivered,
        if the recipient has contacted the business within the last 24 hours,
        otherwise template message should be used.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, MultiProductMessageBody)

        response = self._client.post(
            self.SEND_MESSAGE_URL_TEMPLATE + "interactive/multi-product",
            message.dict(by_alias=True),
        )
        response_class = self._get_response_class(response)
        return self._construct_response(response, response_class)
