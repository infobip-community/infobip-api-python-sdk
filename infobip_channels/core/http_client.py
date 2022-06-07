from typing import Dict, Union

import requests

from infobip_channels.core.models import (
    Authentication,
    DeleteHeaders,
    GetHeaders,
    PostHeaders,
    PutHeaders,
    RequestHeaders,
)


class _HttpClient:
    """Default HTTP client used by the Infobip channels for making HTTP requests."""

    def __init__(
        self,
        auth: Authentication,
        post_headers: RequestHeaders = None,
        get_headers: RequestHeaders = None,
        put_headers: RequestHeaders = None,
        delete_headers: RequestHeaders = None,
    ):
        """Create an instance of the _HttpClient class with the provided
        authentication model instance. Headers can optionally be provided, otherwise
        default instances will be created. These headers will be used as defaults in
        the HTTP methods, unless new values are sent through method arguments.
        """
        self.auth = auth
        self.post_headers = post_headers or PostHeaders(authorization=self.auth.api_key)
        self.get_headers = get_headers or GetHeaders(authorization=self.auth.api_key)
        self.put_headers = put_headers or PutHeaders(authorization=self.auth.api_key)
        self.delete_headers = delete_headers or DeleteHeaders(
            authorization=self.auth.api_key
        )

    def post(
        self,
        endpoint: str,
        body: Union[Dict, bytes] = None,
        headers: RequestHeaders = None,
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

    def get(
        self, endpoint: str, headers: RequestHeaders = None, params: Dict = None
    ) -> requests.Response:
        """Send an HTTP get request to base_url + endpoint.
        :param endpoint: Which endpoint to hit
        :param headers: Request headers
        :param params: Dictionary of query parameters
        :return: Received response
        """
        headers = headers or self.get_headers
        url = self.auth.base_url + endpoint

        return requests.get(url=url, headers=headers.dict(by_alias=True), params=params)

    def put(
        self,
        endpoint: str,
        body: Dict,
        headers: RequestHeaders = None,
        params: Dict = None,
    ) -> requests.Response:
        """Send an HTTP put request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param headers: Request headers
        :param body: Body to send with the request
        :param params: Dictionary of query parameters
        :return: Received response
        """
        headers = headers or self.put_headers
        url = self.auth.base_url + endpoint

        return requests.put(
            url=url, json=body, headers=headers.dict(by_alias=True), params=params
        )

    def delete(
        self, endpoint: str, headers: RequestHeaders = None
    ) -> requests.Response:
        """Send an HTTP delete request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param headers: Request headers
        :return: Received response
        """
        headers = headers or self.delete_headers
        url = self.auth.base_url + endpoint

        return requests.delete(url=url, headers=headers.dict(by_alias=True))
