import os

# Directory containing the generated code within the output directory
CODEGEN_DIR_NAME: str = "src"

# Sample input file and output dir
SAMPLE_INPUT_FILE: str = os.path.abspath("example/configs/user_groups.yaml")
SAMPLE_OUTPUT_DIR: str = os.path.abspath("data/example_output")

# Version directory
VERSIONS_DIR: str = os.path.abspath("versions")

# Template directories
TEMPLATE_DIR: str = os.path.abspath("builder/templates")
MODEL_TEMPLATES: str = f"{TEMPLATE_DIR}/models/"
SERVICE_TEMPLATES: str = f"{TEMPLATE_DIR}/service/"
MANAGER_TEMPLATES: str = f"{TEMPLATE_DIR}/manager/"
MONGO_TEMPLATES: str = f"{TEMPLATE_DIR}/mongo/"
POETRY_TEMPLATES: str = f"{TEMPLATE_DIR}/poetry/"
README_TEMPLATES: str = f"{TEMPLATE_DIR}/readme/"
FRONTEND_TEMPLATES: str = f"{TEMPLATE_DIR}/frontend/"
DOCKER_TEMPLATES: str = f"{TEMPLATE_DIR}/docker/"

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
