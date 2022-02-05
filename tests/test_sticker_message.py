from http import HTTPStatus

import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from tests.conftest import get_random_string
from whatsapp.client import WhatsAppChannel
from whatsapp.models.core import (
    MessageBody,
    WhatsAppResponse,
    WhatsAppResponseError,
    WhatsAppResponseOK,
)
from whatsapp.models.sticker_message import StickerMessageBody

IMAGE_MESSAGE_ENDPOINT = "/whatsapp/1/message/sticker"


class StickerMessageBodyFactory(ModelFactory):
    __model__ = StickerMessageBody


def test_sticker_message_body__is_an_instance_of_message_body():
    assert isinstance(StickerMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        StickerMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("media_url", [None, "", {}, get_random_string(4097)])
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        StickerMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


def test_send_sticker_message_with_provided_client__returns_raw_response(
    httpserver, http_test_client, ok_content, response_ok
):
    httpserver.expect_request(
        IMAGE_MESSAGE_ENDPOINT, method="POST"
    ).respond_with_response(response_ok)

    whatsapp_client = WhatsAppChannel.from_provided_client(
        http_test_client(httpserver.url_for("/"))
    )
    response = whatsapp_client.send_sticker_message(StickerMessageBodyFactory.build())

    assert isinstance(response, WhatsAppResponse) is False
    assert response.status_code == 200
    assert response.json() == ok_content


@pytest.mark.parametrize(
    "raw_response,response_object,status_code,response_body",
    [
        ("response_ok", WhatsAppResponseOK, 200, "ok_content"),
        ("response_bad_request", WhatsAppResponseError, 400, "bad_request_content"),
        ("response_unauthorized", WhatsAppResponseError, 401, "unauthorized_content"),
        (
            "response_too_many_requests",
            WhatsAppResponseError,
            429,
            "too_many_requests_content",
        ),
    ],
)
def test_send_sticker_message_with_auth_params__returns_whatsapp_response(
    httpserver,
    http_test_client,
    raw_response,
    response_object,
    status_code,
    response_body,
    request,
):
    raw_response_fixture = request.getfixturevalue(raw_response)
    response_body_fixture = request.getfixturevalue(response_body)

    httpserver.expect_request(
        IMAGE_MESSAGE_ENDPOINT, method="POST"
    ).respond_with_response(raw_response_fixture)

    server_url = httpserver.url_for("/")
    whatsapp_client = WhatsAppChannel.from_auth_params(
        {"base_url": server_url, "api_key": "secret"}
    )
    response = whatsapp_client.send_sticker_message(StickerMessageBodyFactory.build())
    response_dict_cleaned = response.dict(by_alias=True, exclude_unset=True)
    raw_response = response_dict_cleaned.pop("rawResponse")

    expected_response_dict = {
        **response_body_fixture,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, response_object)
    assert response.status_code == status_code
    assert response_dict_cleaned == expected_response_dict
    assert raw_response is not None
