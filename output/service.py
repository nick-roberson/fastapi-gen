import logging
# Typing Imports
from typing import List

# FastAPI Imports
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from group_manager import get_group_manager
# Output Imports
from models.models import Group, User
# Manager Imports
from user_manager import get_user_manager

# Create instances of managers for each model

user_manager = get_user_manager()

group_manager = get_group_manager()


# Create FastAPI App and Allow CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


##############################################
# Get Endpoints for User, Group
##############################################


@app.get("/user")
def get_user(user_id: str):
    logging.info(f"Getting User with id: {id}")
    return user_manager.get(user_id=user_id)


@app.get("/users")
def get_users() -> List[User]:
    logging.info(f"Getting all Users")
    return user_manager.get_all()


@app.get("/group")
def get_group(group_id: str):
    logging.info(f"Getting Group with id: {id}")
    return group_manager.get(group_id=group_id)


@app.get("/groups")
def get_groups() -> List[Group]:
    logging.info(f"Getting all Groups")
    return group_manager.get_all()


##############################################
# Create Endpoints for User, Group
##############################################


@app.post("/user")
def create_user(user: User) -> User:
    """Create a User"""
    logging.info(f"Creating User: {str(user)}")
    return user_manager.create(user)


@app.post("/users")
def create_users(users: List[User]) -> List[User]:
    """Create multiple Users"""
    logging.info(f"Creating Users: {str(users)}")
    return user_manager.create_many(users)


@app.post("/group")
def create_group(group: Group) -> Group:
    """Create a Group"""
    logging.info(f"Creating Group: {str(group)}")
    return group_manager.create(group)


@app.post("/groups")
def create_groups(groups: List[Group]) -> List[Group]:
    """Create multiple Groups"""
    logging.info(f"Creating Groups: {str(groups)}")
    return group_manager.create_many(groups)


##############################################
# Update Endpoints for User, Group
##############################################


@app.put("/user")
def update_user(user: User) -> User:
    """Update a User"""
    logging.info(f"Updating User: {str(user)}")
    return user_manager.update(user)


@app.put("/users")
def update_users(users: List[User]) -> List[User]:
    """Update multiple Users"""
    logging.info(f"Updating Users: {str(users)}")
    return user_manager.udpate_many(users)


@app.put("/group")
def update_group(group: Group) -> Group:
    """Update a Group"""
    logging.info(f"Updating Group: {str(group)}")
    return group_manager.update(group)


@app.put("/groups")
def update_groups(groups: List[Group]) -> List[Group]:
    """Update multiple Groups"""
    logging.info(f"Updating Groups: {str(groups)}")
    return group_manager.udpate_many(groups)


##############################################
# Delete Endpoints for User, Group
##############################################


@app.delete("/user")
def delete_user(user_id: str):
    """Delete a User"""
    logging.info(f"Deleting User with id: {id}")
    return user_manager.delete(user_id=user_id)


@app.delete("/users")
def delete_users(user_ids: List[str]):
    """Delete multiple Users"""
    logging.info(f"Deleting Users: {str(user_ids)}")
    return user_manager.delete_many(user_ids=user_ids)


@app.delete("/group")
def delete_group(group_id: str):
    """Delete a Group"""
    logging.info(f"Deleting Group with id: {id}")
    return group_manager.delete(group_id=group_id)


@app.delete("/groups")
def delete_groups(group_ids: List[str]):
    """Delete multiple Groups"""
    logging.info(f"Deleting Groups: {str(group_ids)}")
    return group_manager.delete_many(group_ids=group_ids)


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Start the server
    uvicorn.run(app, host="localhost", port=8000)
