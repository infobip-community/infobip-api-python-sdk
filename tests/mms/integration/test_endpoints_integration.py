from http import HTTPStatus
from unittest.mock import patch

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.mms.channel import MMSChannel
from tests.conftest import get_response_object


def set_up_mock_server_and_send_request(
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_data,
    request_data,
    method_name,
):
    httpserver.expect_request(
        endpoint,
        method=http_method,
        query_string=expected_query_parameters,
        headers=expected_headers,
        data=expected_data,
    ).respond_with_response(get_response_object(status_code, response_content))

    mms_channel = MMSChannel.from_auth_params(
        {"base_url": httpserver.url_for("/"), "api_key": "secret"}
    )

    return getattr(mms_channel, method_name)(request_data)


@patch("urllib3.filepost.choose_boundary", return_value="mockBoundary")
@parametrize_with_cases(
    "status_code, response_content, endpoint, http_method, expected_headers, "
    "expected_query_parameters, expected_data, request_data, method_name",
    prefix="case__supported_status",
)
def test_get_mms_delivery_reports__supported_status(
    mock_boundary,
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_data,
    request_data,
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
        expected_data,
        request_data,
        method_name,
    )
    response_dict = MMSChannel.convert_model_to_dict(response)
    raw_response = response_dict.pop("rawResponse")
    expected_response_dict = {
        **response_content,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, ResponseBase) is True
    assert response.status_code == status_code
    assert response_dict == expected_response_dict
    assert raw_response is not None


@patch("urllib3.filepost.choose_boundary", return_value="mockBoundary")
@parametrize_with_cases(
    "status_code, response_content, endpoint, http_method, expected_headers, "
    "expected_query_parameters, expected_data, request_data, method_name",
    prefix="case__unsupported_status",
)
def test_get_mms_delivery_reports__unsupported_status(
    mock_boundary,
    httpserver,
    status_code,
    response_content,
    endpoint,
    http_method,
    expected_headers,
    expected_query_parameters,
    expected_data,
    request_data,
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
        expected_data,
        request_data,
        method_name,
    )
    assert isinstance(response, ResponseBase) is False
    assert response is not None
    assert response.status_code == status_code
    assert response.json() == response_content
