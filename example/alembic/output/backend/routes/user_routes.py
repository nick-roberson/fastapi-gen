import argparse
import logging
from typing import List

import uvicorn
from db.user_manager import get_user_manager
from fastapi import APIRouter, BackgroundTasks, HTTPException
from models.models import User, UserQuery

# Create instances of managers for each model

user_manager = get_user_manager()


# Define Router
router = APIRouter()


########################################################################################################################
# Query Endpoints for User
########################################################################################################################


@router.post("/user/query")
def query_user(query: UserQuery) -> List[User]:
    """Query Users"""
    logging.info(f"Querying Users with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.dict().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in UserQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Users with the given query, if none found raise 404
    models = user_manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return the Users
    return models


########################################################################################################################
# Get Endpoints for User
########################################################################################################################


@router.get("/user")
def get_user(user_id: str) -> User:
    """Get a User"""
    logging.info(f"Getting User with id: {id}")

    # Get the User with the given id, if none found raise 404
    model = user_manager.get(user_id=user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    # Return the User
    return model


@router.get("/users")
def get_users() -> List[User]:
    """Get all Users"""
    logging.info(f"Getting all Users")

    # Get all Users, if none found raise 404
    models = user_manager.get_all()
    if not models:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return all Users
    return models


########################################################################################################################
# Create Endpoints for User
########################################################################################################################


def _create_user(user: User) -> User:
    """Create a User helper function"""
    logging.info(f"Creating User: {str(user)}")

    # Create the User, if failed raise 400
    model = user_manager.create(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create User")

    # Return the created User
    return model


@router.post("/user")
def create_user(user: User) -> User:
    """Create a User"""
    # Call the helper function to create the User
    return _create_user(user)


@router.post("/user/async")
def create_user_async(user: User, background_tasks: BackgroundTasks):
    """Create a User asynchronously"""
    logging.info(f"Creating User asynchronously: {str(user)}")
    # Create the User asynchronously
    background_tasks.add_task(_create_user, user)
    # Return the created User
    return {"message": "Creating User asynchronously"}


def _create_users(users: List[User]) -> List[User]:
    """Create multiple Users helper function"""
    logging.info(f"Creating Users: {str(users)}")

    # Create the Users, if failed raise 400
    models = user_manager.create_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Users")

    # Return the created Users
    return models


@router.post("/users")
def create_users(users: List[User]) -> List[User]:
    """Create multiple Users"""
    # Call the helper function to create the Users
    return _create_users(users)


@router.post("/users/async")
def create_users_async(users: List[User], background_tasks: BackgroundTasks):
    """Create multiple Users asynchronously"""
    logging.info(f"Creating Users asynchronously: {str(users)}")
    # Create the Users asynchronously
    background_tasks.add_task(_create_users, users)
    # Return the created Users
    return {"message": "Creating Users asynchronously"}


########################################################################################################################
# Update Endpoints for User
########################################################################################################################


def _update_user(user: User) -> User:
    """Update a User helper function"""
    logging.info(f"Updating User: {str(user)}")

    # Update the User, if failed raise 400
    model = user_manager.update(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update User")

    # Return the updated User
    return model


@router.put("/user")
def update_user(user: User) -> User:
    """Update a User"""
    # Call the helper function to update the User
    return _update_user(user)


@router.put("/user/async")
def update_user_async(user: User, background_tasks: BackgroundTasks):
    """Update a User asynchronously"""
    logging.info(f"Updating User asynchronously: {str(user)}")
    # Update the User asynchronously
    background_tasks.add_task(_update_user, user)
    # Return the updated User
    return {"message": "Updating User asynchronously"}


def _update_users(users: List[User]) -> List[User]:
    """Update multiple Users helper function"""
    logging.info(f"Updating Users: {str(users)}")

    # Update the Users, if failed raise 400
    models = user_manager.update_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Users")

    # Return the updated Users
    return models


@router.put("/users")
def update_users(users: List[User]) -> List[User]:
    """Update multiple Users"""
    # Call the helper function to update the Users
    return _update_users(users)


@router.put("/users/async")
def update_users_async(users: List[User], background_tasks: BackgroundTasks):
    """Update multiple Users asynchronously"""
    logging.info(f"Updating Users asynchronously: {str(users)}")
    # Update the Users asynchronously
    background_tasks.add_task(_update_users, users)
    # Return the updated Users
    return {"message": "Updating Users asynchronously"}


########################################################################################################################
# Delete Endpoints for User
########################################################################################################################


def _delete_user(user_id: str) -> User:
    """Delete a User helper function"""
    logging.info(f"Deleting User with id: {id}")

    # Delete the User, if failed raise 404
    model = user_manager.delete(user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete User")

    # Return the deleted User
    return model


@router.delete("/user")
def delete_user(user_id: str) -> User:
    """Delete a User"""
    # Call the helper function to delete the User
    return _delete_user(user_id)


@router.delete("/user/async")
def delete_user_async(user_id: str, background_tasks: BackgroundTasks):
    """Delete a User asynchronously"""
    logging.info(f"Deleting User asynchronously with id: {id}")
    # Delete the User asynchronously
    background_tasks.add_task(_delete_user, user_id)
    # Return the deleted User
    return {"message": "Deleting User asynchronously"}


def _delete_users(user_ids: List[str]) -> List[User]:
    """Delete multiple Users helper function"""
    logging.info(f"Deleting Users: {str(user_ids)}")

    # Delete the Users, if failed raise 404
    models = user_manager.delete_many(user_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Users")

    # Return the deleted Users
    return models


@router.delete("/users")
def delete_users(user_ids: List[str]) -> List[User]:
    """Delete multiple Users"""
    # Call the helper function to delete the Users
    return _delete_users(user_ids)


@router.delete("/users/async")
def delete_users_async(user_ids: List[str], background_tasks: BackgroundTasks):
    """Delete multiple Users asynchronously"""
    logging.info(f"Deleting Users asynchronously: {str(user_ids)}")
    # Delete the Users asynchronously
    background_tasks.add_task(_delete_users, user_ids)
    # Return the deleted Users
    return {"message": "Deleting Users asynchronously"}
