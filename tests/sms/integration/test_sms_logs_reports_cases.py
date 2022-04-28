from pytest_cases import parametrize

from tests.conftest import get_expected_get_headers
from tests.sms.conftest import (
    get_outbound_sms_delivery_reports_query_parameters,
    get_outbound_sms_delivery_reports_response,
    get_sms_request_error_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "get_outbound_sms_delivery_reports": {
        "endpoint": "/sms/1/reports",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "bulkId=BULK-ID-123-xyz&messageId=MESSAGE-ID-123"
        "-xyz&limit=1",
        "expected_json": None,
        "request_parameters": get_outbound_sms_delivery_reports_query_parameters(),
        "method_name": "get_outbound_sms_delivery_reports",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_outbound_sms_delivery_reports_response],
        [400, get_sms_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    # if endpoint_type == "preview_SMS_message" and responses[0] == 200:
    #     response_content = get_preview_send_sms_response

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys())
def case__unsupported_status(endpoint_type):

    return (
        201,
        get_sms_request_error_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
