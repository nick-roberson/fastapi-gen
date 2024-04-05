# extract-openapi.py
import json
import os
import sys

import yaml
from uvicorn.importer import import_from_string

from service_builder.constants import (CODEGEN_DIR_NAME, OPENAPI_SPEC_FN,
                                       SERVICE_NAME)


def export_openapi(code_dir: str) -> str:
    """Export the OpenAPI spec from a FastAPI app
    Args:
        code_dir (str): The app directory
    Returns:
        str: The output file
    """
    # Add the application directory to the path
    if code_dir is not None:
        sys.path.insert(0, code_dir)

    # Import the app
    app = import_from_string(SERVICE_NAME)
    openapi = app.openapi()

    # Write the spec to a file
    openapi_spec_file = os.path.join(code_dir, OPENAPI_SPEC_FN)
    with open(openapi_spec_file, "w") as f:
        if openapi_spec_file.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    # Return the output file
    return openapi_spec_file
