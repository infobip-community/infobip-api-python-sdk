from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import Field, validator
from pydantic_collections import BaseCollectionModel

from whatsapp.models.core import CamelCaseModel, MessageBody


class ContactTypeEnum(str, Enum):
    home = "HOME"
    work = "WORK"


class PhoneTypeEnum(str, Enum):
    cell = "CELL"
    main = "MAIN"
    iphone = "IPHONE"
    home = "HOME"
    work = "WORK"


class Address(CamelCaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    address_type: Optional[ContactTypeEnum] = Field(alias="type")


class Addresses(BaseCollectionModel[Address]):
    pass


class Email(CamelCaseModel):
    email: Optional[str] = None
    email_type: Optional[ContactTypeEnum] = Field(alias="type")


class Emails(BaseCollectionModel[Email]):
    pass


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


class Phones(BaseCollectionModel[Phone]):
    pass


class Url(CamelCaseModel):
    url: Optional[str] = None
    url_type: Optional[ContactTypeEnum] = Field(alias="type")


class Urls(BaseCollectionModel[Url]):
    pass


class Contacts(CamelCaseModel):
    addresses: Optional[Addresses] = None
    birthday: Optional[date] = None
    emails: Optional[Emails] = None
    name: Name
    org: Optional[Org] = None
    phones: Optional[Phones] = None
    urls: Optional[Urls] = None

    @validator("birthday")
    def datetime_to_string(cls, v):
        if v:
            return v.isoformat()


class Content(CamelCaseModel):
    contacts: Optional[List[Contacts]]


class ContactMessageBody(MessageBody):
    content: Content
