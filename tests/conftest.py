from random import choice
from string import ascii_letters

import pytest
import requests
from pydantic_factories import ModelFactory

from whatsapp.models.core import Authentication


def get_random_string(length: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))


class AuthenticationFactory(ModelFactory):
    __model__ = Authentication


@pytest.fixture
def authentication():
    return AuthenticationFactory.build()


class HttpTestClient:
    def __init__(self, url):
        self.url = url

    def post(self, endpoint, body):
        return requests.post(url=f"{self.url}" + endpoint, json=body)


@pytest.fixture
def http_test_client():
    def _get_http_test_client(url):
        return HttpTestClient(url)

    return _get_http_test_client


@pytest.fixture
def bad_request_response():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "BAD_REQUEST",
                "text": "Bad request",
                "validationErrors": {
                    "content.text": [
                        "size must be between 1 and 4096",
                        "must not be blank",
                    ]
                },
            }
        }
    }
