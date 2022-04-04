from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.webrtc.conftest import (
    GenerateTokenFactory,
    get_webrtc_body_generate_token,
    get_webrtc_generate_token_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "generate_token": {
        "response_content": get_webrtc_generate_token_response(),
        "endpoint": "/webrtc/1/token",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_query_parameters": None,
        "expected_json": GenerateTokenFactory,
        "request_data": get_webrtc_body_generate_token(),
        "method_name": "generate_token",
    }
}


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(), status_code=(200, 400, 500))
def case__supported_status(endpoint_type, status_code):
    return (
        status_code,
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["response_content"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
