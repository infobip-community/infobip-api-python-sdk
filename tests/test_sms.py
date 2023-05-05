import pytest

from common import TEST_URL, get_test_client
from infobip.models.sms_preview_request import PreviewSMSRequestBody
from infobip.models.sms_preview_response import PreviewSMSResponseBody


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
            url=f"{TEST_URL}{client.SMS.PATH_PREVIEW_SMS}",
            method="POST",
            json=expected_response,
            status_code=200,
        )

        request_body = PreviewSMSRequestBody(
            text="Let's see how many characters remain unused in this message.",
        )

        response = await client.SMS.preview_message(request_body)

        assert PreviewSMSResponseBody.from_json(response.text).to_dict() == expected_response
        assert response.status_code == 200
