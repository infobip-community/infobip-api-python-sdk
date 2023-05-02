# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from models.number_registration_address import NumberRegistrationAddress


class NumberRegistrationUpdateBrandRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    address: Optional[NumberRegistrationAddress] = None
    country_code: Optional[StrictStr] = Field(
        None, alias="countryCode", description="The country where the brand is located."
    )
    legal_name: Optional[StrictStr] = Field(
        None, alias="legalName", description="The legal name of the brand."
    )
    name: Optional[StrictStr] = Field(
        None, description="The customer defined name of brand."
    )
    support_email: Optional[StrictStr] = Field(
        None,
        alias="supportEmail",
        description="The business email address to contact about brand compliance issues. Must be a well formed email address that does not include a '=' character.",
    )
    support_phone: Optional[StrictStr] = Field(
        None,
        alias="supportPhone",
        description="The business phone number to contact about brand compliance issues.",
    )
    reference_id: Optional[StrictStr] = Field(
        None,
        alias="referenceId",
        description="Unique user defined ID for the brand. While not required, it is recommended to supply a referenceId as the uniqueness constraint will help ensure a brand is not accidentally created multiple times. Subsequent create requests with the same referenceId will be rejected with an error.",
    )
    tax_id: Optional[StrictStr] = Field(
        None, alias="taxId", description="The tax identifier for the brand."
    )
    vertical: Optional[StrictStr] = Field(
        None, description="The vertical in which the brand operates."
    )
    website: Optional[StrictStr] = Field(None, description="The website for the brand.")
    stock_exchange: Optional[StrictStr] = Field(
        None,
        alias="stockExchange",
        description="The stock exchange where brand is listed.",
    )
    stock_symbol: Optional[StrictStr] = Field(
        None,
        alias="stockSymbol",
        description="The ticker symbol for the brand on the exchange where it is listed.",
    )
    __properties = [
        "address",
        "countryCode",
        "legalName",
        "name",
        "supportEmail",
        "supportPhone",
        "referenceId",
        "taxId",
        "vertical",
        "website",
        "stockExchange",
        "stockSymbol",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NumberRegistrationUpdateBrandRequest:
        """Create an instance of NumberRegistrationUpdateBrandRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict["address"] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationUpdateBrandRequest:
        """Create an instance of NumberRegistrationUpdateBrandRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationUpdateBrandRequest.parse_obj(obj)

        _obj = NumberRegistrationUpdateBrandRequest.parse_obj(
            {
                "address": NumberRegistrationAddress.from_dict(obj.get("address"))
                if obj.get("address") is not None
                else None,
                "country_code": obj.get("countryCode"),
                "legal_name": obj.get("legalName"),
                "name": obj.get("name"),
                "support_email": obj.get("supportEmail"),
                "support_phone": obj.get("supportPhone"),
                "reference_id": obj.get("referenceId"),
                "tax_id": obj.get("taxId"),
                "vertical": obj.get("vertical"),
                "website": obj.get("website"),
                "stock_exchange": obj.get("stockExchange"),
                "stock_symbol": obj.get("stockSymbol"),
            }
        )
        return _obj
