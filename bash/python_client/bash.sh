# Generate Python Client for the API with OpenAPI Generator
# Usage:
#   - bash python_client.sh
# Dependencies: 
#   - openapi-generator-cli

OUTPUT_DIR="bash/python_client/client"
OPENAPI_JSON="data/example_output/openapi.json"

# Generate config
poetry run python main.py generate-openapi \
    --service-dir data/example_output 

# Generate client
openapi-generator generate \
    -i $OPENAPI_JSON \
    -g python \
    -o $OUTPUT_DIR