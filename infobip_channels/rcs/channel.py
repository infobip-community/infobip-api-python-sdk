from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase

from infobip_channels.rcs.Models.response.core import RcsResponseError
from infobip_channels.rcs.Models.response.core import RcsResponseOK
from infobip_channels.rcs.Models.body.send_rcs import RCSMessageBody


class RCSChannel(Channel):
    """Class used for interaction with the Infobip's RCS API."""
    RCS_URL_TEMPLATE = "/ott/rcs/1/"

    def _get_custom_response_class(
            self,
            raw_response: Union[requests.Response, Any],
            response_ok_class: Type[ResponseBase] = RcsResponseOK,
            *args,
            **kwargs
    ) -> Type[ResponseBase]:
        if raw_response.status_code == HTTPStatus.OK:
            return response_ok_class

        if raw_response.status_code in (
                HTTPStatus.OK,
                HTTPStatus.BAD_REQUEST,
        ):
            return RcsResponseError

        raise ValueError

    def send_rcs_message(
            self, message: Union[RCSMessageBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """Used for sending single RCS messages

        :param message: Body of the message to send
        :return: Received response
        """

        message = self.validate_message_body(message, RCSMessageBody)
        response = self._client.post(
            self.RCS_URL_TEMPLATE + "message", message.dict(by_alias=True)
        )
        return self._construct_response(response, RcsResponseOK)

