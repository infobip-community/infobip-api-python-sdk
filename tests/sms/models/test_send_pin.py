import pytest
from pydantic import ValidationError

from infobip_channels.sms.models.body.send_pin_over_sms import SendPINOverSMSBody


@pytest.mark.parametrize("app_id", ["", {}])
def test_when_app_id_is_none_or_empty__validation_error_is_raised(app_id):
    with pytest.raises(ValidationError):
        SendPINOverSMSBody(
            **{
                "applicationId": app_id,
                "messageId": "7654321",
                "from": "Sender 1",
                "to": "41793026727",
                "placeholders": {"firstName": "John"},
            }
        )


@pytest.mark.parametrize("message_id", ["", {}])
def test_when_message_id_is_none_or_empty__validation_error_is_raised(message_id):
    with pytest.raises(ValidationError):
        SendPINOverSMSBody(
            **{
                "applicationId": "1234567",
                "messageId": message_id,
                "from": "Sender 1",
                "to": "41793026727",
                "placeholders": {"firstName": "John"},
            }
        )


@pytest.mark.parametrize("to", ["", {}])
def test_when_message_id_is_none_or_empty__validation_error_is_raised(to):
    with pytest.raises(ValidationError):
        SendPINOverSMSBody(
            **{
                "applicationId": "1234567",
                "messageId": "7654321",
                "from": "Sender 1",
                "to": to,
                "placeholders": {"firstName": "John"},
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        SendPINOverSMSBody(
            **{
                "applicationId": "1234567",
                "messageId": "7654321",
                "from": "Sender 1",
                "to": "41793026727",
                "placeholders": {"firstName": "John"},
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
