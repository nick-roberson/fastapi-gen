import os

import yaml

from service_builder.constants import VERSIONS_DIR
from service_builder.models import ServiceVersion


def load_versions() -> list[ServiceVersion]:
    """Load the versions from the versions directory

    Returns:
        list[ServiceVersion]: A list of ServiceVersion objects
    """
    versions = []

    # If versions dir does not exist, create it and return empty list
    if not os.path.exists(VERSIONS_DIR):
        os.makedirs(VERSIONS_DIR, exist_ok=True)
        return []

    # Load each version in
    for file in os.listdir(VERSIONS_DIR):
        if file.endswith(".yaml"):
            version_file = os.path.join(VERSIONS_DIR, file)
            with open(version_file, "r") as f:
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
