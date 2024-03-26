# extract-openapi.py
import json
import os
import sys

import yaml
from uvicorn.importer import import_from_string

from generate.constants import OPENAPI_SPEC_FN, SERVICE_NAME


def export_openapi(
    output_dir: str = None,
) -> str:
    """Export the OpenAPI spec from a FastAPI app
    Args:
        output_dir (str): The app directory
    Returns:
        str: The output file
    """
    # Add the application directory to the path
    if output_dir is not None:
        print(f"Adding {output_dir} to sys.path")
        sys.path.insert(0, output_dir)

    # Import the app
    print(f"Importing app from {SERVICE_NAME}")
    app = import_from_string(SERVICE_NAME)
    openapi = app.openapi()

    # Log the version of the openapi spec
    version = openapi.get("openapi", "unknown version")
    print(f"Writing openapi spec v{version}")

    # Write the spec to a file
    openapi_spec_file = os.path.join(output_dir, OPENAPI_SPEC_FN)
    with open(openapi_spec_file, "w") as f:
        if openapi_spec_file.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    # Return the output file
    print(f"OpenAPI spec written to {openapi_spec_file}")
    return openapi_spec_file
