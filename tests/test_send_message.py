from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from whatsapp.client import WhatsAppChannel
from whatsapp.models.core import WhatsAppResponse


@parametrize_with_cases(
    "endpoint, message_body_factory, method_name, raw_response_fixture, status_code, "
    "response_content",
    prefix="from_provided_client",
)
def test_send_message_from_provided_client__returns_raw_response(
    httpserver,
    http_test_client,
    endpoint,
    message_body_factory,
    method_name,
    raw_response_fixture,
    status_code,
    response_content,
    get_expected_headers,
):
    expected_headers = get_expected_headers("secret")
    message_body = message_body_factory.build()

    httpserver.expect_request(
        endpoint,
        method="POST",
        json=message_body.dict(by_alias=True),
        headers=expected_headers,
    ).respond_with_response(raw_response_fixture(status_code))

    whatsapp_client = WhatsAppChannel.from_provided_client(
        http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_request_headers("secret"),
        )
    )
    response = getattr(whatsapp_client, method_name)(message_body)

    assert isinstance(response, WhatsAppResponse) is False
    assert response.status_code == status_code
    assert response.json() == response_content


@parametrize_with_cases(
    "endpoint, message_body_factory, method_name, raw_response_fixture, status_code, "
    "response_content",
    prefix="from_auth_params",
)
def test_send_message_from_auth_params__returns_whatsapp_response(
    httpserver,
    endpoint,
    message_body_factory,
    method_name,
    raw_response_fixture,
    status_code,
    response_content,
    get_expected_headers,
):
    expected_headers = get_expected_headers("secret")
    message_body = message_body_factory.build()

    httpserver.expect_request(
        endpoint,
        method="POST",
        json=message_body.dict(by_alias=True),
        headers=expected_headers,
    ).respond_with_response(raw_response_fixture(status_code))

    server_url = httpserver.url_for("/")
    whatsapp_client = WhatsAppChannel.from_auth_params(
        {"base_url": server_url, "api_key": "secret"}
    )
    response = getattr(whatsapp_client, method_name)(message_body)
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
