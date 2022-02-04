import json
from random import choice
from string import ascii_letters

import pytest
import requests
from pydantic_factories import ModelFactory
from werkzeug.wrappers.response import Response

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
def ok_content():
    return {
        "to": "441134960001",
        "messageCount": 1,
        "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
        "status": {
            "groupId": 1,
            "groupName": "PENDING",
            "id": 7,
            "name": "PENDING_ENROUTE",
            "description": "Message sent to next instance",
        },
    }


@pytest.fixture
def response_ok(ok_content):
    return Response(json.dumps(ok_content), status=200)


@pytest.fixture
def bad_request_content():
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


@pytest.fixture
def response_bad_request(bad_request_content):
    return Response(json.dumps(bad_request_content), status=400)


@pytest.fixture
def unauthorized_content():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "UNAUTHORIZED",
                "text": "Invalid login details",
            }
        }
    }


@pytest.fixture
def response_unauthorized(unauthorized_content):
    return Response(json.dumps(unauthorized_content), status=401)


@pytest.fixture
def too_many_requests_content():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "TOO_MANY_REQUESTS",
                "text": "Too many requests",
            }
        }
    }


@pytest.fixture
def response_too_many_requests(too_many_requests_content):
    return Response(json.dumps(too_many_requests_content), status=429)
