from pydantic import AnyHttpUrl

from core.models import CamelCaseModel


class Authentication(CamelCaseModel):
    base_url: AnyHttpUrl
    api_key: str
