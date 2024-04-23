import os
from logging.config import fileConfig

from alembic import context
# Import alembic models
from models import Base
from sqlalchemy import create_engine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# Define the environment variable names for the database connection
DB_HOST_ENV = "DB_HOST"
DB_PORT_ENV = "DB_PORT"
DB_USER_ENV = "DB_USER"
DB_NAME_ENV = "DB_NAME"
DB_PASSWORD_ENV = "DB_PASSWORD"
ALL_ENVS = [DB_HOST_ENV, DB_PORT_ENV, DB_USER_ENV, DB_NAME_ENV, DB_PASSWORD_ENV]

# Pull in environment vars for MYSQL or POSTGRES
DB_HOST = os.getenv(DB_HOST_ENV)
DB_PORT = os.getenv(DB_PORT_ENV)
DB_USER = os.getenv(DB_USER_ENV)
DB_NAME = os.getenv(DB_NAME_ENV)
DB_PASSWORD = os.getenv(DB_PASSWORD_ENV)
ALL_VARS = [DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASSWORD]

# Pull in environment var for DB_TYPE
DB_TYPE = "mysql"


def get_url() -> str:
    """Get the database URL from the environment variables"""
    # Validate that all environment variables are set
    if not all(v is not None for v in ALL_VARS):
        raise ValueError(f"Missing environment variables: {', '.join(ALL_VARS)}")

    # Validate that the DB_TYPE is set
    if DB_TYPE is None:
        raise ValueError("DB_TYPE environment variable must be set")

    # Return the database URL based on the type
    if DB_TYPE == "postgres":
        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    elif DB_TYPE == "mysql":
        return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        raise ValueError(
            f"Invalid database type {DB_TYPE} must be 'postgres' or 'mysql'"
        )


DB_URL = get_url()


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(DB_URL)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
