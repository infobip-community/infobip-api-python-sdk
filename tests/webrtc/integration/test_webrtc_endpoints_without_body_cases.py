from pytest_cases import parametrize

from tests.conftest import get_expected_delete_headers, get_expected_get_headers
from tests.webrtc.conftest import (
    get_expected_path_parameters,
    get_webrtc_application_response,
    get_webrtc_delete_request,
    get_webrtc_get_applications_response,
    get_webrtc_request_error_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "get_webrtc_applications": {
        "endpoint": "/webrtc/1/applications",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "method_name": "get_applications",
    },
    "get_webrtc_application": {
        "endpoint": "/webrtc/1/applications/894c822b-d7ba-439c-a761-141f591cace7",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": get_expected_path_parameters(),
        "expected_query_parameters": None,
        "method_name": "get_application",
    },
    "delete_webrtc_application": {
        "endpoint": "/webrtc/1/applications/894c822b-d7ba-439c-a761-141f591cace7",
        "http_method": "DELETE",
        "expected_headers": get_expected_delete_headers(),
        "expected_path_parameters": get_expected_path_parameters(),
        "expected_query_parameters": None,
        "method_name": "delete_application",
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

    if endpoint_type == "get_webrtc_applications" and responses[0] == 200:
        response_content = get_webrtc_get_applications_response
    if endpoint_type == "delete_webrtc_application" and responses[0] == 200:
        response_content = get_webrtc_delete_request

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
)
def case__unsupported_status(endpoint_type):
    return (
        201,
        get_webrtc_application_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
