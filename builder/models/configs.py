from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.fields import FieldInfo

from builder.constants import DEFAULT_SERVICE_NAME
from builder.models.enum import DatabaseTypes, FieldDataType


class FieldDefinition(BaseModel):
    """Field definition for a model"""

    model_config = ConfigDict(extra="ignore")

    def __init__(self, **data):
        super().__init__(**data)
        self.verify_default()

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

    @property
    def camel_case_name(self):
        """For example phone_number -> phoneNumber"""
        return "".join(
            [
                word.capitalize() if i > 0 else word
                for i, word in enumerate(self.name.split("_"))
            ]
        )

    def verify_default(self):
        """We want to check here that if there is a default value, it is of the correct type"""
        if self.default is not None:

            # check none cases
            null_cases = ["None", "none", "null"]
            if self.default in null_cases:
                self.default = None
                return

            # check bool cases
            bool_true_cases = ["True", "true", True]
            bool_false_cases = ["False", "false", False]
            if self.type == "bool":
                if self.default in bool_true_cases:
                    self.default = True
                elif self.default in bool_false_cases:
                    self.default = False
                return

            # check if the type is a valid type
            if self.type == "str":
                expected_type = str
            elif self.type == "int":
                expected_type = int
            elif self.type == "float":
                expected_type = float
            elif self.type == "list":
                expected_type = list
            elif self.type == "dict":
                expected_type = dict
            elif self.type == "datetime":
                expected_type = str
            else:
                raise ValueError(f"Invalid type {self.type}")

            # try to cast the default value to the expected type
            try:
                self.default = expected_type(self.default)
            except ValueError:
                raise ValueError(
                    f"Default value {self.default} is not of type {self.type}"
                )

            # check if the default value is of the expected type
            if not isinstance(self.default, expected_type):
                raise ValueError(
                    f"Default value {self.default} is not of type {self.type}"
                )

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
                return f"{self.name}: Optional[{self.type}] = FieldInfo(default=None,description='{self.description}', required={self.required})"
            else:
                default = f"'{self.default}'" if self.type == "str" else self.default
                return (
                    f"{self.name}: Optional[{self.type}] = FieldInfo(default={default}, description='{self.description}', "
                    f"required={self.required})"
                )

    @property
    def alembic_db_def(self):
        """Return the Alembic database definition for the field"""
        # Handle id fields
        if self.name == "id":
            return "Column(Integer, primary_key=True, autoincrement=True)"

        # Handle all other fields
        if self.type == "str":
            return f"Column(String(10000), nullable={not self.required}, default='{self.default or ''}')"
        elif self.type == "int":
            return (
                f"Column(Integer, nullable={not self.required}, default={self.default})"
            )
        elif self.type == "float":
            return (
                f"Column(Float, nullable={not self.required}, default={self.default})"
            )
        elif self.type == "bool":
            return (
                f"Column(Boolean, nullable={not self.required}, default={self.default})"
            )
        elif self.type == "datetime":
            return f"Column(DateTime, nullable={not self.required}, default=func.now())"
        elif self.type == "list" or self.type == "dict":
            return f"Column(JSON, nullable={not self.required}, default={self.default})"
        else:
            raise ValueError(f"Invalid type {self.type}")


class ModelConfig(BaseModel):
    """Model definition"""

    model_config = ConfigDict(extra="ignore")

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

    def __str__(self):
        return f"ModelConfig(name={self.name}, fields={self.fields})"


class DependencyConfig(BaseModel):
    """Dependency definition"""

    model_config = ConfigDict(extra="ignore")
    name: str
    version: Optional[str] = None

    def __str__(self):
        return f"DependencyConfig(name={self.name}, version={self.version})"


class DatabaseConfig(BaseModel):
    """Database configuration"""

    model_config = ConfigDict(extra="ignore")

    db_type: str
    db_uri_env_var: str

    @field_validator("db_type")
    def validate_db_type(cls, v):
        if v not in DatabaseTypes.choices():
            raise ValueError(f"db_type must be one of {DatabaseTypes.choices()}")
        return v


class ServiceInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str = DEFAULT_SERVICE_NAME
    version: str = "0.1.0"
    description: str = "A service built with builder"

    def __str__(self):
        return f"ServiceInfo(service_name={self.name}, version={self.version}, description={self.description})"


class ServiceConfig(BaseModel):
    """List of model definitions"""

    model_config = ConfigDict(extra="ignore")

    service_info: ServiceInfo
    database: DatabaseConfig
    models: List[ModelConfig] = []
    dependencies: List[DependencyConfig] = []

    def __str__(self):
        return f"Config(models={self.models}, dependencies={self.dependencies})"
