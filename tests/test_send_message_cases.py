from pytest_cases import case, parametrize

from tests.conftest import (
    DocumentMessageBodyFactory,
    TextMessageBodyFactory,
    get_response_error,
    get_response_error_content,
    get_response_error_invalid_content,
    get_response_ok,
    get_response_ok_content,
    get_response_ok_invalid_content,
)

MESSAGE_TYPE_ATTRIBUTES = {
    "text": {
        "message_body_factory": TextMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/text",
        "method_name": "send_text_message",
    },
    "document": {
        "message_body_factory": DocumentMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/document",
        "method_name": "send_document_message",
    },
}


@case(tags="valid_response_content")
@parametrize(
    message_type=MESSAGE_TYPE_ATTRIBUTES.keys(),
    responses=(
        (200, get_response_ok, get_response_ok_content),
        (201, get_response_ok, get_response_ok_content),
        (400, get_response_error, get_response_error_content),
        (405, get_response_error, get_response_error_content),
    ),
)
def from_auth_params_case__ok(message_type, responses):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        responses[1](),
        responses[0],
        responses[2](),
    )


@case(tags="invalid_content_or_unexpected_response")
@parametrize(
    message_type=MESSAGE_TYPE_ATTRIBUTES.keys(),
    responses=(
        (201, get_response_ok, get_response_ok_invalid_content),
        (500, get_response_error, get_response_error_invalid_content),
    ),
)
def from_auth_params_case__invalid_content_or_unexpected_response(
    message_type, responses
):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        responses[1](),
        responses[0],
        responses[2](),
    )


@case(tags="provided_client")
@parametrize(message_type=MESSAGE_TYPE_ATTRIBUTES.keys())
def from_provided_client_case(message_type):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        get_response_ok(),
        200,
        get_response_ok_content(),
    )
