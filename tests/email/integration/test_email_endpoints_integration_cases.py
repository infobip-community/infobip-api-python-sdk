from pytest_cases import parametrize

from tests.conftest import get_expected_get_headers, get_expected_post_headers
from tests.email.conftest import (
    get_email_body_multipart,
    get_email_body_request,
    get_email_delivery_reports_query_parameters,
    get_email_delivery_reports_response,
    get_email_logs_query_parameters,
    get_email_logs_response,
    get_email_request_error_response,
    get_sent_email_bulk_id_query_parameter,
    get_sent_email_bulks_response,
    get_sent_email_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "send_email_message": {
        "response_content": get_sent_email_response(),
        "endpoint": "/email/2/send",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(
            "multipart/form-data; boundary=mockBoundary"
        ),
        "expected_query_parameters": None,
        "expected_data": get_email_body_multipart(),
        "request_data": get_email_body_request(),
        "method_name": "send_email_message",
    },
    "email_delivery_reports": {
        "response_content": get_email_delivery_reports_response(),
        "endpoint": "/email/1/reports",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_query_parameters": "messageId=abc-123&limit=1",
        "expected_data": None,
        "request_data": get_email_delivery_reports_query_parameters(),
        "method_name": "email_delivery_reports",
    },
    "get_email_logs": {
        "response_content": get_email_logs_response(),
        "endpoint": "/email/1/logs",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_query_parameters": "messageId=abc-123&limit=1",
        "expected_data": None,
        "request_data": get_email_logs_query_parameters(),
        "method_name": "get_email_logs",
    },
    "get_sent_email_bulks": {
        "response_content": get_sent_email_bulks_response(),
        "endpoint": "/email/1/bulks",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_query_parameters": "bulkId=xyz-123-444",
        "expected_data": None,
        "request_data": get_sent_email_bulk_id_query_parameter(),
        "method_name": "get_sent_email_bulks",
    },
}


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(), status_code=(200, 400, 500))
def case__supported_status(endpoint_type, status_code):
    if endpoint_type == "send_email_message":
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"]["attachment"].seek(0)
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"]["inlineImage"].seek(0)

    response_content = get_sent_email_response
    if endpoint_type == "email_delivery_reports":
        response_content = get_email_delivery_reports_response
    if endpoint_type == "get_email_logs":
        response_content = get_email_logs_response
    if endpoint_type == "get_sent_email_bulks":
        response_content = get_sent_email_bulks_response
    if status_code == 400 or status_code == 500:
        response_content = get_email_request_error_response

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_data"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys())
def case__unsupported_status(endpoint_type):
    if endpoint_type == "send_email_message":
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"]["attachment"].seek(0)
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"]["inlineImage"].seek(0)

    return (
        201,
        get_email_request_error_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_data"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_data"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
