<h1 align="center"> A CLI for FastAPI + React Service Generation </h1>

<p align="center" markdown=1>
    <i>
        Create proof-of-concept FastAPI services with React frontends effortlessly using a simple CLI tool. 
        Database support includes MongoDB, PostgreSQL, and MySQL.
        ... Collaborators are always welcome!
    </i>
</p>

<h3 align="center">Backend</h3>
<p align="center">
    <a href="">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    </a>
    <a href="https://fastapi.tiangolo.com"> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
    </a>
    <a href="https://docs.pydantic.dev/2.4/">
        <img src="https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=fff&style=for-the-badge" alt="Pydantic">
    </a>
    <a href="https://www.docker.com/">
        <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    </a>
</p>

<h3 align="center">Database </h3>
<p align="center">
    <a href="https://www.mongodb.com/">
        <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
    </a>
    <a href="https://www.sqlalchemy.org/">
        <img src="https://img.shields.io/badge/SQLAlchemy-3178C6?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
    </a>
    <a href="https://www.postgresql.org/">
        <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
    </a>
    <a href="https://www.mysql.com/">
        <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
    </a>

<h3 align="center">Frontend</h3>

<p align="center">
    <a href="https://www.typescriptlang.org/">
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
    </a>
    <a href="https://reactjs.org/">
        <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React">
    </a>
</p>


<h3 align="center">Future Additions</h3>
<p align="center">
    <a href="https://docs.celeryq.dev/en/stable/">
        <img src="https://img.shields.io/badge/Celery-b0cc54?style=for-the-badge&logo=celery&logoColor=white" alt="Celery">
    </a>
    <a href="https://redis.com/">
      <img src="https://img.shields.io/badge/Redis-E92063?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
    </a>
</p>

**Mongo DB Integration is lagging behind the MySQL / PostrgreSQL implementation... working to bring them back into sync!**

_**NOTE:**_
- _This project is actively under development and not yet intended for production usage, although it functions well for general use cases and POCs._
- _While the service templates are robust, the generated code is still being refined, and there are ongoing improvements._

**That all being said `fastapi-gen` does a really great job of creating working POC frontend and backend services that can be used 
to quickly prototype ideas and test out new features!** 

So use this and don't worry anymore about some of the more annoying parts of setting up a new services!
In the future I hope to add far more configurability as well as support for more databases and frontend frameworks. See examples below for more information! 

# Table of Contents

