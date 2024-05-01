import os
from subprocess import run

import psycopg2
import pymysql
from rich import print

from builder.generate.db.constants import get_url
from builder.models import ServiceConfig


class DBManager:
    """
    Manages database operations based on the service configuration and output directory.
    Handles tasks such as creating, running, and reverting database migrations using Alembic.
    """

    def __init__(self, service_config: ServiceConfig, output_dir: str):
        """
        Initializes the DBManager with the service configuration and output directory.
        Sets up directories and database configuration, and initializes the database connection.
        """
        # Setup directories for output and database operations
        self.output_dir = output_dir
        self.service_config = service_config
        self.backend_dir = os.path.join(output_dir, "backend")
        self.db_dir = os.path.join(self.backend_dir, "src/db")
        self.db_type = service_config.database.db_type

        # Retrieve the database URL from service configuration
        self.db_url = get_url(service_config.database.db_type)

        # Retrieve the database name from the environment
        self.db_name = os.getenv(self.service_config.database.db_name_env)

        # Setup database configuration from environment variables
        self.db_config = self._setup_db_config()

        # Initialize the database connection or create schema if connection fails
        self._initialize_database()

    def _setup_db_config(self):
        """
        Sets up and returns the database configuration for MySQL and PostgreSQL based on environment variables.
        """
        # Common configuration for both database types
        db_config_common = {
            "host": os.getenv(self.service_config.database.host_env),
            "port": int(os.getenv(self.service_config.database.port_env)),
            "user": os.getenv(self.service_config.database.user_env),
            "password": os.getenv(self.service_config.database.password_env),
        }

        # Return configuration specific to the database type
        if self.db_type == "mysql":
            return {**db_config_common, "db": self.db_name}
        elif self.db_type == "postgres":
            return {**db_config_common, "dbname": self.db_name}
        else:
            raise ValueError("Unsupported database type")

    def _initialize_database(self):
        """
        Tries to establish a database connection; if unsuccessful, it attempts to create the database schema and the database itself.
        """
        try:
            self.connection = self.get_db_connection()
        except Exception as e:
            print(f"Failed to connect to the database, creating schema now: {e}")
            self.ensure_database()

    def db_code_exists(self):
        """
        Checks if the database code directory exists in the specified backend directory.
        """
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Database service not found at {self.db_dir}")

    def get_db_connection(self, with_db: bool = True):
        """
        Attempts to establish and return a database connection using the configured settings for MySQL or PostgreSQL.
        """
        print(f"Getting database connection for {self.db_name}")
        self.db_code_exists()
        try:
            # If we are getting a connection to create the database, we don't need to specify the database name
            config = self.db_config.copy()
            if not with_db:
                print(f"Connecting to database without specifying a database name.")
                if self.db_type == "mysql":
                    config["db"] = ""
                elif self.db_type == "postgres":
                    config["dbname"] = "postgres"

            # Connect to the database based on the type
            if self.db_type == "mysql":
                connection = pymysql.connect(**config)
            elif self.db_type == "postgres":
                connection = psycopg2.connect(**config)
            else:
                raise ValueError("Unsupported database type")
            print("Database connection successful.")
            return connection
        except Exception as e:
            raise Exception(f"Failed to connect to the database: {e}")

    def ensure_database(self):
        """
        Creates the database if it does not exist using the configuration provided.
        """
        self.db_code_exists()
        with self.get_db_connection(with_db=False) as connection:
            cursor = connection.cursor()
            sql = (
                f"CREATE DATABASE IF NOT EXISTS {self.db_name}"
                if self.db_type == "mysql"
                else f"CREATE DATABASE {self.db_name}"
            )
            print(f"Creating database with command: {sql}")
            cursor.execute(sql)
            print(f"Database {self.db_name} created.")
            cursor.close()

    def ensure_schema(self):
        """
        Ensures that the database schema exists by creating it if necessary.
        """
        self.db_code_exists()
        with self.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = f"CREATE SCHEMA IF NOT EXISTS {self.db_name}"
            print(f"Creating database schema with command: {sql}")
            cursor.execute(sql)
            print(f"Database schema {self.db_name} created.")
            cursor.close()

    def create_migration(self, message: str):
        """
        Generates a new database migration file using Alembic with the specified message.
        """
        print(f"Generating migration: {message}")
        self.db_code_exists()
        commands = [
            "poetry",
            "run",
            "alembic",
            "revision",
            "--autogenerate",
            "-m",
            f"'{message}'",
        ]
        run(commands, cwd=self.db_dir)

    def run_migrations(self):
        """
        Applies all pending migrations to the database up to the latest revision.
        """
        print(f"Running migrations on {self.db_name}")
        self.db_code_exists()
        commands = ["poetry", "run", "alembic", "upgrade", "head"]
        run(commands, cwd=self.db_dir)

    def revert_migration(self, revision: str):
        """
        Reverts the database schema to a previous version specified by the revision identifier.
        """
        self.db_code_exists()
        commands = ["poetry", "run", "alembic", "downgrade", revision]
        run(commands, cwd=self.db_dir)

    def show_migrations(self):
        """
        Displays all database migrations, both applied and pending, for review.
        """
        self.db_code_exists()
        commands = ["poetry", "run", "alembic", "history"]
        run(commands, cwd=self.db_dir)
