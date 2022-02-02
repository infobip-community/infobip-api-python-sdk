from http import HTTPStatus

import requests

from whatsapp.core.models import Response, ResponseError, ResponseOK


class ApiException(Exception):
    pass


ERROR_STATUSES = (
    HTTPStatus.BAD_REQUEST,
    HTTPStatus.UNAUTHORIZED,
    HTTPStatus.TOO_MANY_REQUESTS,
)


def construct_response_model(response: requests.Response) -> Response:
    response_body = {
        "status_code": response.status_code,
        "raw_response": response,
        **response.json(),
    }

    if response.status_code == HTTPStatus.OK:
        return ResponseOK(**response_body)

    elif response.status_code in ERROR_STATUSES:
        return ResponseError(**response_body)

    raise ApiException("Unexpected status code received")
