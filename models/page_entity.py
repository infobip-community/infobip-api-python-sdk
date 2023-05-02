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


from typing import List, Optional
from pydantic import BaseModel
from models.entity import Entity
from models.page_info import PageInfo


class PageEntity(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    results: Optional[List[Entity]] = None
    paging: Optional[PageInfo] = None
    __properties = ["results", "paging"]

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
    def from_json(cls, json_str: str) -> PageEntity:
        """Create an instance of PageEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict["paging"] = self.paging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PageEntity:
        """Create an instance of PageEntity from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PageEntity.parse_obj(obj)

        _obj = PageEntity.parse_obj(
            {
                "results": [Entity.from_dict(_item) for _item in obj.get("results")]
                if obj.get("results") is not None
                else None,
                "paging": PageInfo.from_dict(obj.get("paging"))
                if obj.get("paging") is not None
                else None,
            }
        )
        return _obj
