from typing import Dict

from service_builder.generate.backend.generator import BackendGenerator
from service_builder.generate.frontend.generator import FrontendGenerator
from service_builder.models import ServiceConfig


def generate(
    service_config: ServiceConfig,
    output_dir: str,
    backend_only: bool = False,
    frontend_only: bool = False,
) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        service_config (ServiceConfig): Service configuration
        output_dir (str): Output directory
        backend_only (bool): Only regenerate the backend
        frontend_only (bool): Only regenerate the frontend
    Returns:
        Dict: Dictionary of the generated files
    """
    # Initialize the backend generator
    backend_generator = BackendGenerator(config=service_config, output_dir=output_dir)
    frontend_generator = FrontendGenerator(config=service_config, output_dir=output_dir)

    # Only regenerate the backend
    if backend_only:
        print("\nGenerating backend services...\n")
        return backend_generator.generate_all()

    # Only regenerate the frontend
    if frontend_only:
        print("\nGenerating frontend services...\n")
        return frontend_generator.generate_all()

    # Regenerate both the backend and frontend
    print("\nGenerating backend and frontend services...\n")
    created_files = backend_generator.generate_all()
    print("\nGenerating frontend services...\n")
    frontend_files = frontend_generator.generate_all()
    return {**created_files, **frontend_files}
