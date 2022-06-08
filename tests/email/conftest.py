import os

from pydantic_factories import ModelFactory

from infobip_channels.email.models.body.add_new_domain import AddNewDomainMessageBody
from infobip_channels.email.models.body.reschedule_messages import (
    RescheduleMessagesMessageBody,
)
from infobip_channels.email.models.body.update_scheduled_status import (
    UpdateScheduledStatusMessageBody,
)
from infobip_channels.email.models.body.update_tracking_events import (
    UpdateTrackingEventsMessageBody,
)
from infobip_channels.email.models.body.validate_email_adresses import (
    ValidateEmailAddressesMessageBody,
)


class GenerateRescheduleEmailMessagesFactory(ModelFactory):
    __model__ = RescheduleMessagesMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """
        Needed because we do not want to generate any random string.
        We will add custom validation to this field when datetime format changes.
        """
        return RescheduleMessagesMessageBody(
            **{"sendAt": "2022-06-01T18:00:00.00+00:00"}
        )


class GenerateUpdateScheduledEmailMessagesStatusFactory(ModelFactory):
    __model__ = UpdateScheduledStatusMessageBody


class GenerateValidateEmailAddressesFactory(ModelFactory):
    __model__ = ValidateEmailAddressesMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because we do not want to generate any random string."""
        return ValidateEmailAddressesMessageBody(**{"to": "test@test"})


class GenerateAddNewDomainFactory(ModelFactory):
    __model__ = AddNewDomainMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because we do not want to generate any random string."""
        return AddNewDomainMessageBody(**{"domainName": "newDomain.com"})


class GenerateUpdateTrackingEventsFactory(ModelFactory):
    __model__ = UpdateTrackingEventsMessageBody


def get_email_body_request():
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
        "sendAt": "2022-11-09T11:35:39.214+00:00",
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
        b"text/plain\r\n\r\n2022-11-09T11:35:39.214+00:00\r\n--mockBoundary\r\nContent"
        b'-Disposition: form-data; name="landingPagePlaceholders"\r\nContent-Type: '
        b"text/plain\r\n\r\nLanding page "
        b"placeholders\r\n--mockBoundary\r\nContent-Disposition: form-data; "
        b'name="landingPageId"\r\nContent-Type: '
        b"text/plain\r\n\r\nLANDING-PAGE-ID-123-xyz\r\n--mockBoundary--\r\n"
    )


def get_empty_response():
    return ""


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


def get_validate_email_addresses_response():
    return {
        "to": "abc@zxc.com",
        "validMailbox": "unknown",
        "validSyntax": True,
        "catchAll": False,
        "disposable": False,
        "roleBased": False,
        "reason": "INBOX_FULL",
    }


def get_add_new_domain_response():
    return {
        "domainId": 1,
        "domainName": "newDomain.com",
        "active": False,
        "tracking": {"clicks": False, "opens": True, "unsubscribe": True},
        "dnsRecords": [
            {
                "recordType": "string",
                "name": "string",
                "expectedValue": "string",
                "verified": True,
            }
        ],
        "blocked": False,
        "createdAt": "2022-05-05T17:32:28.777+01:00",
    }


def get_reschedule_email_messages_response():
    return {"bulkId": "xyz-123-444", "sendAt": "2022-06-01T18:00:00.00+00:00"}


def get_email_delivery_reports_response():
    return {
        "results": [
            {
                "bulkId": "bulk-123",
                "messageId": "abc-123",
                "to": "some@some.com",
                "sentAt": "2022-05-23T07:10:44Z",
                "doneAt": "2022-05-23T07:10:44Z",
                "messageCount": 0,
                "price": {"pricePerMessage": 0, "currency": "string"},
                "status": {
                    "groupId": 0,
                    "groupName": "string",
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "action": "string",
                },
                "error": {
                    "groupId": 0,
                    "groupName": "string",
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "permanent": True,
                },
                "channel": "EMAIL",
            }
        ]
    }


def get_email_logs_response():
    return {
        "results": [
            {
                "bulkId": "bulk-123",
                "messageId": "abc-123",
                "to": "string",
                "from": "string",
                "text": "string",
                "sentAt": "2022-05-23T10:24:59Z",
                "doneAt": "2022-05-23T10:24:59Z",
                "messageCount": 0,
                "price": {"pricePerMessage": 0, "currency": "string"},
                "status": {
                    "groupId": 0,
                    "groupName": "string",
                    "id": 0,
                    "name": "string",
                    "description": "string",
                    "action": "string",
                },
            }
        ]
    }


def get_sent_email_bulks_response():
    return {
        "externalBulkId": "string",
        "bulks": [{"bulkId": "xyz-123-444", "sendAt": "2022-06-06T17:00:00.00+00:00"}],
    }


def get_all_domains_for_account_response():
    return {
        "paging": {"page": 20, "size": 0, "totalPages": 0, "totalResults": 0},
        "results": [
            {
                "domainId": 1,
                "domainName": "newDomain.com",
                "active": False,
                "tracking": {"clicks": True, "opens": True, "unsubscribe": True},
                "dnsRecords": [
                    {
                        "recordType": "string",
                        "name": "string",
                        "expectedValue": "string",
                        "verified": True,
                    }
                ],
                "blocked": True,
                "createdAt": "2022-05-05T17:32:28.777+01:00",
            }
        ],
    }


def get_domain_response():
    return {
        "domainId": 1,
        "domainName": "newDomain.com",
        "active": False,
        "tracking": {"clicks": True, "opens": True, "unsubscribe": True},
        "dnsRecords": [
            {
                "recordType": "string",
                "name": "string",
                "expectedValue": "string",
                "verified": True,
            }
        ],
        "blocked": False,
        "createdAt": "2022-05-05T17:32:28.777+01:00",
    }


def get_update_scheduled_email_messages_status_response():
    return {"bulkId": "xyz-123-444", "status": "PENDING"}


def get_email_delivery_reports_query_parameters():
    return {"messageId": "abc-123", "limit": 1}


def get_email_request_error_response():
    return {
        "requestError": {"serviceException": {"messageId": "error", "text": "error"}}
    }


def get_email_logs_query_parameters():
    return {"messageId": "abc-123", "limit": 1}


def get_sent_email_bulk_id_query_parameter():
    return {"bulkId": "xyz-123-444"}


def get_validate_email_addresses():
    return {"to": "test@test.com"}


def get_all_domains_for_account():
    return {"size": "20", "page": "0"}


def get_domain():
    return {"domainName": "newDomain.com"}
