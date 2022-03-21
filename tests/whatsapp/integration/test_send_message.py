from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.channel import WhatsAppChannel
from tests.whatsapp.conftest import (
    get_response_object,
    get_response_object_unofficial,
    get_whatsapp_channel_instance,
)


def send_message_request(
    factory,
    http_server,
    endpoint,
    headers,
    response,
    instantiation_type,
    message_body_type,
    method_name,
    **kwargs,
):
    message_body_instance = message_body = factory.build()
    http_server.expect_request(
        endpoint,
        method="POST",
        json=message_body_instance.dict(by_alias=True),
        headers=headers,
    ).respond_with_response(response)

    whatsapp_channel = get_whatsapp_channel_instance(instantiation_type, **kwargs)

    if message_body_type == "dict":
        message_body = message_body_instance.dict()

    return getattr(whatsapp_channel, method_name)(message_body)


@parametrize_with_cases(
    "endpoint, message_body_factory, method_name, status_code, "
    "response_content, message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__valid_content",
)
def test_send_message_from_all_instantiation_types_case__valid_content(
    httpserver,
    http_test_client,
    endpoint,
    message_body_factory,
    method_name,
    status_code,
    response_content,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_post_headers,
):

    response = send_message_request(
        factory=message_body_factory,
        http_server=httpserver,
        endpoint=endpoint,
        headers=get_expected_post_headers("secret"),
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        message_body_type=message_body_type,
        method_name=method_name,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_post_request_headers("secret"),
        ),
    )

    response_dict = WhatsAppChannel.convert_model_to_dict(response)
    raw_response = response_dict.pop("rawResponse")
    expected_response_dict = {
        **response_content,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, ResponseBase) is True
    assert response.status_code == status_code
    assert response_dict == expected_response_dict
    assert raw_response is not None


@parametrize_with_cases(
    "endpoint, message_body_factory, method_name, status_code, "
    "response_content, message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__invalid_content",
)
def test_send_message_from_all_instantiation_types_case__invalid_content(
    httpserver,
    http_test_client,
    http_test_client_unofficial,
    endpoint,
    message_body_factory,
    method_name,
    status_code,
    response_content,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_post_headers,
):
    if whatsapp_channel_instantiation_type == "client_unofficial":
        client = http_test_client_unofficial
        response_object = get_response_object_unofficial
    else:
        client = http_test_client
        response_object = get_response_object

    response = send_message_request(
        factory=message_body_factory,
        http_server=httpserver,
        endpoint=endpoint,
        headers=get_expected_post_headers("secret"),
        response=response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        message_body_type=message_body_type,
        method_name=method_name,
        server_url=httpserver.url_for("/"),
        client=client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_post_request_headers("secret"),
        ),
    )

    assert isinstance(response, ResponseBase) is False
    assert response is not None

    if whatsapp_channel_instantiation_type != "client_unofficial":
        assert response.status_code == status_code
        assert response.json() == response_content
