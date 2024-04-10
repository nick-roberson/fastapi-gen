from typing import List

from pydantic import BaseModel, ConfigDict

from builder.models.configs import (DatabaseConfig, DependencyConfig,
                                    ModelConfig, ServiceConfig)


class ServiceVersion(BaseModel):
    """Service version. Used to export and import the previous states of the service that
    has been generated. This will be useful later for versioning the service and models, and for
    testing the changes in the service and models.
    """

    model_config = ConfigDict(extra="ignore", from_attributes=True)
    version: int
    created_at: str
    db_config: DatabaseConfig = None
    models: List[ModelConfig] = []
    dependencies: List[DependencyConfig] = []

    @property
    def config(self):
        return ServiceConfig(
            database=self.db_config, models=self.models, dependencies=self.dependencies
        )

    def __str__(self):
        return f"ServiceVersion(version={self.version}, models={self.models}, dependencies={self.dependencies})"
