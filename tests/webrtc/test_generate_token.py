import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.web_rtc.models.body.generate_token import GenerateTokenBody
from tests.conftest import get_random_string
from tests.webrtc.conftest import GenerateTokenFactory


@pytest.mark.parametrize("identity", [None, "", {}, get_random_string(65)])
def test_when_identity_is_invalid__validation_error_is_raised(identity):
    with pytest.raises(ValidationError):
        GenerateTokenFactory.build(
            **{
                "identity": identity,
                "applicationId": "2277594c-76ea-4b8e-a299-e2b6db41b9dc",
                "displayName": "Alice in Wonderland",
                "capabilities": {"recording": "ALWAYS"},
                "timeToLive": 43200,
            }
        )


@pytest.mark.parametrize("display_name", [get_random_string(4), get_random_string(51)])
def test_when_display_name_is_invalid__validation_error_is_raised(display_name):
    with pytest.raises(ValidationError):
        GenerateTokenFactory.build(
            **{
                "identity": "Alice",
                "applicationId": "2277594c-76ea-4b8e-a299-e2b6db41b9dc",
                "displayName": display_name,
                "capabilities": {"recording": "ALWAYS"},
                "timeToLive": 43200,
            }
        )


@pytest.mark.parametrize("time_to_live", [-1, 86401])
def test_when_recording_is_invalid__validation_error_is_raised(time_to_live):
    with pytest.raises(ValidationError):
        GenerateTokenFactory.build(
            **{
                "identity": "Alice",
                "applicationId": "2277594c-76ea-4b8e-a299-e2b6db41b9dc",
                "displayName": "Alice in Wonderland",
                "capabilities": {"recording": "ALWAYS"},
                "timeToLive": time_to_live,
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        GenerateTokenBody(
            **{
                "identity": "Alice12-_.é=+",
                "applicationId": "2277594c-76ea-4b8e-a299-e2b6db41b9dc",
                "displayName": "Alice in Wonderland",
                "capabilities": {"recording": "ALWAYS"},
                "timeToLive": 43200,
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
