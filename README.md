<h1 align="center"> FastAPI + React Service Generator </h1>
<p align="center" markdown=1>
  <i>Command line tool for generating POC FastAPI services and UI Templates!</i>
</p>

<p align="center">
  <a href="">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://fastapi.tiangolo.com">
      <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  </a>
  <a href="https://docs.pydantic.dev/2.4/">
      <img src="https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=fff&style=for-the-badge" alt="Pydantic">
  </a>
  <a href="https://www.mongodb.com/">
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  </a>
</p>


This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

### Backend Generation
- [x] Generate FastAPI service
- [x] Generate Pydantic base models
- [x] Generate MongoDB manager
- [x] Generate CRUD+ API Endpoints operations for each model
- [x] Generate Poetry file and install dependencies
- [x] Generate OpenAPI JSON file
- [x] Generate Python API Client for the FastAPI service using openapi-generator

### Frontend Generation
- [x] Generate a React frontend as Sample Application
- [x] Generate frontend React API Client for the FastAPI service using openapi-generator
- [x] Install some basic dependencies for the frontend

### Planned Backend Features
- [ ] Allow support for multiple database types (Postgres, MySQL, etc.)
- [ ] (IN PROGRESS) Generate a Dockerfile for the service
- [ ] Allow for more complex relationships between models

### Planned Frontend Features
- [ ] Generate a more comprehensive frontend application supporting basic CRUD operations

## Requirements

- MongoDB Atlas free tier account setup and the `MONGO_URI` environment variable set

## Setup

This project runs using poetry and should have all the basic imports declared in the `pyproject.toml` file.
```bash
% poetry install && poetry update
```

## Usage

Define a YAML file anywhere that you would like to, it only has to match the format of the example below.

This is the CLI interface for the service generator:
```bash
 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                                                                                │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the installation. [default: None]                                         │
│ --help                                                       Show this message and exit.                                                                                                                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ generate                   Generate the models and services from the input yaml config.                                                                                                                 │
│ revert                     Revert the service to a previous version.                                                                                                                                    │
│ versions                   List all versions of the service that have been generated.                                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For an example of a config that you can use to generate a service, see the `example/configs/user_groups.yaml` file.

Here is an example of the output that you will see when you run the service generator:
```bash
% poetry install && poetry update
% VERBOSE=0 && poetry run python main.py generate \
    --config example/configs/user_groups.yaml \
    --output-dir example/output \
    --service-name nicks-app

Generating models and services with the following inputs
    Input:  /Users/nicholas/Code/service-builder/example/configs/user_groups.yaml
    Output: /Users/nicholas/Code/service-builder/example/output
    Service Name: nicksapp
    Frontend Only: False
    Backend Only: False

Starting generating the backend code...

        BACKEND: Completed clearing the backend code directory.
        BACKEND: Completed generating models and services.
        BACKEND: Completed installing dependencies.
        BACKEND: Completed exporting OpenAPI JSON.

Starting generating the frontend code...

        FRONTEND: Completed clearing the frontend code directory.
        FRONTEND: Completed creating the application.
        FRONTEND: Completed installing dependencies.
        FRONTEND: Completed generating the main page.

Starting generating the client code...

        CLIENTS: Completed clearing the typescript and python client code directories.
        CLIENTS: Completed generating the typescript client code.
        CLIENTS: Completed generating the python client code.

Starting linting the generated code...

        LINT: Completed linting frontend code.
        LINT: Completed linting backend code.

Generated files:
        models: None
        service: /Users/nicholas/Code/service-builder/example/output/src/service.py
        managers: ['/Users/nicholas/Code/service-builder/example/output/src/user_manager.py', '/Users/nicholas/Code/service-builder/example/output/src/group_manager.py']
        mongo: /Users/nicholas/Code/service-builder/example/output/src/mongo.py
        poetry: /Users/nicholas/Code/service-builder/example/output/pyproject.toml
        readme: /Users/nicholas/Code/service-builder/example/output/README.md
        docker: ['/Users/nicholas/Code/service-builder/service_builder/templates/docker//Dockerfile', '/Users/nicholas/Code/service-builder/service_builder/templates/docker//docker-compose.yml']

Run the following commands to run the service:
  % cd /Users/nicholas/Code/service-builder/example/output
  % poetry run uvicorn service:app --reload --port 8000

Run the following commands to run the frontend:
  % cd /Users/nicholas/Code/service-builder/example/output/nicksapp
  % npm start
```

## Running

### Back End

Two options, you can either run from your local environment or from the docker container.

Local:
```
% cd /Users/nicholas/Code/service-builder/output
% poetry run uvicorn service:app --reload --port 8000
```

Docker:
```
% cd /Users/nicholas/Code/service-builder/output
% docker build -t myfastapiapp .
% docker run -p 8000:8000 myfastapiapp
```

To view the generated OpenAPI documentation, navigate to [http://localhost:8000/docs](http://localhost:8000/docs).

### Front End
```
% cd /Users/nicholas/Code/service-builder/example-output/nicksapp
% npm start
```

## Import Config to Postman

You can import the API into Postman by following the steps in the following link: [Importing a Collection Using OpenAPI](https://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/)

The OpenAPI documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs). The raw JSON
for the OpenAPI documentation can be found at [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json).
