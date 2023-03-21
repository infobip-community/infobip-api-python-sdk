from pytest_cases import parametrize

from tests.app_entities.conftest import (
    GenerateModifyEntityBodyFactoryIntegration,
    get_modify_entity_body,
    get_modify_entity_request_error_response,
    get_modify_entity_response,
)
from tests.conftest import get_expected_post_headers

ENDPOINT_TEST_ARGUMENTS = {
    "modify_entity": {
        "endpoint": "/provisioning/1/entities/some-entity-id",
        "http_method": "PUT",
        "expected_headers": get_expected_post_headers(),
        "expected_path_parameters": {"entityId": "some-entity-id"},
        "expected_query_parameters": None,
        "expected_json": GenerateModifyEntityBodyFactoryIntegration,
        "request_parameters": get_modify_entity_body(),
        "method_name": "modify_entity",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=(
        [204, get_modify_entity_response],
        [400, get_modify_entity_request_error_response],
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
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["request_parameters"],
        ENDPOINT_TEST_ARGUMENTS[endpoint_type]["method_name"],
    )
