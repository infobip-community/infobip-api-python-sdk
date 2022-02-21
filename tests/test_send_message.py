from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.whatsapp.client import WhatsAppChannel
from infobip_channels.whatsapp.models.core import Authentication, WhatsAppResponse


def get_whatsapp_channel_instance(instantiation_type, **kwargs):
    if instantiation_type == "auth_params":
        return WhatsAppChannel.from_auth_params(
            {"base_url": kwargs["server_url"], "api_key": "secret"}
        )

    elif instantiation_type == "auth_instance":
        return WhatsAppChannel.from_auth_instance(
            Authentication(base_url=kwargs["server_url"], api_key="secret")
        )

    return WhatsAppChannel.from_provided_client(kwargs["client"])


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
    "endpoint, message_body_factory, method_name, get_response_object, status_code, "
    "response_content, message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__valid_content",
)
def test_send_message_from_all_instantiation_types_case__valid_content(
    httpserver,
    http_test_client,
    endpoint,
    message_body_factory,
    method_name,
    get_response_object,
    status_code,
    response_content,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_headers,
):

    response = send_message_request(
        factory=message_body_factory,
        http_server=httpserver,
        endpoint=endpoint,
        headers=get_expected_headers("secret"),
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        message_body_type=message_body_type,
        method_name=method_name,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_request_headers("secret"),
        ),
    )

    response_dict_cleaned = response.dict(by_alias=True, exclude_unset=True)
    raw_response = response_dict_cleaned.pop("rawResponse")
    expected_response_dict = {
        **response_content,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, WhatsAppResponse) is True
    assert response.status_code == status_code
    assert response_dict_cleaned == expected_response_dict
    assert raw_response is not None


@parametrize_with_cases(
    "endpoint, message_body_factory, method_name, get_response_object, status_code, "
    "response_content, message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__invalid_content",
)
def test_send_message_from_all_instantiation_types_case__invalid_content(
    httpserver,
    http_test_client,
    endpoint,
    message_body_factory,
    method_name,
    get_response_object,
    status_code,
    response_content,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_headers,
):
    response = send_message_request(
        factory=message_body_factory,
        http_server=httpserver,
        endpoint=endpoint,
        headers=get_expected_headers("secret"),
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        message_body_type=message_body_type,
        method_name=method_name,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_request_headers("secret"),
        ),
    )

    assert isinstance(response, WhatsAppResponse) is False
    assert response.status_code == status_code
    assert response.json() == response_content
