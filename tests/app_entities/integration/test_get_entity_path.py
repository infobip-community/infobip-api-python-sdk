from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_platform.app_entities.api import ApplicationEntityManagement
from tests.conftest import get_response_object


def set_up_mock_server_and_send_request(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_path_parameters,
    expected_query_parameters,
    expected_json,
    request_parameters,
    method_name,
):
    httpserver.expect_request(
        endpoint,
        method=http_method,
        query_string=expected_query_parameters,
        headers=expected_headers,
    ).respond_with_response(get_response_object(status_code, response_content))

    app_entity_mgmt = ApplicationEntityManagement.from_auth_params(
        {"base_url": httpserver.url_for("/"), "api_key": "secret"}
    )

    return getattr(app_entity_mgmt, method_name)(expected_path_parameters["entityId"])


@parametrize_with_cases(
    "status_code, response_content, endpoint, http_method, expected_headers, "
    "expected_path_parameters, expected_query_parameters, expected_json, "
    "request_parameters, method_name",
    prefix="case__supported_status",
)
def test_entity_endpoints__supported_status(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_path_parameters,
    expected_query_parameters,
    expected_json,
    request_parameters,
    method_name,
):
    response = set_up_mock_server_and_send_request(
        httpserver,
        status_code,
        response_content,
        endpoint,
        http_method,
        expected_headers,
        expected_path_parameters,
        expected_query_parameters,
        expected_json,
        request_parameters,
        method_name,
    )
    response_dict = ApplicationEntityManagement.convert_model_to_dict(response)
    raw_response = response_dict.pop("rawResponse")

    if type(response_content) is list:
        response_content = {"list": response_content}
    else:
        response_content = response_content

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
    "expected_path_parameters, expected_query_parameters, expected_json, "
    "request_parameters, method_name",
    prefix="case__unsupported_status",
)
def test_entity_endpoints__unsupported_status(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_path_parameters,
    expected_query_parameters,
    expected_json,
    request_parameters,
    method_name,
):
    response = set_up_mock_server_and_send_request(
        httpserver,
        status_code,
        response_content,
        endpoint,
        http_method,
        expected_headers,
        expected_path_parameters,
        expected_query_parameters,
        expected_json,
        request_parameters,
        method_name,
    )
    assert isinstance(response, ResponseBase) is False
    assert response is not None
    assert response.status_code == status_code
    assert response.json() == response_content
