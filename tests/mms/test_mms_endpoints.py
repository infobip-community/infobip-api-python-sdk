from http import HTTPStatus
from unittest.mock import patch

from pytest_cases import parametrize_with_cases

from infobip_channels.core.models import ResponseBase
from infobip_channels.mms.channel import MMSChannel
from tests.conftest import get_expected_post_headers, get_response_object


def set_up_mock_server_and_send_request(
    httpserver, mms_body_multipart, status_code, response_content, mms_body_request
):
    httpserver.expect_request(
        "/mms/1/single",
        method="POST",
        data=mms_body_multipart,
        headers=get_expected_post_headers("multipart/form-data; boundary=mockBoundary"),
    ).respond_with_response(get_response_object(status_code, response_content))

    mms_channel = MMSChannel.from_auth_params(
        {"base_url": httpserver.url_for("/"), "api_key": "secret"}
    )

    return mms_channel.send_mms_message(mms_body_request)


@patch("urllib3.filepost.choose_boundary", return_value="mockBoundary")
@parametrize_with_cases(
    "status_code, response_content", prefix="case__supported_status"
)
def test_send_mms_message__supported_status(
    mock_boundary,
    httpserver,
    status_code,
    response_content,
    mms_body_request,
    mms_body_multipart,
):

    response = set_up_mock_server_and_send_request(
        httpserver, mms_body_multipart, status_code, response_content, mms_body_request
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


@patch("urllib3.filepost.choose_boundary", return_value="mockBoundary")
@parametrize_with_cases(
    "status_code, response_content", prefix="case__unsupported_status"
)
def test_send_mms_message__unsupported_status(
    mock_boundary,
    httpserver,
    status_code,
    response_content,
    mms_body_request,
    mms_body_multipart,
):
    response = set_up_mock_server_and_send_request(
        httpserver, mms_body_multipart, status_code, response_content, mms_body_request
    )

    assert isinstance(response, ResponseBase) is False
    assert response is not None
    assert response.status_code == status_code
    assert response.json() == response_content
