from pytest_cases import parametrize

from tests.app_entities.conftest import get_get_entities_response
from tests.conftest import get_expected_get_headers

ENDPOINT_TEST_ARGUMENTS = {
    "get_entities": {
        "endpoint": "/provisioning/1/entities",
        "http_method": "GET",
        "expected_headers": get_expected_get_headers(),
        "expected_path_parameters": None,
        "expected_query_parameters": {"page": "0", "size": "10"},
        "expected_json": None,
        "request_parameters": None,
        "method_name": "get_entities",
    },
}


@parametrize(
    endpoint_type=ENDPOINT_TEST_ARGUMENTS.keys(),
    responses=([200, get_get_entities_response],),
)
def case__supported_status(endpoint_type, responses):
    status_code = responses[0]
    response_content = responses[1]

    if endpoint_type == "get_entities" and responses[0] == 200:
        response_content = get_get_entities_response

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
