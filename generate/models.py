from typing import Any, List, Optional, Tuple

from pydantic import BaseModel
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


class ModelDefinition(BaseModel):
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
        return f"ModelDefinition(name={self.name}, fields={self.fields})"


class DependencyDefinition(BaseModel):
    """Dependency definition"""

    base: str
    imports: List[str]

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"DependencyDefinition(base={self.base}, imports={self.imports})"


class ModelDefinitionList(BaseModel):
    """List of model definitions"""

    models: List[ModelDefinition]
    dependencies: List[DependencyDefinition]

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"ModelDefinitionList(models={self.models}, dependencies={self.dependencies})"


class ServiceVersion(BaseModel):
    """Service version. Used to export and import the previous states of the service that
    has been generated. This will be useful later for versioning the service and models, and for
    testing the changes in the service and models.
    """

    version: int
    created_at: str
    models: List[ModelDefinition]
    dependencies: List[DependencyDefinition]

    class Config:
        extra = "ignore"

    def __str__(self):
        return f"ServiceVersion(version={self.version}, models={self.models}, dependencies={self.dependencies})"
