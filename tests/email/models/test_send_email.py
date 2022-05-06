from datetime import date
from io import open
from tempfile import NamedTemporaryFile

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.send_email import EmailMessageBody
from tests.conftest import get_random_string


@pytest.mark.parametrize("from_email", [None, {}])
def test_when_from_email_is_invalid__validation_error_is_raised(from_email):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": from_email,
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
            }
        )


@pytest.mark.parametrize("to", [None, {}])
def test_when_to_is_invalid__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": to,
                "subject": "Mail subject text",
            }
        )


def test_when_cc_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "cc": {},
            }
        )


def test_when_bcc_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "bcc": {},
            }
        )


def test_when_subject_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": {},
            }
        )


def test_when_text_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "text": {},
            }
        )


def test_when_bulk_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "bulkId": {},
            }
        )


def test_when_message_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "messageId": {},
            }
        )


def test_when_templateid_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "templateid": {},
            }
        )


@pytest.mark.parametrize("attachment", [[], {}, get_random_string(3)])
def test_when_attachment_is_invalid__validation_error_is_raised(attachment):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "attachment": attachment,
            }
        )


@pytest.mark.parametrize("inline_image", [[], {}, get_random_string(3)])
def test_when_inline_image_is_invalid__validation_error_is_raised(inline_image):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "inlineImage": inline_image,
            }
        )


def test_when_html_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "HTML": {},
            }
        )


def test_when_replyto_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "replyto": {},
            }
        )


def test_when_defaultplaceholders_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "defaultplaceholders": {},
            }
        )


def test_when_preserverecipients_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "preserverecipients": {},
            }
        )


def test_when_tracking_url_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "trackingUrl": {},
            }
        )


def test_when_trackclicks_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "trackclicks": {},
            }
        )


def test_when_trackopens_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "trackopens": {},
            }
        )


def test_when_track_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "track": {},
            }
        )


@pytest.mark.parametrize("callback_data", [{}, get_random_string(4001)])
def test_when_callback_data_is_invalid__validation_error_is_raised(callback_data):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "callbackData": callback_data,
            }
        )


def test_when_intermediate_report_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "intermediateReport": {},
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "string", "ftp://url.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "notifyUrl": notify_url,
            }
        )


@pytest.mark.parametrize("notify_content_type", [{}, "string"])
def test_when_notify_content_type_is_invalid__validation_error_is_raised(
    notify_content_type,
):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "notifyContentType": notify_content_type,
            }
        )


@pytest.mark.parametrize("send_at", [{}, "22-03-2022", date.today()])
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "sendAt": send_at,
            }
        )


def test_when_landing_page_placeholders_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "landingPagePlaceholders": {},
            }
        )


def test_when_landing_page_id_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        EmailMessageBody(
            **{
                "from": "jane.smith@somecompany.com",
                "to": "john.smith@somedomain.com",
                "subject": "Mail subject text",
                "landingPageId": {},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    f = NamedTemporaryFile("wb")
    f.write(b"random bytes")
    f.flush()
    attachment = open(f.name, "rb")
    in_line_image = open(f.name, "rb")

    try:
        EmailMessageBody(
            **{
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
                "trackingUrl": "https://someurl.com",
                "trackclicks": True,
                "trackopens": True,
                "track": True,
                "callbackData": "https://someurl.com",
                "intermediateReport": True,
                "notifyUrl": "https://someurl.com",
                "notifyContentType": "application/json",
                "sendAt": "2022-05-06T22:29:17.437992",
                "landingPagePlaceholders": "Landing page placeholders",
                "landingPageId": "LANDING-PAGE-ID-123-xyz",
            }
        )
        f.close()
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
