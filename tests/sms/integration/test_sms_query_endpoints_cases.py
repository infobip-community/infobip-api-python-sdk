from pytest_cases import parametrize

from tests.conftest import get_expected_get_headers
from tests.sms.conftest import (
    get_inbound_sms_messages_query_parameters,
    get_inbound_sms_messages_response,
    get_outbound_sms_delivery_reports_query_parameters,
    get_outbound_sms_delivery_reports_response,
    get_outbound_sms_message_logs_query_parameters,
    get_outbound_sms_message_logs_response,
    get_scheduled_sms_messages,
    get_scheduled_sms_messages_response,
    get_sms_request_error_response,
    get_sms_request_response,
    get_sms_send_message_over_query_parameters,
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
    "get_outbound_sms_message_logs": {
        "endpoint": "/sms/1/logs",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "from=41793026999&to=41793026727&bulkId=BULK-ID"
        "-123-xyz",
        "expected_json": None,
        "request_parameters": get_outbound_sms_message_logs_query_parameters(),
        "method_name": "get_outbound_sms_message_logs",
    },
    "get_inbound_sms_messages": {
        "endpoint": "/sms/1/inbox/reports",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "limit=2",
        "expected_json": None,
        "request_parameters": get_inbound_sms_messages_query_parameters(),
        "method_name": "get_inbound_sms_messages",
    },
    "send_SMS_message_over_query_parameters": {
        "endpoint": "/sms/1/text/query",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "username=TestUser&password=Pass123&to"
        "=41793026727&flash=False",
        "expected_json": None,
        "request_parameters": get_sms_send_message_over_query_parameters(),
        "method_name": "send_sms_message_over_query_parameters",
    },
    "get_scheduled_sms_messages": {
        "endpoint": "/sms/1/bulks",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "bulkId=BulkId-xyz-123",
        "expected_json": None,
        "request_parameters": get_scheduled_sms_messages(),
        "method_name": "get_scheduled_sms_messages",
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

    if endpoint_type == "get_outbound_sms_message_logs" and responses[0] == 200:
        response_content = get_outbound_sms_message_logs_response
    if endpoint_type == "get_inbound_sms_messages" and responses[0] == 200:
        response_content = get_inbound_sms_messages_response
    if (
        endpoint_type == "send_SMS_message_over_query_parameters"
        and responses[0] == 200
    ):
        response_content = get_sms_request_response
    if endpoint_type == "get_scheduled_sms_messages" and responses[0] == 200:
        response_content = get_scheduled_sms_messages_response

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
