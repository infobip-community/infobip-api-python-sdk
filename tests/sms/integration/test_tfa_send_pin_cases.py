from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers
from tests.sms.conftest import (
    get_tfa_request_error_response,
    get_send_pin_over_sms_response,
    get_send_pin_over_sms_body,
    GenerateSendPINOverSMSBodyFactoryIntegration,
    GenerateSendPINOverVoiceBodyFactoryIntegration,
    get_send_pin_over_voice_body,
    get_send_pin_over_voice_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "send_pin_over_sms": {
        "endpoint": "/2fa/2/pin",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateSendPINOverSMSBodyFactoryIntegration,
        "request_parameters": get_send_pin_over_sms_body(),
        "method_name": "send_pin_over_sms",
    },
    "send_pin_over_voice": {
        "endpoint": "/2fa/2/pin/voice",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": None,
        "expected_json": GenerateSendPINOverVoiceBodyFactoryIntegration,
        "request_parameters": get_send_pin_over_voice_body(),
        "method_name": "send_pin_over_voice",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [200, get_send_pin_over_sms_response],
        [200, get_send_pin_over_voice_response],
        [400, get_tfa_request_error_response],
    ),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "send_pin_over_sms" and responses[0] == 200:
        response_content = get_send_pin_over_sms_response
    elif endpoint_type == "send_pin_over_voice" and responses[0] == 200:
        response_content = get_send_pin_over_voice_response

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
