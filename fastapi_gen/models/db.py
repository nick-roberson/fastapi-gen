import os
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict, Field, constr

from fastapi_gen.models.enum import DatabaseTypes

# Relational DB drivers
MYSQL_DRIVER = "mysql+pymysql"
POSTGRES_DRIVER = "postgresql"

# Custom type for string types that enforce a minimum length and no whitespace
MinStrType = constr(strip_whitespace=True, min_length=1)


class DBConfig(BaseModel):
    """Base class for database config."""

    model_config = ConfigDict(extra="ignore", from_attributes=True)

    db_type: MinStrType = Field(..., description="Type of the database")
    config: Dict[MinStrType, Any] = Field({}, description="Database config")

    def __str__(self):
        obfuscated_config = {**self.config}
        if "password" in obfuscated_config:
            obfuscated_config["password"] = "********"
        if "db_uri" in obfuscated_config:
            obfuscated_config["db_uri"] = "********"
        return f"""
        DBConfig(
            db_type={self.db_type},
            config={obfuscated_config}
        )
        """


class RelationalDBConfig(DBConfig):
    """Config for a relational database setup."""

    db_driver: MinStrType = Field(..., description="Database driver")
    host_env: MinStrType = Field(..., description="Environment variable for the host")
    port_env: MinStrType = Field(..., description="Environment variable for the port")
    user_env: MinStrType = Field(..., description="Environment variable for the user")
    password_env: MinStrType = Field(
        ..., description="Environment variable for the password"
    )
    db_name_env: MinStrType = Field(
        ..., description="Environment variable for the database name"
    )

    def __init__(self, **data):
        """Initialize the relational database config."""
        # Check for valid db_type
        if data["db_type"] not in DatabaseTypes.choices():
            raise ValueError(f"db_type must be one of {DatabaseTypes.choices()}")

        # Set the driver based on the db_type
        if data["db_type"] == DatabaseTypes.MYSQL.value:
            data["db_driver"] = MYSQL_DRIVER
        elif data["db_type"] == DatabaseTypes.POSTGRES.value:
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

    def __str__(self):
        obfuscated_config = {**self.config, "password": "********", "host": "********"}
        return f"""
        RelationalDBConfig(
            db_type={self.db_type},
            db_driver={self.db_driver},
            config={obfuscated_config},
            host_env={self.host_env},
            port_env={self.port_env},
            user_env={self.user_env},
            password_env={self.password_env},
            db_name_env={self.db_name_env}
        )
        """
