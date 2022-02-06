from pytest_cases import parametrize

from tests.conftest import DocumentMessageBodyFactory, TextMessageBodyFactory

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


@parametrize(message_type=MESSAGE_TYPE_ATTRIBUTES.keys(), status_code=(200, 201))
def from_auth_params_case__ok(
    message_type, status_code, get_response_ok, response_ok_content
):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        get_response_ok,
        status_code,
        response_ok_content,
    )


@parametrize(message_type=MESSAGE_TYPE_ATTRIBUTES.keys(), status_code=(400, 405))
def from_auth_params_case__error(
    message_type,
    status_code,
    get_response_error,
    response_error_content,
):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        get_response_error,
        status_code,
        response_error_content,
    )


@parametrize(message_type=MESSAGE_TYPE_ATTRIBUTES.keys())
def from_provided_client_case(message_type, get_response_ok, response_ok_content):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        get_response_ok,
        200,
        response_ok_content,
    )
