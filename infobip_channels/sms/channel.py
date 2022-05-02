from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, ResponseBase
from infobip_channels.sms.models.body.preview_message import PreviewSMSMessage
from infobip_channels.sms.models.body.reschedule_sms_messages import (
    RescheduleSMSMessagesMessageBody,
)
from infobip_channels.sms.models.body.send_binary_message import BinarySMSMessageBody
from infobip_channels.sms.models.body.send_message import SMSMessageBody
from infobip_channels.sms.models.body.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesMessageBody,
)
from infobip_channels.sms.models.query_parameters.get_inbound_messages import (
    GetInboundSMSMessagesQueryParameters,
)
from infobip_channels.sms.models.query_parameters.get_outbound_delivery_reports import (
    GetOutboundSMSDeliveryReportsQueryParameters,
)
from infobip_channels.sms.models.query_parameters.get_outbound_logs import (
    GetOutboundSMSLogsQueryParameters,
)
from infobip_channels.sms.models.query_parameters.get_scheduled_messages import (
    GetScheduledSMSMessagesQueryParameters,
)
from infobip_channels.sms.models.query_parameters.get_scheduled_messages_status import (
    GetScheduledSMSMessagesStatusQueryParameters,
)
from infobip_channels.sms.models.query_parameters.reschedule_messages import (
    RescheduleSMSMessagesQueryParameters,
)
from infobip_channels.sms.models.query_parameters.send_message import (
    SendSMSMessageQueryParameters,
)
from infobip_channels.sms.models.query_parameters.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesQueryParameters,
)
from infobip_channels.sms.models.response.core import SMSResponseError
from infobip_channels.sms.models.response.get_scheduled_messages import (
    GetScheduledSMSMessagesResponse,
)
from infobip_channels.sms.models.response.get_scheduled_messages_status import (
    GetScheduledSMSMessagesStatusResponse,
)
from infobip_channels.sms.models.response.inbound_messages import (
    InboundSMSMessagesResponse,
)
from infobip_channels.sms.models.response.outbound_delivery_reports import (
    OutboundDeliveryReportsResponse,
)
from infobip_channels.sms.models.response.outbound_message_logs import (
    OutboundMessageLogsResponse,
)
from infobip_channels.sms.models.response.preview_message import (
    PreviewSMSMessageResponse,
)
from infobip_channels.sms.models.response.reschedule_sms_messages import (
    RescheduleSMSMessagesResponse,
)
from infobip_channels.sms.models.response.send_message import SendSMSResponse
from infobip_channels.sms.models.response.update_scheduled_messages_status import (
    UpdateScheduledSMSMessagesStatusResponse,
)


class SMSChannel(Channel):
    """Class used for interaction with the Infobip's SMS API."""

    SMS_URL_TEMPLATE_VERSION_1 = "/sms/1/"
    SMS_URL_TEMPLATE_VERSION_2 = "/sms/2/"

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_class: Type[ResponseBase] = SendSMSResponse,
        *args,
        **kwargs
    ) -> Type[ResponseBase]:

        if raw_response.status_code == HTTPStatus.OK:
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
        )
        return self._construct_response(response, SendSMSResponse)

    def send_sms_message_over_query_parameters(
        self, query_parameters: Union[SendSMSMessageQueryParameters, Dict]
    ) -> Union[ResponseBase, Any]:
        """
        All message parameters of the message can be defined in the query string. Use
        this method only if Send SMS message is not an option for your use case!

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
        )
        return self._construct_response(response, PreviewSMSMessageResponse)

    def get_outbound_sms_delivery_reports(
        self,
        query_parameters: Union[
            GetOutboundSMSDeliveryReportsQueryParameters, Dict
        ] = None,
    ) -> Union[ResponseBase, Any]:
        """If you are for any reason unable to receive real-time delivery reports on
        your endpoint, you can use this API method to learn if and when the message
        has been delivered to the recipient. Each request will return a batch of
        delivery reports - only once. The following API request will return only new
        reports that arrived since the last API request in the last 48 hours.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetOutboundSMSDeliveryReportsQueryParameters
        )

        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "reports",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, OutboundDeliveryReportsResponse)

    def get_outbound_sms_message_logs(
        self,
        query_parameters: Union[GetOutboundSMSLogsQueryParameters, Dict] = None,
    ) -> Union[ResponseBase, Any]:
        """Use this method for displaying logs for example in the user interface.
        Available are the logs for the last 48 hours and you can only retrieve
        maximum of 1000 logs per call. See message delivery reports if your use case
        is to verify message delivery.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetOutboundSMSLogsQueryParameters
        )

        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "logs",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, OutboundMessageLogsResponse)

    def get_inbound_sms_messages(
        self,
        query_parameters: Union[GetInboundSMSMessagesQueryParameters, Dict] = None,
    ) -> Union[ResponseBase, Any]:
        """If for some reason you are unable to receive incoming SMS to the endpoint
        of your choice in real time, you can use this API call to fetch messages.
        Each request will return a batch of received messages - only once. The API
        request will only return new messages that arrived since the last API request.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetInboundSMSMessagesQueryParameters
        )

        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "inbox/reports",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, InboundSMSMessagesResponse)

    def get_scheduled_sms_messages(
        self,
        query_parameters: Union[GetScheduledSMSMessagesQueryParameters, Dict],
    ) -> Union[ResponseBase, Any]:
        """See the status and the scheduled time of your SMS messages.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, GetScheduledSMSMessagesQueryParameters
        )

        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "bulks",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetScheduledSMSMessagesResponse)

    def reschedule_sms_messages(
        self,
        query_parameters: Union[RescheduleSMSMessagesQueryParameters, Dict],
        message: Union[RescheduleSMSMessagesMessageBody, Dict],
    ) -> Union[ResponseBase, Any]:
        """Change the date and time for sending scheduled messages.

        :param query_parameters: Query parameters to send with the request
        :param message: Body of the message to send
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, RescheduleSMSMessagesQueryParameters
        )

        message = self.validate_message_body(message, RescheduleSMSMessagesMessageBody)

        response = self._client.put(
            self.SMS_URL_TEMPLATE_VERSION_1 + "bulks",
            message.dict(by_alias=True),
            params=query_parameters.dict(by_alias=True),
        )

        return self._construct_response(response, RescheduleSMSMessagesResponse)

    def get_scheduled_sms_messages_status(
        self,
        query_parameters: Union[GetScheduledSMSMessagesStatusQueryParameters, Dict],
    ) -> Union[ResponseBase, Any]:
        """See the status of scheduled messages.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, GetScheduledSMSMessagesStatusQueryParameters
        )

        response = self._client.get(
            self.SMS_URL_TEMPLATE_VERSION_1 + "bulks/status",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetScheduledSMSMessagesStatusResponse)

    def update_scheduled_sms_messages_status(
        self,
        query_parameters: Union[UpdateScheduledSMSMessagesQueryParameters, Dict],
        message: Union[UpdateScheduledSMSMessagesMessageBody, Dict],
    ) -> Union[ResponseBase, Any]:
        """Change status or completely cancel sending of scheduled messages.

        :param query_parameters: Query parameters to send with the request
        :param message: Body of the message to send
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, UpdateScheduledSMSMessagesQueryParameters
        )

        message = self.validate_message_body(
            message, UpdateScheduledSMSMessagesMessageBody
        )

        response = self._client.put(
            self.SMS_URL_TEMPLATE_VERSION_1 + "bulks/status",
            message.dict(by_alias=True),
            params=query_parameters.dict(by_alias=True),
        )

        return self._construct_response(
            response, UpdateScheduledSMSMessagesStatusResponse
        )
