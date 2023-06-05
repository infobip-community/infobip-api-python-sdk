import pytest
from common import TEST_URL, get_test_client, get_test_sync_client

from infobip.api.sms import PATH_PREVIEW_SMS, PATH_SEND_SMS
from infobip.models.sms_advanced_textual_request import SendSMSRequestBody
from infobip.models.sms_destination import Destination
from infobip.models.sms_preview_request import PreviewSMSRequestBody
from infobip.models.sms_preview_response import PreviewSMSResponseBody
from infobip.models.sms_response import SendSMSResponseBody
from infobip.models.sms_textual_message import Message


@pytest.mark.asyncio
async def test_preview_message(httpx_mock):
    expected_response = {
        "originalText": "Let's see how many characters remain unused in this message.",
        "previews": [
            {
                "textPreview": "Let's see how many characters remain unused in this message.",
                "messageCount": 1,
                "charactersRemaining": 96,
                "configuration": {},
            }
        ],
    }

    async with get_test_client() as client:
        httpx_mock.add_response(
            url=f"{TEST_URL}{PATH_PREVIEW_SMS}",
            method="POST",
            json=expected_response,
            status_code=200,
        )

        request_body = PreviewSMSRequestBody(
            text="Let's see how many characters remain unused in this message.",
        )
        response = await client.SMS.preview(request_body)

        assert response.status_code == 200
        assert (
            PreviewSMSResponseBody.from_json(response.text).to_dict()
            == expected_response
        )


@pytest.mark.asyncio
async def test_send_sms_message(httpx_mock):
    expected_response = {
        "bulkId": "2034072219640523072",
        "messages": [
            {
                "messageId": "2250be2d4219-3af1-78856-aabe-1362af1edfd2",
                "status": {
                    "description": "Message sent to next instance",
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 26,
                    "name": "MESSAGE_ACCEPTED",
                },
                "to": "41793026727",
            }
        ],
    }

    async with get_test_client() as client:
        httpx_mock.add_response(
            url=f"{TEST_URL}{PATH_SEND_SMS}",
            method="POST",
            json=expected_response,
            status_code=200,
        )

        request_body = SendSMSRequestBody(
            messages=[
                Message(
                    destinations=[
                        Destination(
                            to="555555555555",
                        ),
                    ],
                    text="Hello from Infobip Python SDK!",
                )
            ]
        )
        response = await client.SMS.send(request_body)

        assert response.status_code == 200
        assert (
            SendSMSResponseBody.from_json(response.text).to_dict() == expected_response
        )


def test_sync_preview(httpx_mock):
    expected_response = {
        "originalText": "Let's see how many characters remain unused in this message.",
        "previews": [
            {
                "textPreview": "Let's see how many characters remain unused in this message.",
                "messageCount": 1,
                "charactersRemaining": 96,
                "configuration": {},
            }
        ],
    }

    client = get_test_sync_client()
    httpx_mock.add_response(
        url=f"{TEST_URL}{PATH_PREVIEW_SMS}",
        method="POST",
        json=expected_response,
        status_code=200,
    )

    request_body = PreviewSMSRequestBody(
        text="Let's see how many characters remain unused in this message.",
    )
    response = client.SMS.preview(request_body)

    assert response.status_code == 200
    assert (
        PreviewSMSResponseBody.from_json(response.text).to_dict() == expected_response
    )
