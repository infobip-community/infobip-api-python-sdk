from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_channels.web_rtc.models.body.generate_token import GenerateTokenBody
from infobip_channels.web_rtc.models.body.save_application import SaveApplicationBody
from infobip_channels.web_rtc.models.body.update_application import (
    UpdateApplicationBody,
)
from infobip_channels.web_rtc.models.path_parameters.web_rtc_application import (
    WebRtcPathParameters,
)
from infobip_channels.web_rtc.models.response.core import (
    WebRtcResponseError,
    WebRtcResponseOK,
)
from infobip_channels.web_rtc.models.response.generate_token import (
    GenerateTokenResponseOK,
)
from infobip_channels.web_rtc.models.response.get_applications import (
    GetApplicationsResponseOK,
)


class WebRtcChannel(Channel):
    """Class used for interaction with the Infobip's WebRTC API."""

    WEB_RTC_URL_TEMPLATE = "/webrtc/1/"

    def _get_custom_response_class(
        self,
        response: Union[requests.Response, Any],
        response_ok_model: Type[ResponseBase] = WebRtcResponseOK,
        *args,
        **kwargs
    ) -> Type[ResponseBase]:

        if response.status_code == HTTPStatus.OK:
            return response_ok_model

        elif response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
        ):
            return WebRtcResponseError

        raise ValueError

    def generate_token(
        self, message: Union[GenerateTokenBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        This endpoint allows you to generate token for WebRTC channel.

        :param message: Body of request to send
        :return: Received response
        """
        message = self.validate_message_body(message, GenerateTokenBody)
        response = self._client.post(
            self.WEB_RTC_URL_TEMPLATE + "token", message.dict(by_alias=True)
        )
        return self._construct_response(response, GenerateTokenResponseOK)

    def save_application(
        self, message: Union[SaveApplicationBody, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Create and configure a new WebRTC application.

        :param message: Body of request to send
        :return: Received response
        """
        message = self.validate_message_body(message, SaveApplicationBody)
        response = self._client.post(
            self.WEB_RTC_URL_TEMPLATE + "applications", message.dict(by_alias=True)
        )
        return self._construct_response(response)

    def get_applications(self) -> Union[ResponseBase, requests.Response, Any]:
        """
        List all applications for WebRTC channel.

        :return: Received response
        """
        response = self._client.get(self.WEB_RTC_URL_TEMPLATE + "applications")
        return self._construct_response(response, GetApplicationsResponseOK)

    def get_application(
        self, parameter: Union[WebRtcPathParameters, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Get a single WebRTC application to see its configuration details.

        :param parameter: Application Id
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(parameter, WebRtcPathParameters)
        response = self._client.get(
            self.WEB_RTC_URL_TEMPLATE + "applications/" + path_parameter.id
        )
        return self._construct_response(response)

    def delete_application(
        self, parameter: Union[WebRtcPathParameters, Dict]
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Delete WebRTC application for a given id.

        :param parameter: Application Id
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(parameter, WebRtcPathParameters)
        response = self._client.delete(
            self.WEB_RTC_URL_TEMPLATE + "applications/" + path_parameter.id
        )
        return self._construct_response(response)

    def update_application(
        self,
        parameter: Union[WebRtcPathParameters, Dict],
        message: Union[UpdateApplicationBody, Dict],
    ) -> Union[ResponseBase, requests.Response, Any]:
        """
        Change configuration details of your existing WebRTC application.

        :param parameter: Application Id
        :param message: Body of request to send
        :return: Received response
        """
        path_parameter = self.validate_path_parameter(parameter, WebRtcPathParameters)
        message = self.validate_message_body(message, UpdateApplicationBody)
        response = self._client.put(
            self.WEB_RTC_URL_TEMPLATE + "applications/" + path_parameter.id,
            message.dict(by_alias=True),
        )
        return self._construct_response(response)
