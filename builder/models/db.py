import os
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict, Field

from builder.models.enum import DatabaseTypes

# Relational DB types
MYSQL = "mysql"
POSTGRES = "postgres"

# Relational DB drivers
MYSQL_DRIVER = "mysql+pymysql"
POSTGRES_DRIVER = "postgresql"

# Mongo DB Type
MONGO = "mongo"


class DBConfig(BaseModel):
    """Base class for database config."""

    model_config = ConfigDict(extra="ignore", from_attributes=True)

    db_type: str = Field(..., description="Type of the database")
    config: Dict[str, Any] = Field({}, description="Database config")


class MongoDBConfig(DBConfig):
    """Config for a MongoDB setup."""

    db_uri_env: str = Field(..., description="Environment variable for the DB URI")

    def __init__(self, **data):
        """Initialize the MongoDB config."""
        # Check for valid db_type
        if data["db_type"] != MONGO:
            raise ValueError(f"db_type {data['db_type']} must be {MONGO}")

        # Load the environment variables
        data["config"] = {
            "db_uri": os.getenv(data["db_uri_env"]),
        }

        # Call the parent constructor
        super().__init__(**data)


class RelationalDBConfig(DBConfig):
    """Config for a relational database setup."""

    db_driver: str = Field(..., description="Database driver")
    host_env: str = Field(..., description="Environment variable for the host")
    port_env: str = Field(..., description="Environment variable for the port")
    user_env: str = Field(..., description="Environment variable for the user")
    password_env: str = Field(..., description="Environment variable for the password")
    db_name_env: str = Field(
        ..., description="Environment variable for the database name"
    )

    def __init__(self, **data):
        """Initialize the relational database config."""
        # Check for valid db_type
        if data["db_type"] not in [MYSQL, POSTGRES]:
            raise ValueError(f"db_type must be one of {MYSQL} or {POSTGRES}")

        # Set the driver based on the db_type
        if data["db_type"] == MYSQL:
            data["db_driver"] = MYSQL_DRIVER
        elif data["db_type"] == POSTGRES:
            data["db_driver"] = POSTGRES_DRIVER

        # Load the environment variables
        data["config"] = {
            "host": os.getenv(data["host_env"]),
            "port": os.getenv(data["port_env"]),
            "user": os.getenv(data["user_env"]),
            "password": os.getenv(data["password_env"]),
            "db_name": os.getenv(data["db_name_env"]),
        }

        # Call the parent constructor
        super().__init__(**data)
