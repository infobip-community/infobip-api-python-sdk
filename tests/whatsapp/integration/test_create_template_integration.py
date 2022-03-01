from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)
from infobip_channels.whatsapp.models.response.core import WhatsAppResponse
from tests.whatsapp.conftest import (
    CreateTemplateBodyFactory,
    get_response_object,
    get_response_object_unofficial,
    get_whatsapp_channel_instance,
)


def create_template_request(
    http_server,
    headers,
    response,
    instantiation_type,
    path_parameters_type,
    message_body_type,
    **kwargs,
):
    path_parameter_instance = path_parameter = ManageTemplatesPathParameters(
        sender="38598765321"
    )
    message_body_instance = message_body = CreateTemplateBodyFactory.build()
    http_server.expect_request(
        "/whatsapp/1/senders/38598765321/templates",
        method="POST",
        json=message_body_instance.dict(by_alias=True),
        headers=headers,
    ).respond_with_response(response)

    whatsapp_channel = get_whatsapp_channel_instance(instantiation_type, **kwargs)

    if path_parameters_type == "dict":
        path_parameter = path_parameter_instance.dict()
    if message_body_type == "dict":
        message_body = message_body_instance.dict()

    return whatsapp_channel.create_template(path_parameter, message_body)


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__valid_content",
)
def test_create_template_from_all_instantiation_types_case__valid_content(
    httpserver,
    http_test_client,
    status_code,
    response_content,
    path_parameters_type,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_post_headers,
):
    response = create_template_request(
        http_server=httpserver,
        headers=get_expected_post_headers("secret"),
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        message_body_type=message_body_type,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_post_request_headers("secret"),
        ),
    )

    response_dict = WhatsAppChannel.convert_model_to_dict(response)
    raw_response = response_dict.pop("rawResponse")
    expected_response_dict = {
        **response_content,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, WhatsAppResponse) is True
    assert response.status_code == status_code
    assert response_dict == expected_response_dict
    assert raw_response is not None


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "message_body_type, whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__invalid_content",
)
def test_create_template_from_all_instantiation_types_case__invalid_content(
    httpserver,
    http_test_client,
    http_test_client_unofficial,
    status_code,
    response_content,
    path_parameters_type,
    message_body_type,
    whatsapp_channel_instantiation_type,
    get_expected_post_headers,
):
    if whatsapp_channel_instantiation_type == "client_unofficial":
        client = http_test_client_unofficial
        response_object = get_response_object_unofficial
    else:
        client = http_test_client
        response_object = get_response_object

    response = create_template_request(
        http_server=httpserver,
        headers=get_expected_post_headers("secret"),
        response=response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        message_body_type=message_body_type,
        server_url=httpserver.url_for("/"),
        client=client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_post_request_headers("secret"),
        ),
    )

    assert isinstance(response, WhatsAppResponse) is False
    assert response is not None

    if whatsapp_channel_instantiation_type != "client_unofficial":
        assert response.status_code == status_code
        assert response.json() == response_content
