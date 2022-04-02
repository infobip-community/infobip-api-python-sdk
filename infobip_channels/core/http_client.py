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

    def __init__(
        self,
        auth: Authentication,
        post_headers: RequestHeaders = None,
        get_headers: RequestHeaders = None,
    ):
        """Create an instance of the _HttpClient class with the provided authentication
        model instance. Get and post headers can optionally be provided, otherwise
        default instances will be created for both. These headers will be used as
        defaults in the get and post methods, unless new values are sent through method
        arguments.
        """
        self.auth = auth
        self.post_headers = post_headers or PostHeaders(authorization=self.auth.api_key)
        self.get_headers = get_headers or GetHeaders(authorization=self.auth.api_key)

    def post(
        self, endpoint: str, body: Union[Dict, bytes], headers: RequestHeaders = None
    ) -> requests.Response:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :param headers: Request headers
        :return: Received response
        """
        headers = headers or self.post_headers
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
        headers = headers or self.get_headers
        url = self.auth.base_url + endpoint

        return requests.get(url=url, headers=headers.dict(by_alias=True))
