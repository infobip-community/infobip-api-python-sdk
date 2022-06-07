from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.email.channel import EmailChannel
from tests.conftest import get_response_object


def set_up_mock_server_and_send_request(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_json,
    request_query_parameters,
    method_name,
):
    message_body_instance = message_body = expected_json.build()
    httpserver.expect_request(
        endpoint,
        method=http_method,
        query_string=expected_query_parameters,
        headers=expected_headers,
        json=message_body_instance.dict(by_alias=True),
    ).respond_with_response(get_response_object(status_code, response_content))

    email_channel = EmailChannel.from_auth_params(
        {"base_url": httpserver.url_for("/"), "api_key": "secret"}
    )
    if request_query_parameters is None:
        return getattr(email_channel, method_name)(message_body)
    else:
        return getattr(email_channel, method_name)(
            request_query_parameters, message_body
        )


@parametrize_with_cases(
    "status_code, response_content, endpoint, http_method, expected_headers, "
    "expected_query_parameters, expected_json, "
    "request_query_parameters, method_name",
    prefix="case__supported_status",
)
def test_sms_endpoints__supported_status(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_json,
    request_query_parameters,
    method_name,
):

    response = set_up_mock_server_and_send_request(
        httpserver,
        status_code,
        response_content,
        endpoint,
        http_method,
        expected_headers,
        expected_query_parameters,
        expected_json,
        request_query_parameters,
        method_name,
    )
    response_dict = EmailChannel.convert_model_to_dict(response)
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
    "status_code, response_content, endpoint, http_method, expected_headers, "
    "expected_query_parameters, expected_json, "
    "request_query_parameters, method_name",
    prefix="case__unsupported_status",
)
def test_sms_endpoints__unsupported_status(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_json,
    request_query_parameters,
    method_name,
):

    response = set_up_mock_server_and_send_request(
        httpserver,
        status_code,
        response_content,
        endpoint,
        http_method,
        expected_headers,
        expected_query_parameters,
        expected_json,
        request_query_parameters,
        method_name,
    )
    assert isinstance(response, ResponseBase) is False
    assert response is not None
    assert response.status_code == status_code
    assert response.json() == response_content
