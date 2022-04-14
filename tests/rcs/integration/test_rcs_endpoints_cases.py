from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.rcs.conftest import (
    RcsMessageBodyFactory,
    RcsMessageBodyListFactory,
    get_rcs_body_send_message,
    get_rcs_body_send_bulk_message,
    send_rcs_message_response,
    send_rcs_bulk_message_response,
    rcs_error_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "send_message": {
        "endpoint": "/ott/rcs/1/message",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": RcsMessageBodyFactory,
        "request_data": get_rcs_body_send_message(),
        "method_name": "send_rcs_message",
    },
    "send_bulk_message": {
        "endpoint": "/ott/rcs/1/message/bulk",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": RcsMessageBodyListFactory,
        "request_data": get_rcs_body_send_bulk_message(),
        "method_name": "send_bulk_rcs_message",
    }
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, send_rcs_message_response],
        [400, rcs_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "send_bulk_message" and responses[0] == 200:
        response_content = send_rcs_bulk_message_response

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
        send_rcs_message_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
