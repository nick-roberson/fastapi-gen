import os

# Directory containing the generated code within the output directory
CODEGEN_DIR_NAME: str = "backend"

# Sample input file and output dir
SAMPLE_INPUT_FILE: str = os.path.abspath("example/mongo/restaurant.yaml")
SAMPLE_OUTPUT_DIR: str = os.path.abspath("example/mongo/output")

# Version directory
VERSIONS_DIR: str = os.path.abspath("versions")

# Template directories
TEMPLATE_DIR: str = os.path.abspath("builder/templates")

# Backend templates
MODEL_TEMPLATES: str = f"{TEMPLATE_DIR}/backend/models/"
SERVICE_TEMPLATES: str = f"{TEMPLATE_DIR}/backend/service/"
POETRY_TEMPLATES: str = f"{TEMPLATE_DIR}/backend/poetry/"
README_TEMPLATES: str = f"{TEMPLATE_DIR}/backend/readme/"
DOCKER_TEMPLATES: str = f"{TEMPLATE_DIR}/backend/docker/"

# Frontend templates
FRONTEND_TEMPLATES: str = f"{TEMPLATE_DIR}/frontend/"

# Alembic Templates
ALEMBIC_TEMPLATES: str = f"{TEMPLATE_DIR}/databases/alembic/"

# MongoDB Templates
MONGO_TEMPLATES: str = f"{TEMPLATE_DIR}/databases/mongo/"

# Default port
DEFAULT_PORT: int = 8000

# Service Python Dependencies
PYTHON_VERSION = "3.12.2"
PYTHON_DEPENDENCIES = [
    ("python", PYTHON_VERSION),
    ("pydantic", "^2.6.4"),
    ("fastapi", "^0.110.0"),
    ("uvicorn", "^0.28.0"),
    ("pymongo", "^4.6.2"),
    ("certifi", "^2024.2.2"),
    ("rich", "^13.7.1"),
    ("alembic", "^1.13.1"),
    ("sqlalchemy", "^2.0.29"),
    ("pymysql", "^1.0.2"),
]

# Node Dependencies
NODE_DEPENDENCIES = [
    "axios",
    "@mui/material",
    "@mui/icons-material",
    "@mui/x-data-grid",
    "@mui/styled-engine",
    "@mui/lab",
    "@emotion/react",
    "@emotion/styled",
    "prettier",
    "eslint",
    "web-vitals",
    "react-router-dom",
]

# OpenAPI Spec filename
SAMPLE_OPENAPI_DIR: str = "data/openapi/"
OPENAPI_SPEC_FN: str = "openapi.json"

# Service name
SERVICE_NAME: str = "service:app"

# Default service name
DEFAULT_SERVICE_NAME: str = "my-service"

# Verbose logging
VERBOSE: bool = True if os.getenv("VERBOSE") else False

# Required Database Environment Variables
REQUIRED_DB_ENV_VARS = {
    "mysql": ["DB_HOST", "DB_PORT", "DB_USER", "DB_NAME", "DB_PASSWORD"],
    "postgres": ["DB_HOST", "DB_PORT", "DB_USER", "DB_NAME", "DB_PASSWORD"],
    "mongo": ["MONGO_URI"],
}
