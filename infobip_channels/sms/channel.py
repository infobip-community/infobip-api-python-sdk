from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, QueryParameter, ResponseBase
from infobip_channels.sms.models.body.preview_message import PreviewSMSMessage
from infobip_channels.sms.models.body.send_binary_message import BinarySMSMessageBody
from infobip_channels.sms.models.body.send_message import SMSMessageBody
from infobip_channels.sms.models.query_parameters.sms_send_message import (
    SendSMSMessageQueryParameters,
)
from infobip_channels.sms.models.response.core import SMSResponseError
from infobip_channels.sms.models.response.preview_message import (
    PreviewSMSMessageResponse,
)
from infobip_channels.sms.models.response.send_message import SendSMSResponse


class SMSChannel(Channel):
    """Class used for interaction with the Infobip's SMS API."""

    SMS_URL_TEMPLATE_VERSION_1 = "/sms/1/"
    SMS_URL_TEMPLATE_VERSION_2 = "/sms/2/"

    @staticmethod
    def validate_query_parameter(
        parameter: Union[QueryParameter, Dict], parameter_type: Type[QueryParameter]
    ) -> QueryParameter:
        """
        Validate the query parameter by trying to instantiate the provided class.
        If the passed parameter is already of that type, just return it as is.

        :param parameter: Query parameter to validate
        :param parameter_type: Type of the query parameter
        :return: Class instance corresponding to the provided parameter type
        """
        return (
            parameter
            if isinstance(parameter, parameter_type)
            else parameter_type(**parameter)
        )

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_class: Type[ResponseBase] = SendSMSResponse,
        *args,
        **kwargs
    ) -> Type[ResponseBase]:

        if raw_response.status_code in (HTTPStatus.OK,):
            return response_class
        elif raw_response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.TOO_MANY_REQUESTS,
            HTTPStatus.INTERNAL_SERVER_ERROR,
            HTTPStatus.NOT_FOUND,
        ):
            return SMSResponseError

        raise ValueError

    def send_sms_message(
        self, message: Union[SMSMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """99% of all use cases can be achieved by using this API method. Everything
        from sending a simple single message to a single destination, up to batch
        sending of personalized messages to the thousands of recipients with a single
        API request. Language, transliteration, scheduling and every advanced feature
        you can think of is supported.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, SMSMessageBody)

        response = self._client.post(
            self.SMS_URL_TEMPLATE_VERSION_2 + "text/advanced",
            message.dict(by_alias=True),
            PostHeaders(authorization=self._client.auth.api_key),
        )
        return self._construct_response(response, SendSMSResponse)

    def send_binary_sms_message(
        self, message: Union[BinarySMSMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """Send single or multiple binary messages to one or more destination address.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, BinarySMSMessageBody)

        response = self._client.post(
            self.SMS_URL_TEMPLATE_VERSION_2 + "binary/advanced",
            message.dict(by_alias=True),
            PostHeaders(authorization=self._client.auth.api_key),
        )
        return self._construct_response(response, SendSMSResponse)

    def send_sms_message_over_query_parameters(
        self, query_parameters: Union[SendSMSMessageQueryParameters, Dict]
    ) -> Union[ResponseBase, Any]:
        """
        All message parameters of the message can be defined in the query string. Use
        this method only if Send SMS message is not an option for your use case!
        Note: Make sure that special characters and user credentials are properly
        encoded

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, SendSMSMessageQueryParameters
        )
        query_parameters.url_encode()
        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "text/query",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, SendSMSResponse)

    def preview_sms_message(
        self, message: Union[PreviewSMSMessage, Dict]
    ) -> Union[ResponseBase, Any]:
        """
        Avoid unpleasant surprises and check how different message configurations
        will affect your message text, number of characters and message parts.

        :param message: Body of the message to send
        :return: Received response
        """

        message = self.validate_message_body(message, PreviewSMSMessage)

        response = self._client.post(
            self.SMS_URL_TEMPLATE_VERSION_1 + "preview",
            message.dict(by_alias=True),
            PostHeaders(authorization=self._client.auth.api_key),
        )
        return self._construct_response(response, PreviewSMSMessageResponse)
