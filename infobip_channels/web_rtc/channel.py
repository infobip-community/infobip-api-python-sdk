from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_channels.web_rtc.models.path_parameters.core import PathParameter
from infobip_channels.web_rtc.models.response.core import (
    WebRtcResponseError,
    WebRtcResponseOK,
)


class WebRtcChannel(Channel):
    """Class used for interaction with the Infobip's WhatsApp API."""

    WEB_RTC_URL_TEMPLATE = "/webrtc/1/"

    @staticmethod
    def validate_path_parameter(
        parameter: Union[PathParameter, Dict], parameter_type: Type[PathParameter]
    ) -> PathParameter:
        """
        Validate path parameter by trying to instantiate the provided class and
        extract valid path parameter.

        :param parameter: Path parameter to validate
        :param parameter_type: Type of path parameter
        :return: Class instance corresponding to the provided parameter type
        """
        return (
            parameter
            if isinstance(parameter, parameter_type)
            else parameter_type(**parameter)
        )

    def _get_custom_response_class(
        self,
        response: Union[requests.Response, Any],
        response_ok_model: Type[ResponseBase] = WebRtcResponseOK,
        *args,
        **kwargs
    ) -> Type[ResponseBase]:

        if response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
            return response_ok_model

        elif response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.TOO_MANY_REQUESTS,
        ):
            return WebRtcResponseError

        raise ValueError
