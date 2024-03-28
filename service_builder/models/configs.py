from typing import Any, List, Optional, Tuple

from pydantic import BaseModel, field_validator
from pydantic.fields import FieldInfo

from service_builder.constants import DEFAULT_SERVICE_NAME
from service_builder.models.enum import DatabaseTypes, FieldDataType


class FieldDefinition(BaseModel):
    """Field definition for a model"""

    name: str = FieldInfo(description="Name of the field", required=True)
    type: str = FieldInfo(description="Type of the field", required=True)
    of_type: Optional[str] = FieldInfo(
        default=None, description="Reference to another model"
    )
    description: Optional[str] = FieldInfo(
        default=None, description="Description of the field"
    )
    default: Optional[Any] = FieldInfo(
        default=None, description="Default value of the field"
    )
    required: Optional[bool] = FieldInfo(
        default=True, description="Is the field required"
    )

    @field_validator("type")
    def validate_type(cls, v):
        if v not in FieldDataType.choices():
            raise ValueError(f"type must be one of {FieldDataType.choices()}")
        return v

    @field_validator("default")
    def validate_default(cls, v):
        if v is not None:

            # Infer type of default value
            if isinstance(v, str):
                if v.lower() == "none":
                    return None
                elif v.lower() == "true":
                    return True
                elif v.lower() == "false":
                    return False
            elif isinstance(v, int):
                return int(v)
            elif isinstance(v, float):
                return float(v)
            elif isinstance(v, bool):
                return bool(v)
            elif isinstance(v, list):
                return list(v)
            elif isinstance(v, dict):
                return dict(v)
            else:
                return v
        return v

    class Config:
        extra = "ignore"

    def __str__(self):
        return (
            f"FieldDefinition(name={self.name}, type={self.type}, of_type={self.of_type}, "
            f"description={self.description}, default={self.default}, required={self.required})"
        )

    @property
    def row(self):
        """Outputs a string based on the config of the field, to be used in Jinja template.

        Example:
            input: Input = Field(default=[], description=None, required=True)
        """
        # If required, override to not include default
        if self.required:
            return f"{self.name}: {self.type} = FieldInfo(description='{self.description}', required={self.required})"
        # If not required, include default  (if present)
        else:
            if self.default is None:
                return f"{self.name}: {self.type} = FieldInfo(default=None,description='{self.description}', required={self.required})"
            else:
                return (
                    f"{self.name}: {self.type} = FieldInfo(default={self.default}, description='{self.description}', "
                    f"required={self.required})"
                )


class ModelConfig(BaseModel):
    """Model definition"""

    name: str
    fields: List[FieldDefinition]

    @property
    def model_id_var_name(self):
        return f"{self.name.lower()}_id"

    @property
    def manager_name(self):
        return f"{self.name}Manager"

    @property
    def manager_var_name(self):
        return f"{self.name.lower()}_manager"

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"ModelConfig(name={self.name}, fields={self.fields})"


class DependencyConfig(BaseModel):
    """Dependency definition"""

    name: str
    version: Optional[str] = None

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"DependencyConfig(name={self.name}, version={self.version})"


class DatabaseConfig(BaseModel):
    """Database configuration"""

    db_type: str
    db_uri_env_var: str

    @field_validator("db_type")
    def validate_db_type(cls, v):
        if v not in DatabaseTypes.choices():
            raise ValueError(f"db_type must be one of {cls.ALLOWED_DB_TYPES}")
        return v

    class Config:
        extra = "ignore"


class ServiceConfig(BaseModel):
    """List of model definitions"""

    service_name: str = DEFAULT_SERVICE_NAME
    database: DatabaseConfig
    models: List[ModelConfig]
    dependencies: List[DependencyConfig]

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"Config(models={self.models}, dependencies={self.dependencies})"