- [Features](#features)
  - [Python Code Generation](#python-code-generation)
  - [Database Generation](#database-generation)
  - [Frontend Code Generation](#frontend-code-generation)
- [Images](#images)
- [Loom Video](#loom-video)
- [Example](#example)
- [Setup](#setup)
- [Usage](#usage)
- [Running](#running)
  - [Back End](#back-end)
  - [Front End](#front-end)
  - [Regenerating Templated Files](#regenerating-templated-files)
- [Test Data](#test-data)



This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

####  Python Code Generation

1. Generate FastAPI services with database support for MongoDB, PostgreSQL, or MySQL
2. Automatically creates endpoints that cover the following areas:
   1. _Synchronous and Asynchronous_
      1. `/create` + `/create_many`
      2. `/update` + `/update_many`
      3. `/delete` + `/delete_many`
   2. _Synchronous Only_
      1. `/get` + `/get_many`, + `/get_all`
      2. `/query`
3. Generate `pydantic` models for the FastAPI services and handle conversion to and from the database models
4. Generate Python client code for the FastAPI service + other python services using `openapi-generator` for use elsewhere

#### Database Generation

1. Generate a `MongoDB` database with `Pydantic` models
2. Generate a `PostgreSQL` database with `SQLAlchemy` + `Alembic` models
3. Generate a `MySQL` database with `SQLAlchemy` + `Alembic` models

In the event that you are using PostgreSQL or MySQL, you will need to set up a local database or 
use a cloud service like AWS RDS or Google Cloud SQL.

#### Frontend Code Generation

1. Creates an entire React frontend that can interact with the FastAPI service
   - Create a homepage that displays all the models that have been generated
   - Create a page for each model that allows you to interact with the FastAPI service
2. All frontend code is generated using `TypeScript` and `React`
3. Generated TypeScript client and models are used to interact with the FastAPI service
4. No work requred on your end to set up the frontend, just run the commands and you are good to go! (assuming you have `npm` installed)

## Images

<div style="padding: 50px;">
  <img src="images/home_page.png" alt="Home Page" />
</div>

Here is an example of the homepage that is generated for the React frontend. It will display all the models that have been generated.

<div style="padding: 100px;">
  <img src="images/reservation_page.png" alt="Reservations Page" style="width: 100%; height: auto; max-width: 35vw;">
</div>

All models will have a page similar to the one above, where you can interact with the FastAPI service.

## Loom Video

You can find a brief demo here!
- [Demo Video](https://www.loom.com/share/c49335aed3db41539aa8d4fee8e5c52e?sid=3ba0b976-d0f1-4827-b4ed-dcbc4d5249a4)

## Example

You can find an example config for both `MongoDB` and `MySQL + Alembic` in the `example/` directory
under their respective folders.

In addition, there is a full generated example of a `Restaurant` service in the `example/alembic/output` directory.
You should be able to run the service and frontend by following the instructions below so long as you have all the
correct environment variables set (see the `setup` section for more information).


## Setup

**General**
- Poetry installed
- Python 3.12.2 installed (can install via poetry)
-
**Database**
- If using **MongoDB** as the database, you will need to set up a free tier MongoDB Atlas database as well as have `MONGO_URI` set in your environment variables.
- If using **PostgreSQL** or **MySQL** as the database, you will need to set up either database locally or somewhere else and have the following environment variables set:
  - `DB_USER`
  - `DB_PASSWORD`
  - `DB_HOST`
  - `DB_PORT`
  - `DB_NAME`
- The options in the config for the `db_type` are `mongo`, `postgres`, and `mysql`

To learn more about how to set up a free tier MongoDB Atlas database,
see the following link: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Click "Try Free" and follow the instructions to set up a free tier database

**Poetry**

All you should need to do before running otherwise is to install the dependencies using poetry.
```bash
% poetry install
```

## Usage

This is the CLI interface for the service generator:
```bash
% poetry run python main.py --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                                                                                │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the installation. [default: None]                                         │
│ --help                                                       Show this message and exit.                                                                                                                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ generate-app                                        Generate a FastAPI backend and React frontend from the input yaml config.                                                                                                   │
│ generate-python-app                                 Generate a FastAPI backend from the input yaml config.                                                                                                                      │
│ generate-test-data                                  Generate fake data for the service                                                                                                                                          │
│ generate-typescript-app                             Generate a React frontend from the input yaml config.                                                                                                                       │
│ regenerate-templates                                Just regenerate the frontend or backend templates, do not recreate the application                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

You can find an example config file in the `example/` directory. There should be one for `MongoDB` and one for `MySQL + Alembic`.
This setup should also work for Postgres, but I have not tested it yet.

### Generate using Alembic

Once you have your config ready (or you can use the example config), you can generate the service using the following command:
```bash
% poetry run python main.py generate-app \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output

...

Run Backend (Poetry):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/backend
    % poetry install && poetry update
    % poetry run uvicorn service:app --reload --port 8000

Run Backend (Docker) (Make sure to fill out the generated .env file!):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/backend
    % docker build -t reservations-app .
    % docker run -p 8000:8000 reservations-app

Run Frontend (NPM):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/reservations-app
    % npm install && npm run start
```

### Generate using Mongo

```bash
% poetry run python main.py generate-app \
    --config example/mongo/restaurant.yaml \
    --output-dir example/mongo/output

...

Run Backend (Poetry):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/backend
    % poetry install && poetry update
    % poetry run uvicorn service:app --reload --port 8000

Run Backend (Docker) (Make sure to fill out the generated .env file!):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/backend
    % docker build -t reservations-app .
    % docker run -p 8000:8000 reservations-app

Run Frontend (NPM):
    % cd /Users/nicholas/Code/fastapi-gen/example/alembic/output/reservations-app
    % npm install && npm run start
```

## Running

### Back End

**Local:**
```
% cd example/alembic/output/backend
% poetry install && poetry update
% poetry run uvicorn service:app --reload --port 8000
```

**Docker:**
```
% cd example/alembic/output/backend
% docker build -t reservations-app .
% docker run -p 8000:8000 reservations-app
```

To view the generated OpenAPI documentation, navigate to [http://localhost:8000/docs](http://localhost:8000/docs).

### Front End

```
% cd example/alembic/output/reservations-app
% npm install && npm run start
```

### Regenerating Templated Files

If you want to regenerate the templates for the frontend or backend, you can use the `regenerate-templates` command.

Alembic Example:
```bash
% poetry run python main.py regenerate-templates frontend \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```
Mongo Example:
```bash
% poetry run python main.py regenerate-templates frontend \
    --config example/mongo/restaurant.yaml \
    --output-dir example/mongo/output
```

If you want to regenerate the backend templates, you can use the following command:

Alembic Example:
```bash
% poetry run python main.py regenerate-templates backend \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```
Mongo Example:
```bash
% poetry run python main.py regenerate-templates backend \
    --config example/mongo/restaurant.yaml \
    --output-dir example/mongo/output
```

## Test Data

To create some fake data that you can insert into the database, you can use the following command:

```bash
% poetry run python main.py generate-test-data \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output

Creating fake data at /Users/nicholas/Code/fastapi-gen/example/alembic/output/data
Creating fake data for User at /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/User.json
Creating fake data for Restaurant at /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Restaurant.json
Creating fake data for Reservation at /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Reservation.json
Creating fake data for Review at /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Review.json
Generated fake data at
        User: /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/User.json
        Restaurant: /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Restaurant.json
        Reservation: /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Reservation.json
        Review: /Users/nicholas/Code/fastapi-gen/example/alembic/output/data/Review.json
```

This data may not be all that useful for your specific use case, but it can be a good starting point for testing out the service.
Feel free to modify the data as you see fit!

For this specific use case in the example you can run the service given the commands provided above and then use postman 
to POST the data to the service. For example:

```json
(POST) http://localhost:8000/users
[
  {
    "id": 71,
    "username": "serious",
    "email": "authority",
    "phone_number": "management",
    "preferences": [
      "although",
      "manager",
      "computer"
    ],
    "role": "anyone"
  },
  {
    "id": 63,
    "username": "he",
    "email": "class",
    "phone_number": "full",
    "preferences": [
      "involve",
      "share",
      "seem"
    ],
    "role": "draw"
  }
]
```