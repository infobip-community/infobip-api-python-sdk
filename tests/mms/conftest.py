import pytest


@pytest.fixture
def mms_body_request():
    return {
        "head": {
            "from": "38598743321",
            "to": "38599876543",
        },
        "text": "some text",
        "externallyHostedMedia": [
            {
                "contentType": "application/pdf",
                "contentId": "331",
                "contentUrl": "https://a.com",
            }
        ],
    }


@pytest.fixture
def mms_body_multipart():
    return (
        b'--mockBoundary\r\nContent-Disposition: form-data; name="head"\r\n'
        b"Content-Type: application/json\r\n\r\n"
        b'{"from": "38598743321", "to": "38599876543", "id": null, "subject": null, '
        b'"validityPeriodMinutes": null, "callbackData": null, "notifyUrl": null, '
        b'"sendAt": null, "intermediateReport": false, "deliveryTimeWindow": null}\r\n'
        b'--mockBoundary\r\nContent-Disposition: form-data; name="text"\r\n'
        b"Content-Type: text/plain\r\n\r\nsome text\r\n--mockBoundary\r\n"
        b'Content-Disposition: form-data; name="externallyHostedMedia"\r\n'
        b'Content-Type: application/json\r\n\r\n[{"contentType": "application/pdf", '
        b'"contentId": "331", "contentUrl": "https://a.com"}]\r\n--mockBoundary--\r\n'
    )


def get_mms_response():
    return {
        "bulkId": "1",
        "messages": [
            {
                "to": "38599876543",
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 26,
                    "name": "PENDING_ACCEPTED",
                    "description": "Message accepted, pending for delivery.",
                },
                "messageId": "2250be2d4219-3af1-78856-aabe-1362af1edfd2",
            }
        ],
        "errorMessage": "string",
    }
