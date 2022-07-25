import json
import string
from io import IOBase
from random import choice
from string import ascii_letters
from typing import Optional

import pytest
import requests
from werkzeug import Response

from infobip_channels.core.models import CamelCaseModel, MultipartMixin


def get_random_string(length: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))


def get_random_numbers(length: int) -> str:
    return "".join(choice(string.digits) for _ in range(length))


class HttpTestClient:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self, endpoint, body, headers=None):
        headers = headers or self.headers
        return requests.post(url=f"{self.url}" + endpoint, json=body, headers=headers)

    def get(self, endpoint, headers=None):
        headers = headers or self.headers
        return requests.get(url=f"{self.url}" + endpoint, headers=headers)

    def delete(self, endpoint, headers=None):
        headers = headers or self.headers
        return requests.delete(url=f"{self.url}" + endpoint, headers=headers)


class Address(CamelCaseModel):
    street: str
    city: str
    zip_code: int


class UserInfo(CamelCaseModel, MultipartMixin):
    name: Optional[str] = None
    last_name: str
    address: Address
    profile_image: IOBase

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True


@pytest.fixture
def http_test_client():
    def _get_http_test_client(url, headers):
        return HttpTestClient(url, headers)

    return _get_http_test_client


def get_response_object(status_code, content):
    return Response(json.dumps(content), status_code)


def get_response_error_invalid_content():
    return {
        "error": {"field_one": "error_one", "field_two": "error_two"},
    }


def get_expected_post_headers(content_type="application/json"):
    return {
        "Authorization": "App secret",
        "Content-Type": content_type,
        "Accept": "application/json",
    }


def get_expected_put_headers(content_type="application/json"):
    return {
        "Authorization": "App secret",
        "Content-Type": content_type,
        "Accept": "application/json",
    }


def get_expected_get_headers():
    return {
        "Authorization": "App secret",
        "Accept": "application/json",
    }


def get_expected_delete_headers():
    return {
        "Authorization": "App secret",
        "Accept": "application/json",
    }
