# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from openapi_client.models.comment1 import Comment1
from openapi_client.models.id1 import Id1
from openapi_client.models.rating1 import Rating1
from openapi_client.models.restaurant_id import RestaurantId
from openapi_client.models.user_id import UserId
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self


class ReviewQuery(BaseModel):
    """
    ReviewQuery
    """  # noqa: E501

    id: Optional[Id1] = None
    restaurant_id: Optional[RestaurantId] = None
    user_id: Optional[UserId] = None
    rating: Optional[Rating1] = None
    comment: Optional[Comment1] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "restaurant_id",
        "user_id",
        "rating",
        "comment",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReviewQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict["id"] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of restaurant_id
        if self.restaurant_id:
            _dict["restaurant_id"] = self.restaurant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict["user_id"] = self.user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict["rating"] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict["comment"] = self.comment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReviewQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": Id1.from_dict(obj["id"]) if obj.get("id") is not None else None,
                "restaurant_id": (
                    RestaurantId.from_dict(obj["restaurant_id"])
                    if obj.get("restaurant_id") is not None
                    else None
                ),
                "user_id": (
                    UserId.from_dict(obj["user_id"])
                    if obj.get("user_id") is not None
                    else None
                ),
                "rating": (
                    Rating1.from_dict(obj["rating"])
                    if obj.get("rating") is not None
                    else None
                ),
                "comment": (
                    Comment1.from_dict(obj["comment"])
                    if obj.get("comment") is not None
                    else None
                ),
            }
        )
        return _obj
