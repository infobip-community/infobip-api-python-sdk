import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.rcs.Models.body.send_bulk_rcs_message import RCSMessageBodyList
from tests.rcs.conftest import RCSMessageBodyListModelFactory


@pytest.mark.parametrize("messages_list", ["", None, {}])
def test_when_messages_list_is_invalid__validation_error_is_raised(messages_list):
    with pytest.raises(ValidationError):
        RCSMessageBodyListModelFactory.build(
            **{"messages": messages_list})


def test_when_input_data_is_valid_text__validation_error_is_not_raised():
    try:
        RCSMessageBodyList(
            **{"messages":
                [
                    {
                        "from": "myRcsSender 1",
                        "to": "385977666618",
                        "validityPeriod": 15,
                        "validityPeriodTimeUnit": "MINUTES",
                        "content": {
                            "text": "exampleText",
                            "type": "TEXT"
                        }
                    },
                    {
                        "from": "myRcsSender 2",
                        "to": "385977666618",
                        "validityPeriod": 15,
                        "validityPeriodTimeUnit": "MINUTES",
                        "content": {
                            "text": "exampleText",
                            "type": "TEXT"
                        }
                    },
                ]
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
