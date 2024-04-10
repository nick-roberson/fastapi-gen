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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from openapi_client.models.comment import Comment
from openapi_client.models.id2 import Id2
from pydantic import (BaseModel, ConfigDict, Field, StrictFloat, StrictInt,
                      StrictStr)
from typing_extensions import Self


class Review(BaseModel):
    """
    Review
    """  # noqa: E501

    id: Optional[Id2] = None
    restaurant_id: StrictStr = Field(description="The ID of the alembic being reviewed")
    user_id: StrictStr = Field(description="The ID of the user who wrote the review")
    rating: Union[StrictFloat, StrictInt] = Field(
        description="The rating given by the user"
    )
    comment: Optional[Comment] = None
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
        """Create an instance of Review from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict["comment"] = self.comment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Review from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": Id2.from_dict(obj["id"]) if obj.get("id") is not None else None,
                "restaurant_id": obj.get("restaurant_id"),
                "user_id": obj.get("user_id"),
                "rating": obj.get("rating"),
                "comment": (
                    Comment.from_dict(obj["comment"])
                    if obj.get("comment") is not None
                    else None
                ),
            }
        )
        return _obj
