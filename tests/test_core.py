import os
from unittest.mock import patch

import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.core.models import Authentication
from tests.conftest import UserInfo


@pytest.mark.parametrize("base_url", [None, "", "ftp://123.api.infobip.com", {}])
def test_when_base_url_is_invalid__validation_error_is_raised(base_url):
    with pytest.raises(ValidationError):
        Authentication(base_url=base_url, api_key="api_key")


@pytest.mark.parametrize("api_key", [None, "", {}])
def test_when_api_key_is_invalid__validation_error_is_raised(api_key):
    with pytest.raises(ValidationError):
        Authentication(base_url="https://123.api.infobip.com", api_key=api_key)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://123.api.infobip.com",
        "https://123.api.infobip.com",
        "123.api.infobip.com",
    ],
)
def test_base_url_in_different_forms__validation_passes(base_url):
    try:
        Authentication(base_url=base_url, api_key="api_key")
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@patch("urllib3.filepost.choose_boundary", return_value="ourBoundary12345")
def test_when_model_inherits_multipart_mixin__it_can_export_multipart_data(boundary):
    with open("profile_img.jpg", "wb") as f:
        f.write(b"X")
        f.flush()
        profile_img = open(f.name, "rb")
        os.remove("profile_img.jpg")

    info = UserInfo(
        **{
            "last_name": "Doe",
            "address": {"street": "Some st. 1", "city": "Split", "zip_code": 21000},
            "profile_image": profile_img,
        }
    )
    body, content_type = info.to_multipart()

    assert body == (
        b"--ourBoundary12345\r\n"
        b'Content-Disposition: form-data; name="lastName"\r\n'
        b"Content-Type: text/plain\r\n\r\n"
        b"Doe\r\n"
        b"--ourBoundary12345\r\n"
        b'Content-Disposition: form-data; name="address"\r\n'
        b"Content-Type: application/json\r\n\r\n"
        b'{"street": "Some st. 1", "city": "Split", "zipCode": 21000}\r\n'
        b"--ourBoundary12345\r\n"
        b"Content-Disposition: form-data; "
        b'name="profileImage"; filename="profile_img.jpg"\r\n'
        b"Content-Type: image/jpeg\r\n\r\nX\r\n"
        b"--ourBoundary12345--\r\n"
    )
    assert content_type == "multipart/form-data; boundary=ourBoundary12345"
