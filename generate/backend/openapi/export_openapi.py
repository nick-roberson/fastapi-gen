# extract-openapi.py
import json
import sys

import yaml
from uvicorn.importer import import_from_string


def export_openapi(
    application_name: str = "service:app",
    application_dir: str = None,
    output_file: str = "openapi.json",
) -> str:
    """Export the OpenAPI spec from a FastAPI app
    Args:
        application_name (str): The app import string
        application_dir (str): The app directory
        output_file (str): The output file
    Returns:
        str: The output file
    """
    # Add the application directory to the path
    if application_dir is not None:
        print(f"Adding {application_dir} to sys.path")
        sys.path.insert(0, application_dir)

    # Import the app
    print(f"Importing app from {application_name}")
    app = import_from_string(application_name)
    openapi = app.openapi()

    # Write the spec to a file
    version = openapi.get("openapi", "unknown version")
    print(f"Writing openapi spec v{version}")
    with open(output_file, "w") as f:
        if output_file.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    # Return the output file
    print(f"OpenAPI spec written to {output_file}")
    return output_file
