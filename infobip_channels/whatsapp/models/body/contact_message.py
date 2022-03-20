from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import validator

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.whatsapp.models.body.core import MessageBody


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
    type: Optional[AddressTypeEnum]


class Email(CamelCaseModel):
    email: Optional[str] = None
    type: Optional[EmailTypeEnum]


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
    type: Optional[PhoneTypeEnum]
    wa_id: Optional[str] = None


class Url(CamelCaseModel):
    url: Optional[str] = None
    type: Optional[UrlTypeEnum]


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
