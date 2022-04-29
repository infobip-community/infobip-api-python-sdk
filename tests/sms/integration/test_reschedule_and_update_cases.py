from pytest_cases import parametrize

from tests.conftest import get_expected_put_headers
from tests.sms.conftest import (
    GenerateRescheduleSMSMessagesFactory,
    get_reschedule_sms_messages_query_parameters,
    get_scheduled_sms_messages_response,
    get_sms_request_error_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "reschedule_sms_messages": {
        "endpoint": "/sms/1/bulks",
        "http_method": "PUT",
        "expected_headers": get_expected_put_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": "bulkId=35122736310703571952",
        "expected_json": GenerateRescheduleSMSMessagesFactory,
        "request_query_parameters": get_reschedule_sms_messages_query_parameters(),
        "method_name": "reschedule_sms_messages",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_scheduled_sms_messages_response],
        [400, get_sms_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_query_parameters"],
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
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
