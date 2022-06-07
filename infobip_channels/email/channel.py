from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, ResponseBase
from infobip_channels.email.models.body.add_new_domain import AddNewDomainMessageBody
from infobip_channels.email.models.body.reschedule_messages import (
    RescheduleMessagesMessageBody,
)
from infobip_channels.email.models.body.send_email import EmailMessageBody
from infobip_channels.email.models.body.update_scheduled_status import (
    UpdateScheduledStatusMessageBody,
)
from infobip_channels.email.models.body.update_tracking_events import (
    UpdateTrackingEventsMessageBody,
)
from infobip_channels.email.models.body.validate_email_adresses import (
    ValidateEmailAddressesMessageBody,
)
from infobip_channels.email.models.path_paramaters.delete_existing_domain import (
    DeleteExistingDomainPathParameter,
)
from infobip_channels.email.models.path_paramaters.get_domain_details import (
    GetDomainDetailsPathParameter,
)
from infobip_channels.email.models.path_paramaters.update_tracking_events import (
    UpdateTrackingEventsPathParameter,
)
from infobip_channels.email.models.path_paramaters.verify_domain import (
    VerifyDomainPathParameter,
)
from infobip_channels.email.models.query_parameters.delivery_reports import (
    DeliveryReportsQueryParameters,
)
from infobip_channels.email.models.query_parameters.get_all_domains import (
    GetAllDomainsForAccountQueryParameters,
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
from infobip_channels.email.models.response.add_new_domain import AddNewDomainResponse
from infobip_channels.email.models.response.core import EmailResponseError
from infobip_channels.email.models.response.delivery_reports import (
    DeliveryReportsResponse,
)
from infobip_channels.email.models.response.get_all_domains import (
    GetAllDomainsForAccountResponse,
)
from infobip_channels.email.models.response.get_domain_details import (
    GetDomainDetailsResponse,
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
from infobip_channels.email.models.response.update_tracking_events import (
    UpdateTrackingEventsResponse,
)
from infobip_channels.email.models.response.validate_email_adresses import (
    ValidateEmailAddressesResponse,
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

    def validate_email_addresses(
        self, message: Union[ValidateEmailAddressesMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Run validation to identify poor quality emails to clean up your recipient list.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, ValidateEmailAddressesMessageBody)

        response = self._client.post(
            self.EMAIL_URL_TEMPLATE_V2 + "validation",
            message.dict(by_alias=True),
        )
        return self._construct_response(response, ValidateEmailAddressesResponse)

    def get_all_domains_for_account(
        self,
        query_parameters: Union[GetAllDomainsForAccountQueryParameters, Dict] = None,
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This API is to get all domain associated with the account. It also provides
        details of the retrieved domain like the DNS records, Tracking details,
        Active/Blocked status,etc.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """

        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetAllDomainsForAccountQueryParameters
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "domains",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetAllDomainsForAccountResponse)

    def get_domain_details(
        self,
        parameter: Union[GetDomainDetailsPathParameter, Dict],
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This API provides with the details of the domain like the DNS records,
        Tracking details, Active/Blocked status,etc.

        :param parameter: Domain for which the details need to be viewed.
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(
            parameter, GetDomainDetailsPathParameter
        )

        response = self._client.get(
            self.EMAIL_URL_TEMPLATE_V1 + "domains/" + path_parameter.domain_name,
        )
        return self._construct_response(response, GetDomainDetailsResponse)

    def add_new_domain(
        self, message: Union[AddNewDomainMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This method allows you to add new domains with a limit to create a maximum of
        10 domains in a day.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, AddNewDomainMessageBody)

        response = self._client.post(
            self.EMAIL_URL_TEMPLATE_V1 + "domains",
            message.dict(by_alias=True),
        )
        return self._construct_response(response, AddNewDomainResponse)

    def delete_existing_domain(
        self, parameter: Union[DeleteExistingDomainPathParameter, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This method allows you to delete an existing domain.

        :param parameter: Domain name which needs to be deleted.
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(
            parameter, DeleteExistingDomainPathParameter
        )

        response = self._client.delete(
            self.EMAIL_URL_TEMPLATE_V1 + "domains/" + path_parameter.domain_name,
        )
        return response

    def verify_domain(
        self, parameter: Union[VerifyDomainPathParameter, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        API request to verify records(TXT, MX, DKIM) associated with the provided
        domain.

        :param parameter: Domain name which needs to be deleted.
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(
            parameter, VerifyDomainPathParameter
        )

        response = self._client.post(
            self.EMAIL_URL_TEMPLATE_V1
            + "domains/"
            + path_parameter.domain_name
            + "/verify"
        )
        return response

    def update_tracking_events(
        self,
        parameter: Union[UpdateTrackingEventsPathParameter, Dict],
        message: Union[UpdateTrackingEventsMessageBody, Dict],
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        API to update tracking events for the provided domain. Tracking events can be
        updated only for CLICKS, OPENS and UNSUBSCRIBES.

        :param parameter: Domain name which needs to be deleted.
        :param message: Body of the message to send
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(
            parameter, UpdateTrackingEventsPathParameter
        )

        message = self.validate_message_body(message, UpdateTrackingEventsMessageBody)

        response = self._client.put(
            self.EMAIL_URL_TEMPLATE_V1
            + "domains/"
            + path_parameter.domain_name
            + "/tracking",
            message.dict(by_alias=True),
        )
        return self._construct_response(response, UpdateTrackingEventsResponse)
