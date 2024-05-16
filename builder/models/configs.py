import os
from typing import Any, List, Optional

import yaml
from faker import Faker
from pydantic import BaseModel, ConfigDict, Field, constr, field_validator

from builder.models.db import DBConfig
from builder.models.enum import DatabaseTypes, FieldDataType

# Custom type for string types that enforce a minimum length and no whitespace
MinStrType = constr(strip_whitespace=True, min_length=1)


class FieldDefinition(BaseModel):
    """Field definition for a model"""

    model_config = ConfigDict(extra="ignore", from_attributes=True)

    def __init__(self, **data):
        super().__init__(**data)
        self.verify_default()

    name: MinStrType = Field(description="Name of the field", required=True)
    type: MinStrType = Field(description="Type of the field", required=True)
    of_type: Optional[str] = Field(
        default=None, description="Reference to another model"
    )
    description: Optional[str] = Field(
        default=None, description="Description of the field"
    )
    default: Optional[Any] = Field(
        default=None, description="Default value of the field"
    )
    required: Optional[bool] = Field(default=True, description="Is the field required")

    @field_validator("type")
    def validate_type(cls, v):
        if v not in FieldDataType.choices():
            raise ValueError(f"type must be one of {FieldDataType.choices()}, was {v}")
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
        return f"""
        FieldDefinition(
            name={self.name},
            type={self.type},
            of_type={self.of_type},
            description={self.description},
            default={self.default},
            required={self.required}
        )
        """

    @property
    def row(self):
        """Outputs a string based on the config of the field, to be used in Jinja template.

        Example:
            input: Input = Field(default=[], description=None, required=True)
        """
        # If required, override to not include default
        if self.required:
            return f"{self.name}: {self.type} = FieldInfo(description='{self.description}', required={self.required})"
        # If not required, include default (if present)
        else:
            if self.default is None:
                return f"{self.name}: Optional[{self.type}] = FieldInfo(default=None, description='{self.description}', required={self.required})"
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
            return f"Column(String(1000), nullable={not self.required}, default='{self.default or ''}')"
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

    def generate_fake_data(self):
        """Generate fake data for the field"""
        fake = Faker()
        if self.type == FieldDataType.STRING.value:
            return fake.word()
        elif self.type == FieldDataType.INTEGER.value:
            return fake.random_int(min=1, max=100)
        elif self.type == FieldDataType.FLOAT.value:
            return float(fake.random_number(digits=2))
        elif self.type == FieldDataType.BOOLEAN.value:
            return fake.boolean()
        elif self.type == FieldDataType.DATETIME.value:
            return fake.date_time_this_decade().isoformat()
        elif self.type == FieldDataType.LIST.value:
            return [fake.word() for _ in range(3)]
        elif self.type == FieldDataType.DICT.value:
            return {fake.word(): fake.word() for _ in range(3)}
        else:
            raise ValueError(
                f"type must be one of {FieldDataType.choices()}, was {self.type}"
            )


class ModelConfig(BaseModel):
    """Model definition"""

    model_config = ConfigDict(extra="ignore", from_attributes=True)

    name: MinStrType
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
        return f"""
        ModelConfig(
            name={self.name},
            fields={self.fields}
        )
        """

    def create_fake_data(self, no_ids: bool = False):
        """Create fake data for the model"""
        return {
            field.name: field.generate_fake_data()
            for field in self.fields
            if field.name != "id" or not no_ids
        }


class DependencyConfig(BaseModel):
    """Dependency definition"""

    model_config = ConfigDict(extra="ignore", from_attributes=True)
    name: MinStrType
    version: Optional[MinStrType] = None

    def __str__(self):
        return f"""
        DependencyConfig(
            name={self.name},
            version={self.version}
        )
        """


class ServiceInfo(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    name: MinStrType
    email: MinStrType
    version: MinStrType = "1.0.0"
    description: MinStrType = "A service built with the FastAPI Gen builder."

    @property
    def author(self):
        return f"{self.name} <{self.email}>"

    def __init__(self, **data):
        super().__init__(**data)
        # Get rid of special characters in the name
        self.name = self.name.replace("-", "_").replace(" ", "_")
        # Set the email if not provided
        if not self.email:
            self.email = f"{self.name}@example.com"

    def __str__(self):
        return f"""
        ServiceInfo(
            name={self.name},
            email={self.email},
            version={self.version},
            description={self.description}
        )
        """


class ServiceConfig(BaseModel):
    """List of model definitions"""

    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Output directory
    output_dir: MinStrType = "output"

    # Service information
    service_info: ServiceInfo
    # Database configuration
    database: DBConfig
    # List of models
    models: List[ModelConfig] = []
    # List of dependencies
    dependencies: List[DependencyConfig] = []

    def to_file(self, file_path: str):
        """Writes config to a YAML file"""
        # If the directory does not exist, create it
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Obfuscate the database password
        config_dict = self.model_dump()
        if self.database.db_type in DatabaseTypes.choices():
            config_dict["database"]["config"]["password"] = "********"
            config_dict["database"]["config"]["host"] = "********"
        else:
            raise ValueError(f"Invalid db_type: {self.database.db_type}")
        # Write the config to the file
        with open(file_path, "w") as file:
            yaml.dump(config_dict, file)

    @classmethod
    def from_file(cls, file_path: str):
        """Reads config from a YAML file"""
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found at {file_path}")
        # Read the config from the file
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return cls(**data)

    def __str__(self):
        return f"""
        ServiceConfig(
            output_dir={self.output_dir},
            service_info={self.service_info},
            database={self.database},
            models={self.models},
            dependencies={self.dependencies}
        )
        """
