INPUT_DIR: str = "examples"
TEMPLATE_DIR: str = "templates"
OUTPUT_DIR: str = "output"

# Sample input file
SAMPLE_INPUT: str = "examples/models.yaml"

# Template directories
MODEL_TEMPLATES: str = f"{TEMPLATE_DIR}/models/"
SERVICE_TEMPLATES: str = f"{TEMPLATE_DIR}/service/"
MANAGER_TEMPLATES: str = f"{TEMPLATE_DIR}/manager/"
MONGO_TEMPLATES: str = f"{TEMPLATE_DIR}/mongo/"
POETRY_TEMPLATES: str = f"{TEMPLATE_DIR}/poetry/"
README_TEMPLATES: str = f"{TEMPLATE_DIR}/readme/"
FRONTEND_TEMPLATES: str = f"{TEMPLATE_DIR}/frontend/"

# Versions Directory
VERSIONS_DIR: str = "versions"

# Default port
DEFAULT_PORT: int = 8000

# Python Dependencies
PYTHON_DEPENDENCIES = [
    ("python", "3.11.7"),
    ("pydantic", "^2.6.4"),
    ("fastapi", "^0.110.0"),
    ("uvicorn", "^0.28.0"),
    ("pymongo", "^4.6.2"),
    ("certifi", "^2024.2.2"),
    ("rich", "^13.7.1"),
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
]

# OpenAPI Spec filename
OPENAPI_SPEC_FN: str = "openapi.json"

# Service name
SERVICE_NAME: str = "service:app"

# FRONTEND

# Default service name
DEFAULT_SERVICE_NAME: str = "my-service"