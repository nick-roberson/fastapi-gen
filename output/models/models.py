# Model Type Imports
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from typing import List, Dict

# Models


class User(BaseModel):
    id: str = FieldInfo(
        default=None, description="The unique identifier of the user", required=False
    )

    username: str = FieldInfo(description="The username of the user", required=True)

    email: str = FieldInfo(description="The email of the user", required=True)

    class Config:
        extra = "ignore"

    def to_dict(self) -> Dict:
        return self.dict()


class Group(BaseModel):
    id: str = FieldInfo(
        default=None, description="The unique identifier of the group", required=False
    )

    name: str = FieldInfo(description="The name of the group", required=True)

    users: list = FieldInfo(description="None", required=True)

    class Config:
        extra = "ignore"

    def to_dict(self) -> Dict:
        return self.dict()
