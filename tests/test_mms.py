import urllib.parse

import pytest

from infobip.models.mms_get_inbound_messages_query_parameters import (
    GetInboundMessagesQueryParameters,
)
from infobip.models.mms_inbound_report_response import GetInboundMessagesResponseBody
from tests.common import TEST_URL, get_test_client


@pytest.mark.asyncio
async def test_get_inbound_messages(httpx_mock):
    expected_response = {
        "results": [
            {
                "messageId": "817790313235066447",
                "to": "25256",
                "from": "41793026727",
                "message": '{"mms_parts":[{"origin":"text","contentType":"text/plain; charset=utf-8",'
                '"contentId":"content0","value":"Sample text"}],"userAgent":"motogstylus5g",'
                '"priority":null,"subject":null}',
                "receivedAt": "2016-10-06T09:28:39.220+0000",
                "mmsCount": 1,
                "callbackData": "Some custom data",
                "price": {"pricePerMessage": 0.0, "currency": "EUR"},
            }
        ]
    }

    async with get_test_client() as client:
        query_parameters = GetInboundMessagesQueryParameters(
            limit=10,
        )
        url_params = urllib.parse.urlencode(query_parameters.to_dict())

        httpx_mock.add_response(
            url=f"{TEST_URL}{client.MMS.PATH_GET_INBOUND_MESSAGES}?{url_params}",
            method="GET",
            json=expected_response,
            status_code=200,
        )

        query_parameters = GetInboundMessagesQueryParameters(
            limit=10,
        )
        response = await client.MMS.get_inbound_messages(query_parameters)

        response_body = GetInboundMessagesResponseBody.from_json(
            response.text
        ).to_dict()
        assert response.status_code == 200
        assert response_body["results"][0]["messageId"] == "817790313235066447"
