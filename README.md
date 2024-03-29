# FastAPI Service Generator



This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

### Backend Generation
- [x] Generate FastAPI service from a YAML file
- [x] Generate Pydantic base models from a YAML file
- [x] Generate MongoDB manager from a YAML file
- [x] Generate CRUD operations for each model in the YAML
- [x] Generate Poetry file and install dependencies
### Frontend Generation
- [x] Generate a React frontend as Sample Application
- [x] Generate frontend React API Client for the FastAPI service using openapi-generator
- [x] Install some basic dependencies for the frontend
### Planned Features
- [ ] Allow support for multiple database types (Postgres, MySQL, etc.)
- [ ] Generate a Dockerfile for the service
- [ ] Allow for more complex relationships between models
- [ ] Generate a more complex frontend application for the service with some basic features

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

This will create a service that manages two simple objects `User` and `Group` with the following fields:
```yaml
# Database Config
database:
  db_type: mongo
  db_uri_env_var: MONGO_DB_URI

# Model Definitions
models:

  # User model
  - name: User
    fields:
      - name: id
        type: str
        required: false
        default: None
        description: The unique identifier of the user
      - name: username
        type: str
        required: true
        description: The username of the user
      - name: email
        type: str
        required: true
        description: The email of the user
      - name: location
        type: str
        required: false
        default: null
        description: The location of the user
      - name: age
        type: int
        required: false
        default: null
        description: The age of the user
      - name: team
        type: str
        required: false
        default: null
        description: The team name of the user

  # Group model
  - name: Group
    fields:
      - name: id
        type: str
        required: false
        default: None
        description: The unique identifier of the group
      - name: name
        type: str
        required: true
        description: The name of the group
      - name: users
        type: list
        required: true
        description: The users in the group
```

Automatically generate the service using the following command:
```bash
% poetry install && poetry update
% VERBOSE=0 && poetry run python main.py generate \
    --config data/configs/user_groups.yaml \
    --output-dir data/output \
    --service-name nicks-app

Generating models and services with the following inputs
    Input:  /Users/nicholas/Code/service-builder/data/configs/user_groups.yaml
    Output: /Users/nicholas/Code/service-builder/data/output
    Service Name: nicksapp
    Frontend Only: False
    Backend Only: False
    
BACKEND: Completed clearing the output directory.
BACKEND: Completed generating models and services.
BACKEND: Completed installing dependencies.
BACKEND: Completed exporting OpenAPI JSON.
BACKEND: Completed linting the code.

FRONTEND: Completed clearing the output directory.
FRONTEND: Completed creating the application.
FRONTEND: Completed installing dependencies.
FRONTEND: Completed creating the application client.
FRONTEND: Completed generating the main page.
FRONTEND: Completed linting the code.

Generated files:
        models: /Users/nicholas/Code/service-builder/data/output/src/models/models.py
        service: /Users/nicholas/Code/service-builder/data/output/src/service.py
        managers: ['/Users/nicholas/Code/service-builder/data/output/src/user_manager.py', '/Users/nicholas/Code/service-builder/data/output/src/group_manager.py']
        mongo: /Users/nicholas/Code/service-builder/data/output/src/mongo.py
        poetry: /Users/nicholas/Code/service-builder/data/output/pyproject.toml
        readme: /Users/nicholas/Code/service-builder/data/output/README.md

Run the following commands to run the service:
  % cd /Users/nicholas/Code/service-builder/data/output
  % poetry run uvicorn service:app --reload --port 8000

Run the following commands to run the frontend:
  % cd /Users/nicholas/Code/service-builder/data/output/nicksapp
  % npm start
```

## Running

### Back End 

Two options, you can either run from your local environment or from the docker container.

Local:
``` 
% cd /Users/nicholas/Code/service-builder/example-output  
% poetry run uvicorn service:app --reload --port 8000
```

Docker:
```
% cd /Users/nicholas/Code/service-builder/example-output
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
