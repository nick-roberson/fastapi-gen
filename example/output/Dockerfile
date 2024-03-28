# Use an official lightweight Python image.
# https://hub.docker.com/_/python

# Need to have the same version of python as the one used in the generated service
# if you change this it will break the build
FROM python:3.12.1-slim

# Set the working directory in the container
WORKDIR /code

# Install poetry
RUN pip install poetry

# Install poetry requirements
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --ignore-installed --no-cache-dir --upgrade -r requirements.txt

# Test that the installation was successful
RUN python --version
RUN pip --version
RUN uvicorn --version

# Copy local code to the container
COPY . .

# Make sure to expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "service:app", "--port", "8000", "--reload"]
