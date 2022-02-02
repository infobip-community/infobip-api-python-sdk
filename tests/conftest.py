from random import choice
from string import ascii_letters

import pytest
from pydantic_factories import ModelFactory

from whatsapp.authentication.models import Authentication
from whatsapp.core.models import BaseMessageBody


def get_random_string(length):
    return "".join(choice(ascii_letters) for _ in range(length))


class AuthenticationFactory(ModelFactory):
    __model__ = Authentication


class MessageBodyFactory(ModelFactory):
    __model__ = BaseMessageBody


@pytest.fixture
def authentication():
    return AuthenticationFactory.build()
