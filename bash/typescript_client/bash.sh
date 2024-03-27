# Generate Python Client for the API with OpenAPI Generator
# Usage:
#   - bash bash/typescript_client/bash.sh
# Dependencies: 
#   - openapi-generator-cli

OUTPUT_DIR="bash/typescript_client/client"
OPENAPI_JSON="data/example_output/openapi.json"

# Generate config
poetry run python main.py generate-openapi \
    --service-dir data/example_output 

# Generate client
openapi-generator generate \
    -i $OPENAPI_JSON \
    -g typescript-fetch \
    -o $OUTPUT_DIR