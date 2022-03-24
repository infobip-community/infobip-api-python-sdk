from datetime import date

import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import get_random_string
from tests.mms.conftest import MMSMessageBodyFactory


@pytest.mark.parametrize(
    "head",
    [
        None,
        "",
        {},
        {"from": "38599854312"},
        {"to": "38598764321"},
    ],
)
def test_when_head_is_invalid__validation_error_is_raised(head):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(**{"head": head})


@pytest.mark.parametrize("from_number", [None, {}])
def test_when_from_number_is_invalid__validation_error_is_raised(from_number):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{"head": {"from": from_number, "to": "38598764321"}}
        )


@pytest.mark.parametrize("callback_data", [{}, get_random_string(201)])
def test_when_callback_data_is_invalid__validation_error_is_raised(callback_data):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "callbackData": callback_data,
                }
            }
        )


@pytest.mark.parametrize("notify_url", [{}, "string", "ftp://url.com"])
def test_when_notify_url_is_invalid__validation_error_is_raised(notify_url):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "notifyUrl": notify_url,
                }
            }
        )


@pytest.mark.parametrize("send_at", [{}, "22-03-2022", date.today()])
def test_when_send_at_is_invalid__validation_error_is_raised(send_at):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "sendAt": send_at,
                }
            }
        )


@pytest.mark.parametrize("intermediate_report", [{}, "", 0, "True"])
def test_when_intermediate_report_is_invalid__validation_error_is_raised(
    intermediate_report,
):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(
            **{
                "head": {
                    "from": "38599854312",
                    "to": "38598764321",
                    "intermediateReport": intermediate_report,
                }
            }
        )
