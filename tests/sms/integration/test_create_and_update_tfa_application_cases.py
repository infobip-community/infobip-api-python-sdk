from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.sms.conftest import (
    GenerateCreateTFAApplicationBodyFactoryIntegration, get_create_tfa_application_body,
    GenerateUpdateTFAApplicationBodyFactoryIntegration, get_update_tfa_application_body,
    get_tfa_request_error_response, get_create_tfa_application_response)

ENDPOINT_TEST_ARGUMENTS = {
    "create_tfa_application": {
        "endpoint": "/2fa/2/applications",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateCreateTFAApplicationBodyFactoryIntegration,
        "request_parameters": get_create_tfa_application_body(),
        "method_name": "create_tfa_application",
    },
    "update_tfa_application": {
        "endpoint": "/2fa/2/applications/{appId}",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": "1234567890",
        "expected_query_parameters": None,
        "expected_json": GenerateUpdateTFAApplicationBodyFactoryIntegration,
        "request_parameters": get_update_tfa_application_body(),
        "method_name": "update_tfa_application",
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
        response_content = get_create_tfa_application_response()

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
