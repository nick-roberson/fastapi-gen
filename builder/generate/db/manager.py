import os
from subprocess import run

import psycopg2
import pymysql

from builder.generate.db.constants import get_url
from builder.models import ServiceConfig


class DBManager:
    """
    Manages database operations based on the given service configuration and output directory.
    This class handles tasks such as creating, running, and reverting database migrations
    using Alembic through Poetry-managed environments.
    """

    def __init__(self, service_config: ServiceConfig, output_dir: str):
        """
        Initialize the DBManager with service configuration and output directory.

        Args:
            service_config (ServiceConfig): Configuration object containing details about the service,
                                            including database configurations and service metadata.
            output_dir (str): Base directory where the output and generated files will be managed.
                              This typically includes generated code and migration files.
        """
        # Initialize the output directory and service configuration
        self.output_dir = output_dir
        self.service_config = service_config

        # Initialize the service name
        self.service_name = service_config.service_info.name

        # Initialize backend and database directories
        self.backend_dir = os.path.join(output_dir, "backend")
        self.db_dir = os.path.join(self.backend_dir, "src/db")

        # Get the DB URL based on the service configuration
        self.db_url = get_url(service_config.database.db_type)

        # Get DB Environment Variables
        self.db_port_env = service_config.database.port_env
        self.db_host_env = service_config.database.host_env
        self.db_user_env = service_config.database.user_env
        self.db_name_env = service_config.database.db_name_env
        self.db_password_env = service_config.database.password_env

        # Create DB Config
        self.mysql_db_config = {
            "host": os.getenv(self.db_host_env),
            "port": int(os.getenv(self.db_port_env)),
            "user": os.getenv(self.db_user_env),
            "password": os.getenv(self.db_password_env),
            "db": "",  # self.service_name # os.getenv(self.db_name_env),
        }
        self.postgres_db_config = {
            "dbname": os.getenv(self.db_name_env),
            "user": os.getenv(self.db_user_env),
            "password": os.getenv(self.db_password_env),
            "host": os.getenv(self.db_host_env),
            "port": int(os.getenv(self.db_port_env)),
        }

        # Check if a connection can be made to the database
        self.get_db_connection()

    def db_code_exists(self):
        """
        Checks if the database code directory exists in the backend directory.

        Raises:
            FileNotFoundError: If the database directory does not exist.
        """
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Database service not found at {self.db_dir}")

    def get_db_connection(self) -> object:
        """
        Checks that a connection can be made to the database.
        Supports both MySQL and PostgreSQL databases.
        """
        self.db_code_exists()
        db_type = self.service_config.database.db_type
        try:
            if db_type == "mysql":
                connection = pymysql.connect(**self.mysql_db_config)
            elif db_type == "postgres":
                connection = psycopg2.connect(**self.postgres_db_config)
            else:
                raise ValueError("Unsupported database type")
            print("Database connection successful.")
            return connection
        except Exception as e:
            raise Exception(f"Failed to connect to the database: {e}")

    def create_schema(self):
        """
        Create the database schema named after the service name using connections
        to MySQL or PostgreSQL databases.
        """
        self.db_code_exists()
        db_type = self.service_config.database.db_type
        try:
            if db_type == "mysql":
                connection = pymysql.connect(**self.mysql_db_config)
                with connection.cursor() as cursor:
                    sql = f"CREATE SCHEMA IF NOT EXISTS {self.service_name}"
                    print(f"Creating database schema {sql}")
                    cursor.execute(sql)
                print(f"Database schema {self.mysql_db_config['db']} created.")
            elif db_type == "postgres":
                connection = psycopg2.connect(**self.postgres_db_config)
                with connection.cursor() as cursor:
                    sql = f"CREATE SCHEMA IF NOT EXISTS {self.service_name}"
                    print(f"Creating database schema {sql}")
                    cursor.execute(sql)
                print(f"Database schema {self.postgres_db_config['dbname']} created.")
            else:
                raise ValueError("Unsupported database type")
        except Exception as e:
            raise Exception(f"Failed to create the database schema: {e}")
        finally:
            connection.close()

    def create_migration(self, message: str):
        """
        Create a new database migration file using Alembic with auto generation of migration scripts.

        Args:
            message (str): A brief description of the migration for use in the migration script.
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
        print(f"Running command: {' '.join(commands)}")
        run(commands, cwd=self.db_dir)

    def run_migrations(self):
        """
        Applies all pending migrations to the database up to the latest revision using Alembic.
        """
        print(f"Running migrations: {self.service_name}")
        self.db_code_exists()
        commands = ["poetry", "run", "alembic", "upgrade", "head"]
        print(f"Running command: {' '.join(commands)}")
        run(commands, cwd=self.db_dir)

    def revert_migration(self, revision: str):
        """
        Reverts the database schema to a previous version specified by the revision tag using Alembic.

        Args:
            revision (str): The revision identifier to which the database should be reverted.
        """
        self.db_code_exists()
        commands = ["poetry", "run", "alembic", "downgrade", revision]
        run(commands, cwd=self.db_dir)

    def show_migrations(self):
        """
        Displays a list of all database migrations, both applied and pending, using Alembic.

        Prints:
            Outputs the list of migrations directly to the console.
        """
        self.db_code_exists()
        print(f"Migrations: {self.service_name}")
        commands = ["poetry", "run", "alembic", "history"]
        run(commands, cwd=self.db_dir)
