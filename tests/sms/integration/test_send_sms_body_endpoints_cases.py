from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.sms.conftest import (
    GenerateBinarySMSMessageBodyFactoryIntegration,
    GeneratePreviewSMSMessageBodyFactory,
    GenerateSMSMessageBodyFactoryIntegration,
    get_preview_send_sms_message_body,
    get_preview_send_sms_response,
    get_send_binary_sms_message_body,
    get_send_sms_message_body,
    get_sms_request_error_response,
    get_sms_request_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "send_SMS_message": {
        "endpoint": "/sms/2/text/advanced",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateSMSMessageBodyFactoryIntegration,
        "request_parameters": get_send_sms_message_body(),
        "method_name": "send_sms_message",
    },
    "send_binary_SMS_message": {
        "endpoint": "/sms/2/binary/advanced",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateBinarySMSMessageBodyFactoryIntegration,
        "request_parameters": get_send_binary_sms_message_body(),
        "method_name": "send_binary_sms_message",
    },
    "preview_SMS_message": {
        "endpoint": "/sms/1/preview",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GeneratePreviewSMSMessageBodyFactory,
        "request_parameters": get_preview_send_sms_message_body(),
        "method_name": "preview_sms_message",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_sms_request_response],
        [400, get_sms_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "preview_SMS_message" and responses[0] == 200:
        response_content = get_preview_send_sms_response

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
