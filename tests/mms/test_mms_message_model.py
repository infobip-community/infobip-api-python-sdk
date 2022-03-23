import pytest
from pydantic.error_wrappers import ValidationError

from tests.mms.conftest import MMSMessageBodyFactory


@pytest.mark.parametrize(
    "head", [None, "", {}, {"from": "38599854312"}, {"to": "38598764321"}]
)
def test_when_head_is_invalid__validation_error_is_raised(head):
    with pytest.raises(ValidationError):
        MMSMessageBodyFactory.build(**{"head": head})

