# extract-openapi.py
import json
import os
import sys

import yaml
from uvicorn.importer import import_from_string

from generate.constants import CODEGEN_DIR, OPENAPI_SPEC_FN, SERVICE_NAME


def export_openapi(
    output_dir: str = None,
    file_name: str = OPENAPI_SPEC_FN,
) -> str:
    """Export the OpenAPI spec from a FastAPI app
    Args:
        output_dir (str): The app directory

    Returns:
        str: The output file
    """
    # Add the application directory to the path
    codegen_dir = os.path.join(output_dir, CODEGEN_DIR)
    if codegen_dir is not None:
        sys.path.insert(0, codegen_dir)

    # Import the app
    app = import_from_string(SERVICE_NAME)
    openapi = app.openapi()

    # Log the version of the openapi spec
    version = openapi.get("openapi", "unknown version")

    # Write the spec to a file
    openapi_spec_file = os.path.join(output_dir, file_name)
    with open(openapi_spec_file, "w") as f:
        if openapi_spec_file.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    # Return the output file
    return openapi_spec_file
