import json
from random import choice
from string import ascii_letters

import pytest
import requests
from pydantic_factories import ModelFactory
from werkzeug.wrappers.response import Response

from whatsapp.models.core import Authentication
from whatsapp.models.document_message import DocumentMessageBody
from whatsapp.models.text_message import TextMessageBody


def get_random_string(length: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))


class AuthenticationFactory(ModelFactory):
    __model__ = Authentication


class TextMessageBodyFactory(ModelFactory):
    __model__ = TextMessageBody


class DocumentMessageBodyFactory(ModelFactory):
    __model__ = DocumentMessageBody


@pytest.fixture
def authentication():
    return AuthenticationFactory.build()


class HttpTestClient:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self, endpoint, body):
        return requests.post(
            url=f"{self.url}" + endpoint, json=body, headers=self.headers
        )


@pytest.fixture
def http_test_client():
    def _get_http_test_client(url, headers):
        return HttpTestClient(url, headers)

    return _get_http_test_client


@pytest.fixture
def response_ok_content():
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
def response_ok_invalid_content():
    return {
        "to": "441134960001",
        "messageCount": 1,
        "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
    }


@pytest.fixture
def get_response_ok(response_ok_content):
    def _get_response_ok(status_code=200, content=response_ok_content):
        return Response(json.dumps(content), status=status_code)

    return _get_response_ok


@pytest.fixture
def response_error_content():
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
def response_error_invalid_content():
    return {
        "error": {"field_one": "error_one", "field_two": "error_two"},
    }


@pytest.fixture
def get_response_error(response_error_content):
    def _get_response_error(status_code=400, content=response_error_content):
        return Response(json.dumps(content), status=status_code)

    return _get_response_error


@pytest.fixture
def get_expected_headers():
    def _get_expected_headers(api_key):
        return {
            "Authorization": f"App {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    return _get_expected_headers
