def get_mms_body_request():
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
        "smil": "<persons><person><name>John</name></person></persons>",
    }


def get_mms_body_multipart():
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


def get_send_mms_response():
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


def get_mms_delivery_reports_query_parameters():
    return {"bulk_id": None, "message_id": "abc-123", "limit": 1}


def get_mms_delivery_reports_response():
    return {
        "results": [
            {
                "bulkId": None,
                "messageId": "abc-123",
                "to": "38598331223",
                "from": "38599873331",
                "sentAt": "2022-04-02T15:44:12.351Z",
                "doneAt": "2022-04-02T15:46:32.931Z",
                "mmsCount": 1,
                "mccMnc": "28988",
                "callbackData": "",
                "price": {"pricePerMessage": 4, "currency": "HRK"},
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 26,
                    "name": "PENDING_ACCEPTED",
                    "description": "Message accepted, pending for delivery.",
                },
                "error": {
                    "groupId": 1,
                    "groupName": "Group 1",
                    "id": 1,
                    "name": "The Name",
                    "description": "Some error",
                },
            }
        ]
    }


def get_inbound_mms_messages_query_parameters():
    return {"limit": 1}


def get_inbound_mms_messages_response():
    return {
        "results": [
            {
                "messageId": "uyx-333",
                "to": "38598331223",
                "from": "38599873331",
                "message": "Hi from MMS!",
                "receivedAt": "2022-04-01T16:44:12.351Z",
                "mmsCount": 1,
                "callbackData": "",
                "price": {"pricePerMessage": 4, "currency": "HRK"},
            }
        ]
    }
