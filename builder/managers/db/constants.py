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

DB_TYPES = ["postgres", "mysql"]


def get_url(db_type: str) -> str:
    """Get the database URL from the environment variables"""
    # Validate that all environment variables are set
    if not all(v is not None for v in ALL_VARS):
        message = f"ERROR: Missing environment variables: {', '.join(ALL_VARS)}"
        print(message)
        raise ValueError(message)

    # Validate the database type
    if db_type not in DB_TYPES:
        message = f"ERROR: Unsupported database type: {db_type}"
        print(message)
        raise ValueError(message)

    # Return the database URL based on the type
    if db_type == "postgres":
        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    elif db_type == "mysql":
        return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
