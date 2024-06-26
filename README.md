<h2 align="center"> A CLI for FastAPI + React Service Generation and (eventual) Management </h1>

<p align="center" markdown=1>
    <i>
        Create and manage FastAPI backends and React/Typescript frontends effortlessly using a simple CLI tool. 
        Database support includes PostgreSQL and MySQL.
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

_**NOTE:**_
- _This project is actively under development._
- _While the service templates are robust, the generated code is still being refined, and there are ongoing improvements._

**That all being said `fastapi-gen` does a really great job of creating working POC frontend and backend services that can be used 
to quickly prototype ideas and test out new features!** 

# Table of Contents

- [Features](#features)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Code Contributions](#code-contributions)
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


## Features

**Configuration File Generation**: 
- Create a new configuration file interactively to generate a new service.

**Service Generation**: 
- Generate a FastAPI backend and React frontend from the input yaml config.

**Database Migrations**: 
- Create and apply migrations to the database for any models that have been created.

**Data Generation**: 
- Generate fake data for the service using Faker (https://faker.readthedocs.io/).

Additionally `fastapi-gen` provides an interface for simply running your application as well as reloading changes
to the frontend or backend without having to restart the application.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue using the bug report template. Include as much detail as possible.

### Suggesting Features

I welcome feature suggestions! Please create an issue using the feature request template. Describe the problem you're facing and how your suggestion would solve it.

### Code Contributions

To contribute code, follow these steps:
1. Create a new branch: `git checkout -b my-feature-branch`
2. Make your changes.
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to your fork: `git push origin my-feature-branch`
5. Create a pull request.

## Pre-generated Example Code

You can find an example config for `MySQL + Alembic` in the `example/` directory
under their respective folders.

In addition, there is a full generated example of a `Restaurant` service in the `example/alembic/output` directory.
You should be able to run the service and frontend by following the instructions below so long as you have all the
correct environment variables set (see the `setup` section for more information).


## Setup

**General Requirements**
- `poetry` installed
  - `pip install poetry`
- Python 3.12.2 installed (can install via poetry)
- `docker` installed (for backend running)
  - https://docs.docker.com/engine/install/
- `openapi-generator generate` command line tool installed (for python client generation)
  - https://openapi-generator.tech/docs/installation/
- `npm` installed (for frontend running)
  - https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
- If using postgres as the database
  - `brew install libpq`


**Database**
- If using **PostgreSQL** or **MySQL** as the database, you will need to set up either database locally or somewhere else and have the following environment variables set:
  - `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`
- The options in the config for the `db_type` are `postgres` and `mysql`

**Install from Source**

```bash
% git clone git@github.com:nick-roberson/fastapi-gen.git
% cd fastapi-gen
% poetry install
% poetry run builder --help
```

## Usage

Overall CLI structure:
```commandline
main
  |_ config                  - Configuration file management.
  |     \_ create            - Create a new configuration file interactively.
  |
  |_ app                     - Application management.      
  |     |_ create            - Generate a FastAPI backend and React frontend from the input yaml config.
  |     |_ reload            - Just regenerate the frontend or backend templates, do not recreate the application.
  |     |_ run-backend       - Run the FastAPI backend from the input yaml config.
  |     \_ run-frontend      - Run the React frontend from the input yaml config.
  |
  |_ data                    - Data management.
  |     \_ create            - Generate fake data for the service.
  |
  |_ db                      - Database management.
        |_ list              - List all migrations.
        |_ migrate           - Create migration and apply to the database for any models that have been created.
        \_ revert            - Revert the database to a previous revision.
```
## End to End Example

### 1. Create a Configuration File

(You can skip this step if you want to use the example configs provided in the `example/` directory)

If you want to create a new service from scratch, you can use the `create` command to create a new config file interactively.
```bash
% poetry run builder app generate \
  --config output/new_service.yaml
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
% poetry run builder app create \
  --config example/alembic/restaurant.yaml 

...

1. Apply new migrations:
  % poetry run builder db migrate \
      --config example/alembic/restaurant.yaml \
      --message 'Initial migration for restaurant_app'

2. Run backend:
  % poetry run builder app run-backend \
      --config example/alembic/restaurant.yaml

3. Run frontend:
  % poetry run builder app run-frontend \
      --config example/alembic/restaurant.yaml
```

### 3. Create and Apply Database Migrations

If you are using PostgreSQL or MySQL, you can apply the migrations to the database using the following command:
```commandline
poetry run builder db migrate \
    --config example/alembic/restaurant.yaml \
    --message 'Initial migration for restaurant_app'
```

### 4. Run the Service Frontend and Backend

#### Back End

To run the backend, you can use the following command:
```commandline
poetry run builder app run-backend \
    --config example/alembic/restaurant.yaml 
```

#### Front End

To run the frontend, you can use the following command:
```commandline
poetry run builder app run-frontend \
    --config example/alembic/restaurant.yaml 
```

## Working with an Existing Service

If you have an existing service that you want to work with, you can use the following commands to manage the service.

### Reload the Frontend or Backend

If you want to reload the frontend or backend templates, you can use the following command:
```commandline
poetry run builder app reload \
    --config example/alembic/restaurant.yaml \
    --frontend-only
    
poetry run builder app reload \
    --config example/alembic/restaurant.yaml \
    --backend-only
```

### Update the Database

If you have made changes to the models and want to update the database, you can use the following command:
```commandline
poetry run builder db migrate \
    --config example/alembic/restaurant.yaml \
    --message 'Update models for restaurant_app'
```


## Other Commands

### Reverting Database Migrations

If you want to revert the database to a previous revision, you can use the following command:
```commandline
poetry run builder db revert \
    --config example/alembic/restaurant.yaml  \
    --revision <revision>
```

### Listing Database Migrations

If you want to list the migrations that have been applied to the database, you can use the following command:
```commandline
poetry run builder db list \
    --config example/alembic/restaurant.yaml
```

You can run both of these commands while the application is running to see the changes take effect. No need
to restart the application!

### Create Test Data

To create some fake data that you can insert into the database, you can use the following command:

```commandline
poetry run builder data create \
  --config example/alembic/restaurant.yaml 

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

```
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
