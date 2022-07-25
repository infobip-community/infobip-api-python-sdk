from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.delete_template import (
    DeleteTemplatePathParameters,
)
from tests.conftest import get_expected_delete_headers, get_response_object
from tests.whatsapp.conftest import (
    get_response_object_unofficial,
    get_whatsapp_channel_instance,
)


def delete_template_request(
    http_server,
    response,
    instantiation_type,
    path_parameters_type,
    **kwargs,
):
    path_parameter_instance = path_parameter = DeleteTemplatePathParameters(
        sender="38598765321", template_name="test"
    )
    http_server.expect_request(
        "/whatsapp/2/senders/38598765321/templates/test",
        method="DELETE",
        headers=get_expected_delete_headers(),
    ).respond_with_response(response)

    whatsapp_channel = get_whatsapp_channel_instance(instantiation_type, **kwargs)

    if path_parameters_type == "dict":
        path_parameter = path_parameter_instance.dict()

    return whatsapp_channel.delete_template(path_parameter)


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__valid_content",
)
def test_delete_template_from_all_instantiation_types_case__valid_content(
    httpserver,
    http_test_client,
    status_code,
    response_content,
    path_parameters_type,
    whatsapp_channel_instantiation_type,
):
    response = delete_template_request(
        http_server=httpserver,
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_delete_request_headers("secret"),
        ),
    )

    assert response is not None
    assert response.status_code == status_code


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__invalid_content",
)
def test_create_template_from_all_instantiation_types_case__invalid_content(
    httpserver,
    http_test_client,
    http_test_client_unofficial,
    status_code,
    response_content,
    path_parameters_type,
    whatsapp_channel_instantiation_type,
):
    if whatsapp_channel_instantiation_type == "client_unofficial":
        client = http_test_client_unofficial
        response_object = get_response_object_unofficial
    else:
        client = http_test_client
        response_object = get_response_object

    response = delete_template_request(
        http_server=httpserver,
        response=response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        server_url=httpserver.url_for("/"),
        client=client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_delete_request_headers("secret"),
        ),
    )

    assert isinstance(response, ResponseBase) is False
    assert response is not None

    if whatsapp_channel_instantiation_type != "client_unofficial":
        assert response.status_code == status_code
        assert response.json() == response_content
