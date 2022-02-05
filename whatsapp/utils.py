from http import HTTPStatus
from typing import Union

import requests

from whatsapp.models.core import (
    WhatsAppResponse,
    WhatsAppResponseError,
    WhatsAppResponseOK,
)

ERROR_STATUSES = (
    HTTPStatus.BAD_REQUEST,
    HTTPStatus.UNAUTHORIZED,
    HTTPStatus.TOO_MANY_REQUESTS,
)


def construct_response(
    response: requests.Response,
) -> Union[WhatsAppResponse, requests.Response]:
    """Return WhatsAppResponse if the status code has expected value, else return the
    raw requests.Response.

    :param response: Response received from the API
    :return: Received response
    """
    response_body = {
        "status_code": response.status_code,
        "raw_response": response,
        **response.json(),
    }

    if response.status_code == HTTPStatus.OK:
        return WhatsAppResponseOK(**response_body)

    elif response.status_code in ERROR_STATUSES:
        return WhatsAppResponseError(**response_body)

    return response
