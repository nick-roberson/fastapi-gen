import os

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
    if not all(ALL_ENVS):
        raise ValueError(f"Missing environment variables: {', '.join(ALL_ENVS)}")
    if not all(ALL_VARS):
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


# Get the database URL
DB_URL = get_url()
