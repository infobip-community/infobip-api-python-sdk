from typing import Dict, Union

import requests

from infobip_channels.core.models import (
    Authentication,
    GetHeaders,
    PostHeaders,
    RequestHeaders,
)


class _HttpClient:
    """Default HTTP client used by the Infobip channels for making HTTP requests."""

    def __init__(self, auth: Authentication):
        self.auth = auth

    def post(
        self, endpoint: str, body: Union[Dict, bytes], headers: RequestHeaders = None
    ) -> requests.Response:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :param headers: Request headers
        :return: Received response
        """
        headers = headers or PostHeaders(authorization=self.auth.api_key)
        url = self.auth.base_url + endpoint

        if isinstance(body, dict):
            kwargs = {"json": body}
        else:
            kwargs = {"data": body}

        return requests.post(url=url, headers=headers.dict(by_alias=True), **kwargs)

    def get(self, endpoint: str, headers: RequestHeaders = None) -> requests.Response:
        """Send an HTTP get request to base_url + endpoint.
        :param endpoint: Which endpoint to hit
        :param headers: Request headers
        :return: Received response
        """
        headers = headers or GetHeaders(authorization=self.auth.api_key)
        url = self.auth.base_url + endpoint

        return requests.get(url=url, headers=headers.dict(by_alias=True))

    def put(self, endpoint: str, body: Dict) -> requests.Response:
        """Send an HTTP put request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        return requests.put(
            url=url, json=body, headers=self.get_headers.dict(by_alias=True)
        )

    def delete(self, endpoint: str) -> requests.Response:
        """Send an HTTP delete request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        return requests.delete(url=url, headers=self.get_headers.dict(by_alias=True))
