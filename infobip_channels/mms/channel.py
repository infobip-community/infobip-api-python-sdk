from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import PostHeaders, ResponseBase
from infobip_channels.mms.models.body.send_mms import MMSMessageBody
from infobip_channels.mms.models.response.send_mms import SendMMSResponse


class MMSChannel(Channel):
    """Class used for interaction with the Infobip's MMS API."""

    MMS_URL_TEMPLATE = "/mms/1/"

    def _get_custom_response_class(
        self, raw_response: Union[requests.Response, Any], *args, **kwargs
    ) -> Type[ResponseBase]:
        if raw_response.status_code in (
            HTTPStatus.OK,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.INTERNAL_SERVER_ERROR,
        ):
            return SendMMSResponse

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
        return self._construct_response(response)
