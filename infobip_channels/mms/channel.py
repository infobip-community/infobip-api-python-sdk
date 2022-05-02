from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, ResponseBase
from infobip_channels.mms.models.body.send_mms import MMSMessageBody
from infobip_channels.mms.models.query_parameters.get_inbound_mms_messages import (
    GetInboundMMSMessagesQueryParameters,
)
from infobip_channels.mms.models.query_parameters.get_mms_delivery_reports import (
    GetMMSDeliveryReportsQueryParameters,
)
from infobip_channels.mms.models.response.get_inbound_mms_messages import (
    GetInboundMMSMessagesResponse,
)
from infobip_channels.mms.models.response.get_mms_delivery_reports import (
    GetMMSDeliveryReportsResponse,
)
from infobip_channels.mms.models.response.send_mms import SendMMSResponse


class MMSChannel(Channel):
    """Class used for interaction with the Infobip's MMS API."""

    MMS_URL_TEMPLATE = "/mms/1/"

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_class: Type[ResponseBase] = SendMMSResponse,
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

    def send_mms_message(
        self, message: Union[MMSMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """Send a single MMS message to one destination address.

        :param message: Body of the message to send
        :return: Received response
        """
        message = self.validate_message_body(message, MMSMessageBody)
        body, content_type = message.to_multipart()

        response = self._client.post(
            self.MMS_URL_TEMPLATE + "single",
            body,
            PostHeaders(
                content_type=content_type, authorization=self._client.auth.api_key
            ),
        )
        return self._construct_response(response, SendMMSResponse)

    def get_mms_delivery_reports(
        self, query_parameters: Union[GetMMSDeliveryReportsQueryParameters, Dict]
    ) -> Union[ResponseBase, Any]:
        """Use this API method to learn if and when the message has been delivered to
        the recipient. Each request will return a batch of delivery reports - only once.
        The following API request will return only new reports that arrived since the
        last API request.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, GetMMSDeliveryReportsQueryParameters
        )
        response = self._client.get(
            self.MMS_URL_TEMPLATE + "reports",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetMMSDeliveryReportsResponse)

    def get_inbound_mms_messages(
        self, query_parameters: Union[GetInboundMMSMessagesQueryParameters, Dict]
    ) -> Union[ResponseBase, Any]:
        """Use this API method to fetch messages. Each request will return a batch of
        received messages - only once. The following API request will return only new
        messages that arrived since the last API request.

        :param query_parameters: Query parameters to send with the request
        :return: Received response
        """
        query_parameters = self.validate_query_parameter(
            query_parameters, GetInboundMMSMessagesQueryParameters
        )
        response = self._client.get(
            self.MMS_URL_TEMPLATE + "inbox/reports",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetInboundMMSMessagesResponse)
