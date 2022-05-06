import os


def get_mms_body_request():
    with open("attachment", "wb") as f:
        f.write(b"random bytes")
        f.flush()
        attachment = open(f.name, "rb")
        os.remove("attachment")

    with open("in_line_image", "wb") as f:
        f.write(b"image bytes")
        f.flush()
        in_line_image = open(f.name, "rb")
        os.remove("in_line_image")

    return {
        "from": "jane.smith@somecompany.com",
        "to": "john.smith@somedomain.com",
        "cc": "john.smith2@somedomain.com",
        "bcc": "john.smith3@somedomain.com",
        "subject": "Mail subject text",
        "text": "Mail body text",
        "bulkId": "BULK-ID-123-xyz",
        "messageId": "MESSAGE-ID-123-xyz",
        "templateid": 1,
        "attachment": attachment,
        "inlineImage": in_line_image,
        "HTML": "<h1>Mail HTML text</h1>",
        "replyto": "john.smith3@somedomain.com",
        "defaultplaceholders": "placeholder",
        "preserverecipients": True,
        "trackingUrl": "https://someurl1.com",
        "trackclicks": True,
        "trackopens": True,
        "track": True,
        "callbackData": "https://someurl2.com",
        "intermediateReport": True,
        "notifyUrl": "https://someurl3.com",
        "notifyContentType": "application/json",
        "sendAt": "2022-05-06T22:29:17.437992",
        "landingPagePlaceholders": "Landing page placeholders",
        "landingPageId": "LANDING-PAGE-ID-123-xyz",
    }


def get_email_body_multipart():
    return (
        b"--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="from"\r\nContent-Type: '
        b"text/plain\r\n\r\njane.smith@somecompany.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="to"\r\nContent-Type: '
        b"text/plain\r\n\r\njohn.smith@somedomain.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="cc"\r\nContent-Type: '
        b"text/plain\r\n\r\njohn.smith2@somedomain.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="bcc"\r\nContent-Type: '
        b"text/plain\r\n\r\njohn.smith3@somedomain.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="subject"\r\nContent-Type: '
        b"text/plain\r\n\r\nMail subject "
        b"text\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="text"\r\nContent-Type: text/plain\r\n\r\nMail body '
        b"text\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="bulkId"\r\nContent-Type: '
        b"text/plain\r\n\r\nBULK-ID-123-xyz\r\n--mockBoundary\r\nContent-Disposition: "
        b'form-data; name="messageId"\r\nContent-Type: '
        b"text/plain\r\n\r\nMESSAGE-ID-123-xyz\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="templateid"\r\nContent-Type: '
        b"text/plain\r\n\r\n1\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="attachment"; filename="attachment"\r\nContent-Type: '
        b"application/octet-stream\r\n\r\nrandom "
        b"bytes\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="inlineImage"; filename="in_line_image"\r\nContent-Type: '
        b"application/octet-stream\r\n\r\nimage "
        b"bytes\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="HTML"\r\nContent-Type: text/plain\r\n\r\n<h1>Mail HTML '
        b"text</h1>\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="replyto"\r\nContent-Type: '
        b"text/plain\r\n\r\njohn.smith3@somedomain.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="defaultplaceholders"\r\nContent-Type: '
        b"text/plain\r\n\r\nplaceholder\r\n--mockBoundary\r\nContent-Disposition: "
        b'form-data; name="preserverecipients"\r\nContent-Type: '
        b"text/plain\r\n\r\nTrue\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="trackingUrl"\r\nContent-Type: '
        b"text/plain\r\n\r\nhttps://someurl1.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="trackclicks"\r\nContent-Type: '
        b"text/plain\r\n\r\nTrue\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="trackopens"\r\nContent-Type: '
        b"text/plain\r\n\r\nTrue\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="track"\r\nContent-Type: '
        b"text/plain\r\n\r\nTrue\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="callbackData"\r\nContent-Type: '
        b"text/plain\r\n\r\nhttps://someurl2.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="intermediatereport"\r\nContent-Type: '
        b"text/plain\r\n\r\nTrue\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="notifyUrl"\r\nContent-Type: '
        b"text/plain\r\n\r\nhttps://someurl3.com\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="notifyContentType"\r\nContent-Type: '
        b"text/plain\r\n\r\napplication/json\r\n--mockBoundary\r\nContent-Disposition"
        b': form-data; name="sendAt"\r\nContent-Type: '
        b"text/plain\r\n\r\n2022-05-06T22:29:17.437992Z\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="landingPagePlaceholders"\r\nContent-Type: '
        b"text/plain\r\n\r\nLanding page "
        b"placeholders\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="landingPageId"\r\nContent-Type: '
        b"text/plain\r\n\r\nLANDING-PAGE-ID-123-xyz\r\n--mockBoundary--\r\n"
    )


def get_sent_email_response():
    return {
        "messages": [
            {
                "to": "john.smith@somedomain.com",
                "messageCount": 1,
                "messageId": "somexternalMessageId",
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 7,
                    "name": "PENDING_ENROUTE",
                    "description": "Message sent to next instance",
                },
            }
        ]
    }


def get_email_request_error_response():
    return {
        "requestError": {"serviceException": {"messageId": "error", "text": "error"}}
    }
