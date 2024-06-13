import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from src.db.user_manager import UserManager
from src.models.models import User, UserQuery

# Define Router
router = APIRouter()


def get_manager() -> UserManager:
    """Get the User Manager"""
    return UserManager()


########################################################################################################################
# Query Endpoints for User
########################################################################################################################


@router.post("/user/query")
def query_user(
    query: UserQuery, manager: UserManager = Depends(get_manager)
) -> List[User]:
    """Query Users"""
    logging.info(f"Querying Users with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.model_dump().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in UserQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Users with the given query, if none found raise 404
    models = manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return the Users
    return models


########################################################################################################################
# Get Endpoints for User
########################################################################################################################


@router.get("/user")
def get_user(user_id: str, manager: UserManager = Depends(get_manager)) -> User:
    """Get a User"""
    logging.info(f"Getting User with id: {id}")

    # Get the User with the given id, if none found raise 404
    model = manager.get(user_id=user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    # Return the User
    return model


@router.get("/users")
def get_users(
    skip: int = 0, limit: int = 100, manager: UserManager = Depends(get_manager)
) -> List[User]:
    """Get all Users"""
    logging.info(f"Getting all Users")

    # Get all Users, if none found raise 404
    models = manager.get_all(skip=skip, limit=limit)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return all Users
    return models


########################################################################################################################
# Create Endpoints for User
########################################################################################################################


def _create_user(user: User, manager: UserManager) -> User:
    """Create a User helper function"""
    logging.info(f"Creating User: {str(user)}")

    # Create the User, if failed raise 400
    model = manager.create(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create User")

    # Return the created User
    return model


@router.post("/user")
def create_user(user: User, manager: UserManager = Depends(get_manager)) -> User:
    """Create a User"""
    # Call the helper function to create the User
    return _create_user(user, manager)


@router.post("/user/async")
async def create_user_async(
    user: User,
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Create a User asynchronously"""
    logging.info(f"Creating User asynchronously: {str(user)}")
    # Create the User asynchronously
    background_tasks.add_task(_create_user, user, manager)
    # Return the created User
    return {"message": "Creating User asynchronously"}


def _create_users(users: List[User], manager: UserManager) -> List[User]:
    """Create multiple Users helper function"""
    logging.info(f"Creating Users: {str(users)}")

    # Create the Users, if failed raise 400
    models = manager.create_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Users")

    # Return the created Users
    return models


@router.post("/users")
def create_users(
    users: List[User], manager: UserManager = Depends(get_manager)
) -> List[User]:
    """Create multiple Users"""
    # Call the helper function to create the Users
    return _create_users(users, manager)


@router.post("/users/async")
async def create_users_async(
    users: List[User],
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Create multiple Users asynchronously"""
    logging.info(f"Creating Users asynchronously: {str(users)}")
    # Create the Users asynchronously
    background_tasks.add_task(_create_users, users, manager)
    # Return the created Users
    return {"message": "Creating Users asynchronously"}


########################################################################################################################
# Update Endpoints for User
########################################################################################################################


def _update_user(user: User, manager: UserManager) -> User:
    """Update a User helper function"""
    logging.info(f"Updating User: {str(user)}")

    # Update the User, if failed raise 400
    model = manager.update(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update User")

    # Return the updated User
    return model


@router.put("/user")
def update_user(user: User, manager: UserManager = Depends(get_manager)) -> User:
    """Update a User"""
    # Call the helper function to update the User
    return _update_user(user, manager)


@router.put("/user/async")
async def update_user_async(
    user: User,
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Update a User asynchronously"""
    logging.info(f"Updating User asynchronously: {str(user)}")
    # Update the User asynchronously
    background_tasks.add_task(_update_user, user, manager)
    # Return the updated User
    return {"message": "Updating User asynchronously"}


def _update_users(users: List[User], manager: UserManager) -> List[User]:
    """Update multiple Users helper function"""
    logging.info(f"Updating Users: {str(users)}")

    # Update the Users, if failed raise 400
    models = manager.update_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Users")

    # Return the updated Users
    return models


@router.put("/users")
def update_users(
    users: List[User], manager: UserManager = Depends(get_manager)
) -> List[User]:
    """Update multiple Users"""
    # Call the helper function to update the Users
    return _update_users(users, manager)


@router.put("/users/async")
async def update_users_async(
    users: List[User],
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Update multiple Users asynchronously"""
    logging.info(f"Updating Users asynchronously: {str(users)}")
    # Update the Users asynchronously
    background_tasks.add_task(_update_users, users, manager)
    # Return the updated Users
    return {"message": "Updating Users asynchronously"}


########################################################################################################################
# Delete Endpoints for User
########################################################################################################################


def _delete_user(user_id: int, manager: UserManager) -> User:
    """Delete a User helper function"""
    logging.info(f"Deleting User with id: {id}")

    # Delete the User, if failed raise 404
    model = manager.delete(user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete User")

    # Return the deleted User
    return model


@router.delete("/user")
def delete_user(user_id: int, manager: UserManager = Depends(get_manager)) -> User:
    """Delete a User"""
    # Call the helper function to delete the User
    return _delete_user(user_id, manager)


@router.delete("/user/async")
async def delete_user_async(
    user_id: int,
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Delete a User asynchronously"""
    logging.info(f"Deleting User asynchronously with id: {id}")
    # Delete the User asynchronously
    background_tasks.add_task(_delete_user, user_id, manager)
    # Return the deleted User
    return {"message": "Deleting User asynchronously"}


def _delete_users(user_ids: List[int], manager: UserManager) -> List[User]:
    """Delete multiple Users helper function"""
    logging.info(f"Deleting Users: {str(user_ids)}")

    # Delete the Users, if failed raise 404
    models = manager.delete_many(user_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Users")

    # Return the deleted Users
    return models


@router.delete("/users")
def delete_users(
    user_ids: List[int], manager: UserManager = Depends(get_manager)
) -> List[User]:
    """Delete multiple Users"""
    # Call the helper function to delete the Users
    return _delete_users(user_ids, manager)


@router.delete("/users/async")
async def delete_users_async(
    user_ids: List[int],
    background_tasks: BackgroundTasks,
    manager: UserManager = Depends(get_manager),
):
    """Delete multiple Users asynchronously"""
    logging.info(f"Deleting Users asynchronously: {str(user_ids)}")
    # Delete the Users asynchronously
    background_tasks.add_task(_delete_users, user_ids, manager)
    # Return the deleted Users
    return {"message": "Deleting Users asynchronously"}
