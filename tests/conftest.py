import json
from random import choice
from string import ascii_letters

import pytest
import requests
from pydantic_factories import ModelFactory
from werkzeug.wrappers.response import Response

from infobip_channels.whatsapp.models.body.audio_message import AudioMessageBody
from infobip_channels.whatsapp.models.body.buttons_message import ButtonsMessageBody
from infobip_channels.whatsapp.models.body.contact_message import ContactMessageBody
from infobip_channels.whatsapp.models.body.create_template import CreateTemplate
from infobip_channels.whatsapp.models.body.document_message import DocumentMessageBody
from infobip_channels.whatsapp.models.body.image_message import ImageMessageBody
from infobip_channels.whatsapp.models.body.list_message import ListMessageBody
from infobip_channels.whatsapp.models.body.location_message import LocationMessageBody
from infobip_channels.whatsapp.models.body.multi_product_message import (
    MultiProductMessageBody,
)
from infobip_channels.whatsapp.models.body.product_message import ProductMessageBody
from infobip_channels.whatsapp.models.body.sticker_message import StickerMessageBody
from infobip_channels.whatsapp.models.body.template_message import TemplateMessageBody
from infobip_channels.whatsapp.models.body.text_message import TextMessageBody
from infobip_channels.whatsapp.models.body.video_message import VideoMessageBody
from infobip_channels.whatsapp.models.path_parameters.get_templates import (
    GetTemplatesPathParameters,
)
from infobip_channels.whatsapp.models.response.core import Authentication


def get_random_string(length: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))


class AuthenticationFactory(ModelFactory):
    __model__ = Authentication


class TextMessageBodyFactory(ModelFactory):
    __model__ = TextMessageBody


class DocumentMessageBodyFactory(ModelFactory):
    __model__ = DocumentMessageBody


class AudioMessageBodyFactory(ModelFactory):
    __model__ = AudioMessageBody


class ImageMessageBodyFactory(ModelFactory):
    __model__ = ImageMessageBody


class StickerMessageBodyFactory(ModelFactory):
    __model__ = StickerMessageBody


class VideoMessageBodyFactory(ModelFactory):
    __model__ = VideoMessageBody


class LocationMessageBodyFactory(ModelFactory):
    __model__ = LocationMessageBody


class ContactMessageBodyFactory(ModelFactory):
    __model__ = ContactMessageBody


class ButtonsMessageBodyFactory(ModelFactory):
    __model__ = ButtonsMessageBody


class ListMessageBodyFactory(ModelFactory):
    __model__ = ListMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "body": {"text": "Body text"},
                    "action": {
                        "title": "Action title",
                        "sections": [
                            {
                                "title": "section title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": "row title",
                                        "description": "row description",
                                    }
                                ],
                            },
                            {
                                "title": "section title 2",
                                "rows": [
                                    {
                                        "id": "2",
                                        "title": "row title 2",
                                        "description": "row description 2",
                                    }
                                ],
                            },
                        ],
                    },
                    "header": {"type": "TEXT", "text": "header text"},
                    "footer": {"text": "footer text"},
                },
            }
        )


class TemplateMessageBodyFactory(ModelFactory):
    __model__ = TemplateMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because pydantic_factories can't handle regex patterns."""
        return TemplateMessageBody(
            **{
                "messages": [
                    {
                        "from": "441134960000",
                        "to": "38595671032",
                        "content": {
                            "template_name": "template_name",
                            "template_data": {
                                "body": {"placeholders": ["value 1", "value 2"]},
                                "header": {
                                    "type": "VIDEO",
                                    "media_url": "https://video.com",
                                },
                                "buttons": [
                                    {"type": "QUICK_REPLY", "parameter": "button 1"},
                                ],
                            },
                            "language": "en",
                        },
                    },
                ],
            }
        )


class ProductMessageBodyFactory(ModelFactory):
    __model__ = ProductMessageBody


class MultiProductMessageBodyFactory(ModelFactory):
    __model__ = MultiProductMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return MultiProductMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "header": {"type": "TEXT", "text": "Some text"},
                    "body": {"text": "Some text"},
                    "action": {
                        "catalogId": "1",
                        "sections": [
                            {
                                "title": "Title",
                                "productRetailerIds": ["id 2"],
                            },
                            {
                                "title": "Title 2",
                                "productRetailerIds": ["id 2", "id 3"],
                            },
                        ],
                    },
                },
            }
        )


class CreateTemplateBodyFactory(ModelFactory):
    __model__ = CreateTemplate


class CreateTemplatesPathParametersFactory(ModelFactory):
    __model__ = GetTemplatesPathParameters


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


def get_response_ok_content():
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


def get_template_message_response_ok_content():
    return {
        "messages": [
            {
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
            },
            {
                "to": "441631451112",
                "messageCount": 1,
                "messageId": "a2ga3hgc-sa7n-1ach-0df1-9b55aeb3a1na",
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 7,
                    "name": "PENDING_ENROUTE",
                    "description": "Message sent to next instance",
                },
            },
        ],
        "bulkId": "2034072219640523073",
    }


def get_response_ok_invalid_content():
    return {
        "to": "441134960001",
        "messageCount": 1,
        "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
    }


def get_response_object(status_code, content):
    return Response(json.dumps(content), status=status_code)


def get_response_error_content():
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


def get_response_error_invalid_content():
    return {
        "error": {"field_one": "error_one", "field_two": "error_two"},
    }


@pytest.fixture
def get_expected_headers():
    def _get_expected_headers(api_key):
        return {
            "Authorization": f"App {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    return _get_expected_headers
