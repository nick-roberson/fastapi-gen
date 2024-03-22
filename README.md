# FastAPI Service Generator

---

This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

--- 

- [x] Generate FastAPI service from a YAML file
- [x] Generate MongoDB models from a YAML file
- [x] Generate MongoDB manager from a YAML file
- [x] Generate CRUD operations for each model in the YAML

### Planned Features

- [ ] Allow support for multiple database types (Postgres, MySQL, etc.)
- [ ] Generate a Dockerfile for the service
- [ ] Generate Poetry files for the service based on the dependencies in the YAML file


## Requirements

---

- Poetry is installed
- MongoDB Atlas free tier account setup and the `MONGO_URI` environment variable set

## Setup

---

This project runs using poetry and should have all the basic imports declared in the `pyproject.toml` file.
```bash
% poetry install
```
To update 
```bash
% poetry update
```
To add new dependencies
```bash
% poetry add <package>
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

# Dependencies
dependencies:
  - name: "python"
    version: "3.11.7"
  - name: "pydantic"
    version: "^2.6.4"
  - name: "fastapi"
    version: "^0.110.0"
  - name: "uvicorn"
    version: "^0.28.0"
  - name: "pymongo"
    version: "^4.6.2"
  - name: "certifi"
    version: "^2024.2.2"
  - name: "rich"
    version: "^13.7.1"
```

Automatically generate the service using the following command:
```bash
% poetry install && poetry update
% poetry run python main.py generate --config examples/models.yaml --output-dir output

...

Generating models and services with the following inputs
    Input:  examples/models.yaml
    Output: /Users/nicholas/Code/service-builder/output
    
Generated files:
  models:  /Users/nicholas/Code/service-builder/output/models/models.py
  service: /Users/nicholas/Code/service-builder/output/service.py
  manager: ['/Users/nicholas/Code/service-builder/output/user_manager.py', '/Users/nicholas/Code/service-builder/output/group_manager.py']
  mongo:   /Users/nicholas/Code/service-builder/output/mongo.py
  poetry:  /Users/nicholas/Code/service-builder/output/pyproject.toml
  readme:  /Users/nicholas/Code/service-builder/output/README.md
  
Installing dependencies using poetry ...
Installed dependencies!

Run the following commands to run the service:
  % cd /Users/nicholas/Code/service-builder/output
  % poetry run uvicorn service:app --reload --port 8000
```

See the version history of the service:
```bash
% poetry run python main.py versions

Loaded 2 versions:
        Version: 2 - 2024-03-22 10:54:14
        Version: 1 - 2024-03-22 10:51:32
``` 


To lint the code just to make it more readable you can use `black` and `isort`:
```bash
% poetry run black . && poetry run isort .
```

To run the new service 
```bash
% cd /Users/nicholas/Code/service-builder/output
% poetry run uvicorn service:app --reload --port 8000
```

To view the generated OpenAPI documentation, navigate to [http://localhost:8000/docs](http://localhost:8000/docs).

## API Examples

---

### Import into Postman

You can import the API into Postman by following the steps in the following link: [Importing a Collection Using OpenAPI](https://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/)

The OpenAPI documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs). The raw JSON 
for the OpenAPI documentation can be found at [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json).

### Example Requests

#### Create a User

These can be run pretty easily in Postman:

Add 1 User:
```bash
REQUEST: 
    POST http://localhost:8000/user
BODY: 
    {
      "username": "nicholas",
      "email": "my.email@gmail.com"
    }
RESPONSE:
    {
      "id": "0f91623b-7f17-41bf-b54d-c068dd8a7191",
      "username": "nicholas",
      "email": "my.email@gmail.com"
    }
```

Add 2nd User:
```bash
REQUEST: 
    POST http://localhost:8000/user
BODY
    {
      "username": "test",
      "email": "test@gmail.com"
    }
RESPONSE:
    {
      "id": "ea5ec257-8414-4572-a017-a01b0a36e3a7",
      "username": "test",
      "email": "test@gmail.com"
    }
    
```

Get All Users:
```bash
REQUEST: 
    GET http://localhost:8000/users
RESPONSE:
    [
        {
            "id": "0f91623b-7f17-41bf-b54d-c068dd8a7191",
            "username": "nicholas",
            "email": "my.email@gmail.com"
        },
        {
            "id": "ea5ec257-8414-4572-a017-a01b0a36e3a7",
            "username": "test",
            "email": "test@gmail.com"
        }
    ]
```

#### Add a Group

```bash
REQUEST: 
    POST http://localhost:8000/group
BODY:
    {
      "name": "test_group",
      "users": []
    }
RESPONSE:
    {
        "id": "45e4ad8a-9186-4c57-8daa-bf2f0876759c",
        "name": "test_group",
        "users": []
    }
```

Update the group with users from the previous examples:
```bash
REQUEST: 
    PUT http://localhost:8000/group
BODY:
    {
      "id": "45e4ad8a-9186-4c57-8daa-bf2f0876759c",
      "name": "test_group",
      "users": ["0f91623b-7f17-41bf-b54d-c068dd8a7191", "ea5ec257-8414-4572-a017-a01b0a36e3a7"]
    }
RESPONSE:
    None
```

Get All Groups:
```bash
REQUEST: 
    GET http://localhost:8000/groups
RESPONSE:
    [
        {
            "id": "45e4ad8a-9186-4c57-8daa-bf2f0876759c",
            "name": "test_group",
            "users": [
                "0f91623b-7f17-41bf-b54d-c068dd8a7191",
                "ea5ec257-8414-4572-a017-a01b0a36e3a7"
            ]
        }
    ]
```