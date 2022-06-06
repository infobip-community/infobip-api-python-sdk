from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, ResponseBase
from infobip_channels.email.models.body.reschedule_messages import (
    RescheduleMessagesMessageBody,
)
from infobip_channels.email.models.body.send_email import EmailMessageBody
from infobip_channels.email.models.body.update_scheduled_status import (
    UpdateScheduledStatusMessageBody,
)
from infobip_channels.email.models.query_parameters.delivery_reports import (
    DeliveryReportsQueryParameters,
)
from infobip_channels.email.models.query_parameters.get_logs import (
    GetLogsQueryParameters,
)
from infobip_channels.email.models.query_parameters.get_sent_bulks import (
    GetSentBulksQueryParameters,
)
from infobip_channels.email.models.query_parameters.get_sent_bulks_status import (
    GetSentBulksStatusQueryParameters,
)
from infobip_channels.email.models.query_parameters.reschedule_messages import (
    RescheduleMessagesQueryParameters,
)
from infobip_channels.email.models.query_parameters.update_scheduled_status import (
    UpdateScheduledStatusQueryParameters,
)
from infobip_channels.email.models.response.core import EmailResponseError
from infobip_channels.email.models.response.delivery_reports import (
    DeliveryReportsResponse,
)
from infobip_channels.email.models.response.get_logs import GetLogsResponse
from infobip_channels.email.models.response.get_sent_bulk_status import (
    GetSentEmailBulksStatusResponse,
)
from infobip_channels.email.models.response.get_sent_bulks import (
    GetSentEmailBulksResponse,
)
from infobip_channels.email.models.response.reschedule_messages import (
    RescheduleMessagesResponse,
)
from infobip_channels.email.models.response.send_email import SendEmailResponse
from infobip_channels.email.models.response.update_scheduled_status import (
    UpdateScheduledStatusResponse,
)


class EmailChannel(Channel):
    """Class used for interaction with the Infobip's Email API."""

    EMAIL_URL_TEMPLATE_V1 = "/email/1/"
    EMAIL_URL_TEMPLATE_V2 = "/email/2/"

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_class: Type[ResponseBase] = SendEmailResponse,
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
            return EmailResponseError

        raise ValueError

    def send_email_message(
        self, message: Union[EmailMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Send an email or multiple emails to a recipient or multiple recipients
        with CC/BCC enabled.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, EmailMessageBody)
        body, content_type = message.to_multipart()

        response = self._client.post(
            self.EMAIL_URL_TEMPLATE_V2 + "send",
            body,
            PostHeaders(
                content_type=content_type, authorization=self._client.auth.api_key
            ),
        )
        return self._construct_response(response, SendEmailResponse)

    def email_delivery_reports(
        self, query_parameters: Union[DeliveryReportsQueryParameters, Dict] = None
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Get one-time delivery reports for all sent emails.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """

        query_parameters = self.validate_query_parameter(
            query_parameters or {}, DeliveryReportsQueryParameters
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "reports",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, DeliveryReportsResponse)

    def get_email_logs(
        self, query_parameters: Union[GetLogsQueryParameters, Dict] = None
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This method allows you to get email logs of sent Email messagesId for
        request. Email logs are available for the last 48 hours.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """

        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetLogsQueryParameters
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "logs",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetLogsResponse)

    def get_sent_email_bulks(
        self, query_parameters: Union[GetSentBulksQueryParameters, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        See the scheduled time of your Email messages.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """

        query_parameters = self.validate_query_parameter(
            query_parameters, GetSentBulksQueryParameters
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "bulks",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetSentEmailBulksResponse)

    def get_sent_email_bulks_status(
        self, query_parameters: Union[GetSentBulksStatusQueryParameters, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        See the status of scheduled email messages.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """

        query_parameters = self.validate_query_parameter(
            query_parameters, GetSentBulksStatusQueryParameters
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "bulks/status",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetSentEmailBulksStatusResponse)

    def reschedule_email_messages(
        self,
        query_parameters: Union[RescheduleMessagesQueryParameters, Dict],
        message: Union[RescheduleMessagesMessageBody, Dict],
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Change the date and time for sending scheduled Email messages.

        :param query_parameters: Query parameters to send with the request
        :param message: Body of the message to send
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, RescheduleMessagesQueryParameters
        )

        message = self.validate_message_body(message, RescheduleMessagesMessageBody)

        response = self._client.put(
            self.EMAIL_URL_TEMPLATE_V1 + "bulks",
            message.dict(by_alias=True),
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, RescheduleMessagesResponse)

    def update_scheduled_email_messages(
        self,
        query_parameters: Union[UpdateScheduledStatusQueryParameters, Dict],
        message: Union[UpdateScheduledStatusMessageBody, Dict],
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Change status or completely cancel sending of scheduled Email messages.

        :param query_parameters: Query parameters to send with the request
        :param message: Body of the message to send
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, UpdateScheduledStatusQueryParameters
        )

        message = self.validate_message_body(message, UpdateScheduledStatusMessageBody)

        response = self._client.put(
            self.EMAIL_URL_TEMPLATE_V1 + "bulks/status",
            message.dict(by_alias=True),
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, UpdateScheduledStatusResponse)
