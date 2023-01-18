import pytest
from pydantic import ValidationError

from infobip_channels.sms.models.body.create_tfa_message_template import CreateTFAMessageTemplateBody
from infobip_channels.sms.models.core.tfa_message_template import PINTypeEnum


@pytest.mark.parametrize("message_text", ["", {}])
def test_when_message_text_is_empty__validation_error_is_raised(message_text):
    with pytest.raises(ValidationError):
        CreateTFAMessageTemplateBody(
            **{
                "messageText": message_text,
                "pinType": PINTypeEnum.NUMERIC,
                "pinPlaceholder": "{{pin}}",
                "regional": {
                    "indiaDlt": {
                        "principalEntityId": "some-id",
                    }
                }
            }
        )


@pytest.mark.parametrize("pin_type", ["", {}, None])
def test_when_pin_type_is_none_or_empty__validation_error_is_raised(pin_type):
    with pytest.raises(ValidationError):
        CreateTFAMessageTemplateBody(
            **{
                "messageText": "some-message {{pin}}",
                "pinType": pin_type,
                "pinPlaceholder": "{{pin}}",
                "regional": {
                    "indiaDlt": {
                        "principalEntityId": "some-id",
                    }
                }
            }
        )


@pytest.mark.parametrize("principal_entity_id", ["", {}])
def test_when_principal_entity_id_is_none_or_empty__validation_error_is_raised(principal_entity_id):
    with pytest.raises(ValidationError):
        CreateTFAMessageTemplateBody(
            **{
                "messageText": "some-message",
                "pinType": PINTypeEnum.NUMERIC,
                "pinPlaceholder": "{{pin}}",
                "regional": {
                    "indiaDlt": {
                        "principalEntityId": principal_entity_id,
                    }
                }
            }
        )


@pytest.mark.parametrize("pin_placeholder", ["", {}])
def test_when_pin_placeholder_is_empty__validation_error_is_raised(pin_placeholder):
    with pytest.raises(ValidationError):
        CreateTFAMessageTemplateBody(
            **{
                "messageText": "some-message",
                "pinType": PINTypeEnum.NUMERIC,
                "pinPlaceholder": pin_placeholder,
                "regional": {
                    "indiaDlt": {
                        "principalEntityId": "some-id",
                    }
                }
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        CreateTFAMessageTemplateBody(
            **{
                "messageText": "some-text",
                "pinType": PINTypeEnum.NUMERIC,
                "pinPlaceholder": "{{pin}}",
                "regional": {
                    "indiaDlt": {
                        "principalEntityId": "some-id",
                    }
                }
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


def test_when_input_data_is_valid_no_regional__validation_error_is_not_raised():
    try:
        CreateTFAMessageTemplateBody(
            **{
                "messageText": "some-text",
                "pinType": PINTypeEnum.NUMERIC,
                "pinPlaceholder": "{{pin}}",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
