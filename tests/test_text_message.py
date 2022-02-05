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
from whatsapp.models.text_message import TextMessageBody

TEXT_MESSAGE_ENDPOINT = "/whatsapp/1/message/text"


class TextMessageBodyFactory(ModelFactory):
    __model__ = TextMessageBody


def test_text_message_body__is_an_instance_of_message_body():
    assert isinstance(TextMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(4097)])
def test_when_content_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(**{"content": {"text": text}})


@pytest.mark.parametrize("preview_url", ["", {}])
def test_when_content_preview_url_is_invalid__validation_error_is_raised(preview_url):
    with pytest.raises(ValidationError):
        TextMessageBodyFactory.build(
            **{"content": {"text": "text", "previewUrl": preview_url}}
        )


def test_send_text_message_with_provided_client__returns_raw_response(
    httpserver, http_test_client, ok_content, response_ok
):
    httpserver.expect_request(
        TEXT_MESSAGE_ENDPOINT, method="POST"
    ).respond_with_response(response_ok)

    whatsapp_client = WhatsAppChannel.from_provided_client(
        http_test_client(httpserver.url_for("/"))
    )
    response = whatsapp_client.send_text_message(TextMessageBodyFactory.build())

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
def test_send_text_message_with_auth_params__returns_whatsapp_response(
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
        TEXT_MESSAGE_ENDPOINT, method="POST"
    ).respond_with_response(raw_response_fixture)

    server_url = httpserver.url_for("/")
    whatsapp_client = WhatsAppChannel.from_auth_params(
        {"base_url": server_url, "api_key": "secret"}
    )
    response = whatsapp_client.send_text_message(TextMessageBodyFactory.build())
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
