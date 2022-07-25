import pytest
from pydantic.error_wrappers import ValidationError

from tests.whatsapp.conftest import DeleteTemplatePathParametersFactory


@pytest.mark.parametrize("sender", [None, {}])
def test_when_sender_is_invalid__validation_error_is_raised(sender):
    with pytest.raises(ValidationError):
        DeleteTemplatePathParametersFactory.build(**{"sender": sender})


@pytest.mark.parametrize("template_name", [None, {}])
def test_when_template_name_is_invalid__validation_error_is_raised(template_name):
    with pytest.raises(ValidationError):
        DeleteTemplatePathParametersFactory.build(**{"templateName": template_name})
