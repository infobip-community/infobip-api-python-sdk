from random import choice
from string import ascii_letters

import pytest
from models.core import Authentication
from pydantic_factories import ModelFactory


def get_random_string(length: int) -> str:
    return "".join(choice(ascii_letters) for _ in range(length))


class AuthenticationFactory(ModelFactory):
    __model__ = Authentication


@pytest.fixture
def authentication():
    return AuthenticationFactory.build()
