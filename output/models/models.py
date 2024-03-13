# Model Type Imports
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from typing import List, Dict

# Models


class Task(BaseModel):

    id: str = FieldInfo(
        default=None, description="The unique identifier of the task", required=False
    )

    name: str = FieldInfo(description="The name of the task", required=True)

    inputs: list = FieldInfo(description="None", required=True)

    outputs: list = FieldInfo(description="None", required=True)

    class Config:
        extra = "ignore"

    def to_dict(self) -> Dict:
        return self.dict()


class Input(BaseModel):

    id: str = FieldInfo(
        default=None, description="The unique identifier of the input", required=False
    )

    name: str = FieldInfo(description="None", required=True)

    type: str = FieldInfo(description="None", required=True)

    class Config:
        extra = "ignore"

    def to_dict(self) -> Dict:
        return self.dict()


class Output(BaseModel):

    id: str = FieldInfo(
        default=None, description="The unique identifier of the output", required=False
    )

    name: str = FieldInfo(description="None", required=True)

    type: str = FieldInfo(description="None", required=True)

    class Config:
        extra = "ignore"

    def to_dict(self) -> Dict:
        return self.dict()
