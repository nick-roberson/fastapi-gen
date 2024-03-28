import os
from typing import List

import yaml
from constants import VERSIONS_DIR
from generate.models import ServiceVersion


def load_versions() -> list[ServiceVersion]:
    """Load the versions from the versions directory

    Returns:
        list[ServiceVersion]: A list of ServiceVersion objects
    """
    # Load versions files from the versions directory
    versions = []
    for file in os.listdir(VERSIONS_DIR):
        if file.endswith(".yaml"):
            with open(f"{VERSIONS_DIR}/{file}", "r") as f:
                versions.append(yaml.safe_load(f))

    # Load thm into ServiceVersion objects
    service_versions = [ServiceVersion(**version) for version in versions]

    # Order by version number first -> last
    service_versions.sort(key=lambda x: x.version, reverse=True)
    return service_versions


def save_version(version: ServiceVersion) -> str:
    """Save the version to the output directory

    Args:
        output_dir (str): The output directory
        version (ServiceVersion): The version to save

    Returns:
        str: The file name of the saved version
    """
    # Write the version to the output directory
    file_name = f"{VERSIONS_DIR}/schema_version_{version.version}.yaml"
    if not os.path.exists(file_name):
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Write the version to the output directory asc;lear
    with open(file_name, "w") as f:
        version_yaml = yaml.dump(
            version.dict(), default_flow_style=False, sort_keys=False
        )
        f.write(version_yaml)

    return file_name
