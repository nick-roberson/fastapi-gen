<h2 align="center"> A CLI for FastAPI + React Service Generation and (eventual) Management </h1>

<p align="center" markdown=1>
    <i>
        Create and manage FastAPI backends and React/Typescript frontends effortlessly using a simple CLI tool. 
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
- [Pre-generated Example Code](#pre-generated-example-code)
- [Setup](#setup)
- [Usage](#usage)
- [End to End Example](#end-to-end-example)
  - [1. Create a Configuration File](#1-create-a-configuration-file)
  - [2. Generate Application Files](#2-generate-application-files)
  - [3. Apply Database Migrations](#3-apply-database-migrations)
  - [4. Run the Service Frontend and Backend](#4-run-the-service-frontend-and-backend)
- [Other Commands](#other-commands)
  - [Reverting Database Migrations](#reverting-database-migrations)
  - [Listing Database Migrations](#listing-database-migrations)
  - [Regenerating Templated Files](#regenerating-templated-files)
  - [Create Test Data](#create-test-data)
- [Example Screenshots](#example-screenshots)
- [Loom Video](#loom-video)


This is a simple FastAPI service that can be used as a starting point for a new project.

## Features

####  Python Code Generation

1. Generate FastAPI services with database support for MongoDB, PostgreSQL, or MySQL
2. Automatically creates endpoints that cover the following areas:
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

## Pre-generated Example Code

You can find an example config for both `MongoDB` and `MySQL + Alembic` in the `example/` directory
under their respective folders.

In addition, there is a full generated example of a `Restaurant` service in the `example/alembic/output` directory.
You should be able to run the service and frontend by following the instructions below so long as you have all the
correct environment variables set (see the `setup` section for more information).


## Setup

**General**
- Poetry installed
- Python 3.12.2 installed (can install via poetry)
- `docker` installed (for backend running)
  - https://docs.docker.com/engine/install/
- `openapi-generator generate` command line tool installed (for python client generation)
  - https://openapi-generator.tech/docs/installation/
- `npm` installed (for frontend running)
  - https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

**Database**
- If using **MongoDB** as the database, you will need to set up a free tier MongoDB Atlas database as well as have `MONGO_URI` set in your environment variables.
- If using **PostgreSQL** or **MySQL** as the database, you will need to set up either database locally or somewhere else and have the following environment variables set:
  - `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`
- The options in the config for the `db_type` are `mongo`, `postgres`, and `mysql`

To learn more about how to set up a free tier MongoDB Atlas database,
see the following link: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Click "Try Free" and follow the instructions to set up a free tier database

**Poetry**

All you should need to do before running otherwise is to install the dependencies using poetry.
```bash
% pip install poetry
% poetry install
```

## Usage

This is the CLI interface for the service generator:
```bash
% poetry run python main.py --help

 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ app          Create a FastAPI backend and/or React frontend from an input yaml config.                                                                                                                  │
│ config       Interactively create a configuration file that can then be used for generating a FastAPI backend and React frontend.                                                                       │
│ data         Generate fake data for the service using Faker (https://faker.readthedocs.io/).                                                                                                            │
│ db           Create and apply migrations to the database for any models that have been created.                                                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Config Commands
```commandline
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ create            Create a new configuration file interactively.                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### App Commands
```commandline
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ create            Generate a FastAPI backend and React frontend from the input yaml config.                                                                                                   │
│ reload            Just regenerate the frontend or backend templates, do not recreate the application.                                                                                         │
│ run-backend       BETA: Run the FastAPI backend from the input yaml config.                                                                                                                   │
│ run-frontend      BETA: Run the React frontend from the input yaml config.                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Data Commands
```commandline
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ create            Generate fake data for the service                                                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Database Commands 
```commandline
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ list                BETA: List all migrations                                                                                                                                                                                   │
│ migrate             BETA: Create migration and apply to the database for any models that have been created                                                                                                                      │
│ revert              BETA: Revert the database to a previous revision                                                                                                                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## End to End Example


### 1. Create a Configuration File

(You can skip this step if you want to use the example configs provided in the `example/` directory)

If you want to create a new service from scratch, you can use the `create` command to create a new config file interactively.
```bash
% poetry run python main.py app generate \
  --output-dir example/new_service
  --config-name new_service.yaml
```
You will be prompted to enter the information about the following areas:
- Service Information
- Database Information
- Model Information

**_This feature is in development and may not work as expected. If you have any issues, please let me know! You can also 
easily copy the configs that I have in the `example/` directory and modify them as needed._**

Once you have your config ready (or you can use the example config), you can generate the service using the following command:

### 2. Generate Application Files
```bash
% poetry run python main.py app create \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output

...

Run Backend (Poetry):
    % poetry run python main.py app run-backend \
        --config example/mongo/restaurant.yaml \
        --output-dir example/mongo/output
        
Run Frontend (NPM):
    % poetry run python main.py app run-frontend \
        --config example/mongo/restaurant.yaml \
        --output-dir example/mongo/output
```

### 3. Apply Database Migrations

If you are using PostgreSQL or MySQL, you can apply the migrations to the database using the following command:
```commandline
% poetry run python main.py db migrate \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```

### 4. Run the Service Frontend and Backend

#### Back End

To run the backend, you can use the following command:
```bash
% poetry run python main.py app run-backend \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```

#### Front End

To run the frontend, you can use the following command:
```bash
% poetry run python main.py app run-frontend \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```

## Other Commands

### Reverting Database Migrations
If you want to revert the database to a previous revision, you can use the following command:
```commandline
% poetry run python main.py db revert \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output \
    --revision <revision>
```

### Listing Database Migrations
If you want to list the migrations that have been applied to the database, you can use the following command:
```commandline
% poetry run python main.py db list \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output \
    --list
```

### Regenerating Templated Files

If you want to reload the frontend templates, you can use the following command:
```bash
% poetry run python main.py app reload --frontend-only \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```

If you want to reload the backend templates, you can use the following command:
```bash
% poetry run python main.py app reload --backend-only \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output
```

You can run both of these commands while the application is running to see the changes take effect. No need
to restart the application!

### Create Test Data

To create some fake data that you can insert into the database, you can use the following command:

```bash
% poetry run python main.py data create \
    --config example/alembic/restaurant.yaml \
    --output-dir example/alembic/output

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

## Example Screenshots

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
