from typing import Dict

import requests

from infobip_channels.core.models import Authentication, GetHeaders, PostHeaders


class _HttpClient:
    """Default HTTP client used by the WhatsAppChannel for making HTTP requests."""

    def __init__(self, auth: Authentication):
        self.auth = auth
        self.post_headers = PostHeaders(authorization=self.auth.api_key)
        self.get_headers = GetHeaders(authorization=self.auth.api_key)

    def post(self, endpoint: str, body: Dict) -> requests.Response:
        """Send an HTTP post request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :param body: Body to send with the request
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        return requests.post(
            url=url, json=body, headers=self.post_headers.dict(by_alias=True)
        )

    def get(self, endpoint: str) -> requests.Response:
        """Send an HTTP get request to base_url + endpoint.

        :param endpoint: Which endpoint to hit
        :return: Received response
        """
        url = self.auth.base_url + endpoint
        return requests.get(url=url, headers=self.get_headers.dict(by_alias=True))
