import enum
from typing import Any, List, Optional, Tuple

from pydantic import BaseModel, field_validator
from pydantic.fields import FieldInfo


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
                return f"{self.name}: {self.type} = FieldInfo(description='{self.description}', required={self.required})"
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


class DatabaseTypes(enum.Enum):
    """Database types"""

    MONGO: str = "mongo"

    @classmethod
    def choices(cls):
        return [choice.value for choice in cls]


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


class Config(BaseModel):
    """List of model definitions"""

    database: DatabaseConfig
    models: List[ModelConfig]
    dependencies: List[DependencyConfig]

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"Config(models={self.models}, dependencies={self.dependencies})"


class ServiceVersion(BaseModel):
    """Service version. Used to export and import the previous states of the service that
    has been generated. This will be useful later for versioning the service and models, and for
    testing the changes in the service and models.
    """

    version: int
    created_at: str
    db_config: DatabaseConfig = None
    models: List[ModelConfig] = []
    dependencies: List[DependencyConfig] = []

    @property
    def config(self):
        return Config(
            database=self.db_config, models=self.models, dependencies=self.dependencies
        )

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"ServiceVersion(version={self.version}, models={self.models}, dependencies={self.dependencies})"
