from pytest_cases import parametrize

from tests.whatsapp.conftest import (
    get_response_error_content,
    get_response_error_invalid_content,
)


def get_response_ok_content():
    return {
        "id": "222",
        "businessAccountId": 333,
        "name": "exampleName",
        "language": "en",
        "status": "APPROVED",
        "category": "ACCOUNT_UPDATE",
        "structure": {
            "header": {"format": "IMAGE"},
            "body": "example {{1}} body",
            "footer": "exampleFooter",
            "type": "MEDIA",
            "buttons": [{"type": "URL", "text": "url", "url": "http://someurl.com"}],
        },
    }


def get_response_ok_invalid_content():
    return {
        "businessAccountId": 222,
        "name": "exampleName",
        "language": "en",
        "status": "APPROVED",
        "category": "ACCOUNT_UPDATE",
        "structure_invalid": {
            "header": {"format": "IMAGE"},
            "body": "example {{1}} body",
            "footer": "exampleFooter",
            "type": "MEDIA",
            "buttons": [{"type": "URL", "text": "url", "url": "http://someurl.com"}],
        },
    }


@parametrize(
    path_parameters_type=("path_parameter_instance", "dict"),
    message_body_type=("message_body_instance", "dict"),
    whatsapp_channel_instantiation_type=("auth_params", "auth_instance", "client"),
    responses=(
        [200, get_response_ok_content()],
        [201, get_response_ok_content()],
        [400, get_response_error_content()],
        [401, get_response_error_content()],
        [403, get_response_error_content()],
        [429, get_response_error_content()],
    ),
)
def from_all_instantiation_types_case__valid_content(
    responses,
    path_parameters_type,
    message_body_type,
    whatsapp_channel_instantiation_type,
):
    return (
        responses[0],
        responses[1],
        path_parameters_type,
        message_body_type,
        whatsapp_channel_instantiation_type,
    )


@parametrize(
    path_parameters_type=("path_parameter_instance", "dict"),
    message_body_type=("message_body_instance", "dict"),
    whatsapp_channel_instantiation_type=(
        "auth_params",
        "auth_instance",
        "client",
        "client_unofficial",
    ),
    responses=(
        [201, get_response_ok_invalid_content()],
        [202, get_response_ok_content()],
        [403, get_response_error_invalid_content()],
        [405, get_response_error_content()],
        [500, get_response_error_invalid_content()],
    ),
)
def from_all_instantiation_types_case__invalid_content(
    responses,
    path_parameters_type,
    message_body_type,
    whatsapp_channel_instantiation_type,
):
    return (
        responses[0],
        responses[1],
        path_parameters_type,
        message_body_type,
        whatsapp_channel_instantiation_type,
    )
