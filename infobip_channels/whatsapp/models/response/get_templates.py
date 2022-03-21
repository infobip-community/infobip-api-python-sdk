from typing import List, Optional

from pydantic import AnyHttpUrl

from infobip_channels.core.models import CamelCaseModel, ResponseBase


class Button(CamelCaseModel):
    text: str
    type: str
    phone_number: Optional[str] = None
    url: Optional[AnyHttpUrl] = None


class Header(CamelCaseModel):
    format: str
    text: Optional[str] = None


class Structure(CamelCaseModel):
    header: Optional[Header] = None
    body: str
    footer: Optional[str] = None
    type: str
    buttons: Optional[List[Button]] = None


class Template(CamelCaseModel):
    id: str
    business_account_id: int
    name: str
    language: str
    status: str
    category: str
    structure: Structure


class GetTemplatesResponseOK(ResponseBase):
    templates: List[Template]
