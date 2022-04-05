from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.webrtc.conftest import (
    GenerateTokenFactory,
    SaveApplicationFactory,
    UpdateApplicationFactory,
    get_expected_path_parameters,
    get_webrtc_application_request,
    get_webrtc_application_response,
    get_webrtc_body_generate_token,
    get_webrtc_generate_token_response,
    get_webrtc_request_error_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "generate_token": {
        "endpoint": "/webrtc/1/token",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateTokenFactory,
        "request_data": get_webrtc_body_generate_token(),
        "method_name": "generate_token",
    },
    "save_application": {
        "endpoint": "/webrtc/1/applications",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": SaveApplicationFactory,
        "request_data": get_webrtc_application_request,
        "method_name": "save_application",
    },
    "update_application": {
        "endpoint": "/webrtc/1/applications/894c822b-d7ba-439c-a761-141f591cace7",
        "http_method": "PUT",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": get_expected_path_parameters(),
        "expected_query_parameters": None,
        "expected_json": UpdateApplicationFactory,
        "request_data": get_webrtc_application_request,
        "method_name": "update_application",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_webrtc_application_response],
        [400, get_webrtc_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "generate_token" and responses[0] == 200:
        response_content = get_webrtc_generate_token_response

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys())
def case__unsupported_status(endpoint_type):

    return (
        201,
        get_webrtc_application_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
