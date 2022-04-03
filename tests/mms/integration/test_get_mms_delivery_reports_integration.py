from http import HTTPStatus

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.mms.channel import MMSChannel
from tests.conftest import get_expected_get_headers, get_response_object


def set_up_mock_server_and_send_request(
    httpserver, status_code, response_content, mms_delivery_reports_query_parameters
):
    httpserver.expect_request(
        "/mms/1/reports",
        method="GET",
        query_string="messageId=abc-123&limit=1",
        headers=get_expected_get_headers(),
    ).respond_with_response(get_response_object(status_code, response_content))

    mms_channel = MMSChannel.from_auth_params(
        {"base_url": httpserver.url_for("/"), "api_key": "secret"}
    )

    return mms_channel.get_mms_delivery_reports(mms_delivery_reports_query_parameters)


@parametrize_with_cases(
    "status_code, response_content", prefix="case__supported_status"
)
def test_get_mms_delivery_reports__supported_status(
    httpserver,
    status_code,
    response_content,
    mms_delivery_reports_query_parameters,
):

    response = set_up_mock_server_and_send_request(
        httpserver, status_code, response_content, mms_delivery_reports_query_parameters
    )
    response_dict = MMSChannel.convert_model_to_dict(response)
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
    "status_code, response_content", prefix="case__unsupported_status"
)
def test_get_mms_delivery_reports__unsupported_status(
    httpserver,
    status_code,
    response_content,
    mms_delivery_reports_query_parameters,
):
    response = set_up_mock_server_and_send_request(
        httpserver, status_code, response_content, mms_delivery_reports_query_parameters
    )

    assert isinstance(response, ResponseBase) is False
    assert response is not None
    assert response.status_code == status_code
    assert response.json() == response_content
