from pytest_cases import parametrize

from tests.conftest import get_expected_post_headers, get_expected_put_headers
from tests.email.conftest import (
    AddNewDomainFactory,
    GenerateRescheduleEmailMessagesFactory,
    GenerateUpdateScheduledEmailMessagesStatusFactory,
    ValidateEmailAddressesFactory,
    get_add_new_domain_response,
    get_email_request_error_response,
    get_reschedule_email_messages_response,
    get_sent_email_bulk_id_query_parameter,
    get_update_scheduled_email_messages_status_response,
    get_validate_email_addresses_response,
)

ENDPOINT_TEST_ARGUMENTS = {
    "reschedule_email_messages": {
        "response_content": get_reschedule_email_messages_response(),
        "endpoint": "/email/1/bulks",
        "http_method": "PUT",
        "expected_headers": get_expected_put_headers(),
        "expected_query_parameters": "bulkId=xyz-123-444",
        "expected_json": GenerateRescheduleEmailMessagesFactory,
        "request_query_parameters": get_sent_email_bulk_id_query_parameter(),
        "method_name": "reschedule_email_messages",
    },
    "update_scheduled_email_messages": {
        "response_content": get_update_scheduled_email_messages_status_response(),
        "endpoint": "/email/1/bulks/status",
        "http_method": "PUT",
        "expected_headers": get_expected_put_headers(),
        "expected_query_parameters": "bulkId=xyz-123-444",
        "expected_json": GenerateUpdateScheduledEmailMessagesStatusFactory,
        "request_query_parameters": get_sent_email_bulk_id_query_parameter(),
        "method_name": "update_scheduled_email_messages",
    },
    "validate_email_addresses": {
        "response_content": get_validate_email_addresses_response(),
        "endpoint": "/email/2/validation",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_query_parameters": None,
        "expected_json": ValidateEmailAddressesFactory,
        "request_query_parameters": None,
        "method_name": "validate_email_addresses",
    },
    "add_new_domain": {
        "response_content": get_add_new_domain_response(),
        "endpoint": "/email/1/domains",
        "http_method": "POST",
        "expected_headers": get_expected_post_headers(),
        "expected_query_parameters": None,
        "expected_json": AddNewDomainFactory,
        "request_query_parameters": None,
        "method_name": "add_new_domain",
    },
}


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(), status_code=(200, 400, 500))
def case__supported_status(endpoint_type, status_code):
    response_content = get_reschedule_email_messages_response
    if endpoint_type == "update_scheduled_email_messages":
        response_content = get_update_scheduled_email_messages_status_response
    if endpoint_type == "validate_email_addresses":
        response_content = get_validate_email_addresses_response
    if endpoint_type == "add_new_domain":
        response_content = get_add_new_domain_response
    if status_code == 400 or status_code == 500:
        response_content = get_email_request_error_response

    return (
        status_code,
        response_content(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )


@parametrize(endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys())
def case__unsupported_status(endpoint_type):
    return (
        201,
        get_email_request_error_response(),
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["endpoint"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["http_method"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_headers"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["expected_json"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_query_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
