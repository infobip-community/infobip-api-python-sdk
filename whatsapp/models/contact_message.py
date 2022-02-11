from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import Field, validator

from whatsapp.models.core import CamelCaseModel, MessageBody


class AddressTypeEnum(str, Enum):
    HOME = "HOME"
    WORK = "WORK"


class EmailTypeEnum(str, Enum):
    HOME = "HOME"
    WORK = "WORK"


class UrlTypeEnum(str, Enum):
    HOME = "HOME"
    WORK = "WORK"


class PhoneTypeEnum(str, Enum):
    CELL = "CELL"
    MAIN = "MAIN"
    IPHONE = "IPHONE"
    HOME = "HOME"
    WORK = "WORK"


class Address(CamelCaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    address_type: Optional[AddressTypeEnum] = Field(alias="type")


class Email(CamelCaseModel):
    email: Optional[str] = None
    email_type: Optional[EmailTypeEnum] = Field(alias="type")


class Name(CamelCaseModel):
    first_name: str
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    name_suffix: Optional[str] = None
    name_prefix: Optional[str] = None
    formatted_name: str


class Org(CamelCaseModel):
    company: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None


class Phone(CamelCaseModel):
    phone: Optional[str] = None
    phone_type: Optional[PhoneTypeEnum] = Field(alias="type")
    wa_id: Optional[str] = None


class Url(CamelCaseModel):
    url: Optional[str] = None
    url_type: Optional[UrlTypeEnum] = Field(alias="type")


class Contact(CamelCaseModel):
    addresses: Optional[List[Address]] = None
    birthday: Optional[date] = None
    emails: Optional[List[Email]] = None
    name: Name
    org: Optional[Org] = None
    phones: Optional[List[Phone]] = None
    urls: Optional[List[Url]] = None

    @validator("birthday")
    def datetime_to_string(cls, v):
        if v:
            return v.isoformat()


class Content(CamelCaseModel):
    contacts: List[Contact]


class ContactMessageBody(MessageBody):
    content: Content
