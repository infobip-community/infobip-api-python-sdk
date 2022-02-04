from http import HTTPStatus
from typing import Union

import requests

from whatsapp.models.core import (
    WhatsappResponse,
    WhatsappResponseError,
    WhatsappResponseOK,
)

ERROR_STATUSES = (
    HTTPStatus.BAD_REQUEST,
    HTTPStatus.UNAUTHORIZED,
    HTTPStatus.TOO_MANY_REQUESTS,
)


def construct_response(
    response: requests.Response,
) -> Union[WhatsappResponse, requests.Response]:
    """Return WhatsappResponse if the status code has expected value, else return the
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
        return WhatsappResponseOK(**response_body)

    elif response.status_code in ERROR_STATUSES:
        return WhatsappResponseError(**response_body)

    return response
