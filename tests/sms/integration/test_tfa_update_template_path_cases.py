from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.sms.conftest import (
    get_tfa_request_error_response,
    get_create_tfa_application_response,
    GenerateUpdateTFAMessageTemplateBodyFactoryIntegration,
    get_update_tfa_message_template_body,
    get_update_tfa_application_response,
    get_create_tfa_message_template_response,
    get_update_tfa_message_template_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "update_tfa_message_template": {
        "endpoint": "/2fa/2/applications/1234567890/messages/1234567890",
        "http_method": "PUT",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": {"appId": 1234567890, "msgId": 1234567890},
        "expected_query_parameters": None,
        "expected_json": GenerateUpdateTFAMessageTemplateBodyFactoryIntegration,
        "request_parameters": get_update_tfa_message_template_body(),
        "method_name": "update_tfa_message_template",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_create_tfa_application_response],
        [400, get_tfa_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "create_tfa_application" and responses[0] == 200:
        response_content = get_create_tfa_application_response
    elif endpoint_type == "update_tfa_application" and responses[0] == 200:
        response_content = get_update_tfa_application_response
    elif endpoint_type == "create_tfa_message_template" and responses[0] == 200:
        response_content = get_create_tfa_message_template_response
    elif endpoint_type == "update_tfa_message_template" and responses[0] == 200:
        response_content = get_update_tfa_message_template_response

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
        get_tfa_request_error_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_path_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
