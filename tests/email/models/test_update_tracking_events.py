import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.email.models.body.update_tracking_events import (
    UpdateTrackingEventsMessageBody,
)
from infobip_channels.email.models.path_paramaters.update_tracking_events import (
    UpdateTrackingEventsPathParameter,
)


def test_when_domain_name_is_invalid__validation_error_is_raised():
    with pytest.raises(ValidationError):
        UpdateTrackingEventsPathParameter(
            **{
                "domainName": {},
            }
        )


def test_when_input_data_path_is_valid__validation_error_is_not_raised():
    try:
        UpdateTrackingEventsPathParameter(
            **{
                "domainName": "newDomain.com",
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.parametrize("open_test", ["", {}, "true", 1])
def test_when_open_is_invalid__validation_error_is_raised(open_test):
    with pytest.raises(ValidationError):
        UpdateTrackingEventsMessageBody(
            **{
                "open": open_test,
            }
        )


@pytest.mark.parametrize("clicks", ["", {}, "true", 1])
def test_when_clicks_is_invalid__validation_error_is_raised(clicks):
    with pytest.raises(ValidationError):
        UpdateTrackingEventsMessageBody(
            **{
                "clicks": clicks,
            }
        )


@pytest.mark.parametrize("unsubscribe", ["", {}, "true", 1])
def test_when_unsubscribe_is_invalid__validation_error_is_raised(unsubscribe):
    with pytest.raises(ValidationError):
        UpdateTrackingEventsMessageBody(
            **{
                "unsubscribe": unsubscribe,
            }
        )


def test_when_input_data_body_is_valid__validation_error_is_not_raised():
    try:
        UpdateTrackingEventsMessageBody(
            **{
                "open": True,
                "clicks": True,
                "unsubscribe": True,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
