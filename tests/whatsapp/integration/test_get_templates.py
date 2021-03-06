from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)
from tests.conftest import get_expected_get_headers, get_response_object
from tests.whatsapp.conftest import (
    get_response_object_unofficial,
    get_whatsapp_channel_instance,
)


def get_templates_request(
    http_server,
    response,
    instantiation_type,
    path_parameters_type,
    **kwargs,
):
    path_parameter_instance = path_parameter = ManageTemplatesPathParameters(
        sender="38598765321"
    )
    http_server.expect_request(
        "/whatsapp/1/senders/38598765321/templates",
        method="GET",
        headers=get_expected_get_headers(),
    ).respond_with_response(response)

    whatsapp_channel = get_whatsapp_channel_instance(instantiation_type, **kwargs)

    if path_parameters_type == "dict":
        path_parameter = path_parameter_instance.dict()

    return whatsapp_channel.get_templates(path_parameter)


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__valid_content",
)
def test_get_templates_from_all_instantiation_types_case__valid_content(
    httpserver,
    http_test_client,
    status_code,
    response_content,
    path_parameters_type,
    whatsapp_channel_instantiation_type,
):
    response = get_templates_request(
        http_server=httpserver,
        response=get_response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        server_url=httpserver.url_for("/"),
        client=http_test_client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_get_request_headers("secret"),
        ),
    )

    response_dict = WhatsAppChannel.convert_model_to_dict(response)
    raw_response = response_dict.pop("rawResponse")
    expected_response_dict = {
        **response_content,
        "statusCode": HTTPStatus(status_code),
    }

    assert isinstance(response, ResponseBase) is True
    assert response.status_code == status_code
    assert response_dict == expected_response_dict
    assert raw_response is not None


@parametrize_with_cases(
    "status_code, response_content, path_parameters_type, "
    "whatsapp_channel_instantiation_type",
    prefix="from_all_instantiation_types_case__invalid_content",
)
def test_get_templates_from_all_instantiation_types_case__invalid_content(
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

    response = get_templates_request(
        http_server=httpserver,
        response=response_object(status_code, response_content),
        instantiation_type=whatsapp_channel_instantiation_type,
        path_parameters_type=path_parameters_type,
        server_url=httpserver.url_for("/"),
        client=client(
            url=httpserver.url_for("/"),
            headers=WhatsAppChannel.build_get_request_headers("secret"),
        ),
    )

    assert isinstance(response, ResponseBase) is False
    assert response is not None

    if whatsapp_channel_instantiation_type != "client_unofficial":
        assert response.status_code == status_code
        assert response.json() == response_content
