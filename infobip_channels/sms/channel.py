from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, QueryParameter, ResponseBase

from infobip_channels.sms.models.response.send_message import SendSMSResponse
from infobip_channels.sms.models.body.send_message import SMSMessageBody


class SMSChannel(Channel):
    """Class used for interaction with the Infobip's SMS API."""

    SMS_URL_TEMPLATE = "/sms/2/text/"

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
        if raw_response.status_code in (
                HTTPStatus.OK,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.INTERNAL_SERVER_ERROR,
        ):
            return response_class

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
            self.SMS_URL_TEMPLATE + "advanced",
            message.dict(by_alias=True),
            PostHeaders(
                authorization=self._client.auth.api_key
            ),
        )
        return self._construct_response(response, SendSMSResponse)
