# Directory containing the templates
TEMPLATE_DIR: str = "templates"

# Sample input file and output dir
SAMPLE_INPUT_FILE: str = "data/example_configs/user_groups.yaml"
SAMPLE_OUTPUT_DIR: str = "data/example_output"

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

# Service Python Dependencies
PYTHON_VERSION = "3.12.1"
PYTHON_DEPENDENCIES = [
    ("python", PYTHON_VERSION),
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

# Default service name
DEFAULT_SERVICE_NAME: str = "my-service"
