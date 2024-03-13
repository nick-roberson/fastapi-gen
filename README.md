# Generate Simple FastAPI Service

This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

CRUD Endpoints for multiple models 
backed by a MongoDB DB.

## Setup

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

This will create a service that manages two simple objects `User` and `Group` with the following fields:
```yaml
# config.yaml
models:
  - name: User
    fields:
      - name: id
        type: str
        required: false
        default: None
        description: The unique identifier of the user
      - name: username
        type: str
        description: The username of the user
        required: true
      - name: email
        type: str
        description: The email of the user
        required: true
  - name: Group
    fields:
      - name: id
        type: str
        required: false
        default: None
        description: The unique identifier of the group
      - name: name
        type: str
        description: The name of the group
        required: true
      - name: users
        type: list
```

Automatically generate the service using the following command:
```bash
% poetry install && poetry update
% poetry run python main.py
Generating models and services with the following inputs
    Input:  examples/models.yaml
    Output: /Users/nicholas/Code/service-builder/output
    
Generated files:
  Models:  /Users/nicholas/Code/service-builder/output/models/models.py
  Service: /Users/nicholas/Code/service-builder/output/service.py
  Manager: ['/Users/nicholas/Code/service-builder/output/user_manager.py', '/Users/nicholas/Code/service-builder/output/group_manager.py']
  Mongo:   /Users/nicholas/Code/service-builder/output/mongo.py

Run the following commands to run the service:
  % cd /Users/nicholas/Code/service-builder/output
  % poetry run uvicorn service:app --reload --port 8000
```

To run the new service 
```bash
% cd output
% poetry run uvicorn service:app --reload --port 8000
```

To view the generated OpenAPI documentation, navigate to [http://localhost:8000/docs](http://localhost:8000/docs).

## API Examples

### Create a User

These can be run pretty easily in Postman:

Add 1 User:
```bash
REQUEST: 
    POST http://localhost:8000/user
BODY: 
    {
      "username": "nicholas",
      "email": "nicholas.roberson.95@gmail.com"
    }
RESPONSE:
    {
      "id": "0f91623b-7f17-41bf-b54d-c068dd8a7191",
      "username": "nicholas",
      "email": "nicholas.roberson.95@gmail.com"
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
      "id": "60f3e3e3e3e3e3e3e3e3e3e3",
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
            "email": "nicholas.roberson.95@gmail.com"
        },
        {
            "id": "ea5ec257-8414-4572-a017-a01b0a36e3a7",
            "username": "test",
            "email": "test@gmail.com"
        }
    ]
```