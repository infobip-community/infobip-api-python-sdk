from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.models.body.audio_message import AudioMessageBody
from infobip_channels.whatsapp.models.body.buttons_message import ButtonsMessageBody
from infobip_channels.whatsapp.models.body.contact_message import ContactMessageBody
from infobip_channels.whatsapp.models.body.create_template import CreateTemplate
from infobip_channels.whatsapp.models.body.document_message import DocumentMessageBody
from infobip_channels.whatsapp.models.body.image_message import ImageMessageBody
from infobip_channels.whatsapp.models.body.list_message import ListMessageBody
from infobip_channels.whatsapp.models.body.location_message import LocationMessageBody
from infobip_channels.whatsapp.models.body.multi_product_message import (
    MultiProductMessageBody,
)
from infobip_channels.whatsapp.models.body.product_message import ProductMessageBody
from infobip_channels.whatsapp.models.body.sticker_message import StickerMessageBody
from infobip_channels.whatsapp.models.body.template_message import TemplateMessageBody
from infobip_channels.whatsapp.models.body.text_message import TextMessageBody
from infobip_channels.whatsapp.models.body.video_message import VideoMessageBody
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)
from infobip_channels.whatsapp.models.response.core import (
    WhatsAppResponseError,
    WhatsAppResponseOK,
)
from infobip_channels.whatsapp.models.response.create_template import (
    CreateTemplateResponseOK,
)
from infobip_channels.whatsapp.models.response.get_templates import (
    GetTemplatesResponseOK,
)
from infobip_channels.whatsapp.models.response.template_message import (
    TemplateMessageResponseOK,
)


class WhatsAppChannel(Channel):
    """Class used for interaction with the Infobip's WhatsApp API."""

    SEND_MESSAGE_URL_TEMPLATE = "/whatsapp/1/message/"
    MANAGE_URL_TEMPLATE = "/whatsapp/1/senders/"

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_ok_model: Type[ResponseBase] = WhatsAppResponseOK,
        *args,
        **kwargs
    ) -> Type[ResponseBase]:

        if raw_response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
            return response_ok_model

        elif raw_response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.TOO_MANY_REQUESTS,
        ):
            return WhatsAppResponseError

        raise ValueError

    def send_template_message(
        self, message: Union[TemplateMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response, TemplateMessageResponseOK)

    def send_text_message(
        self, message: Union[TextMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_document_message(
        self, message: Union[DocumentMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_image_message(
        self, message: Union[ImageMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_audio_message(
        self, message: Union[AudioMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_video_message(
        self, message: Union[VideoMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_sticker_message(
        self, message: Union[StickerMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_location_message(
        self, message: Union[LocationMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_contact_message(
        self, message: Union[ContactMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_interactive_buttons_message(
        self, message: Union[ButtonsMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_interactive_list_message(
        self, message: Union[ListMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_interactive_product_message(
        self, message: Union[ProductMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def send_interactive_multi_product_message(
        self, message: Union[MultiProductMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
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
        return self._construct_response(response)

    def get_templates(
        self, parameter: Union[ManageTemplatesPathParameters, Dict]
    ) -> Union[ResponseBase, Any]:
        """Get all the templates and their statuses for a given sender.

        :param parameter: Registered WhatsApp sender number. Must be in international
        format
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(
            parameter, ManageTemplatesPathParameters
        )
        response = self._client.get(
            self.MANAGE_URL_TEMPLATE + path_parameter.sender + "/templates"
        )
        return self._construct_response(response, GetTemplatesResponseOK)

    def create_template(
        self,
        parameter: Union[ManageTemplatesPathParameters, Dict],
        message: Union[CreateTemplate, Dict],
    ) -> Union[ResponseBase, Any]:
        """Create WhatsApp template. Created template will be submitted for
        WhatsApp's review and approval. Once approved, template can be sent to
        end-users. Refer to template guidelines for additional info.

        :param parameter: Registered WhatsApp sender number. Must be in international
        format
        :param message: Body of the template to send
        :return: Received response
        """
        message = self.validate_message_body(message, CreateTemplate)
        path_parameter = self.validate_path_parameter(
            parameter, ManageTemplatesPathParameters
        )
        response = self._client.post(
            self.MANAGE_URL_TEMPLATE + path_parameter.sender + "/templates",
            message.dict(by_alias=True),
        )
        return self._construct_response(response, CreateTemplateResponseOK)
