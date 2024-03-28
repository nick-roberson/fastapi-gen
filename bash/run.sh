
# Make sure the test directory exists
TEST_DIR=test_output
mkdir -p $TEST_DIR

# Run the generator
VERBOSE=1 && poetry run python main.py generate \
    --config example/configs/user_groups.yaml \
    --output-dir $TEST_DIR \
    --service-name test-app

# Clean up the output directory
rm -rf $TEST_DIR
