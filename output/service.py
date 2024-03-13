import logging

# FastAPI Imports
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Output Imports
from models.models import User, Group

# Typing Imports
from typing import List

# Manager Imports
from user_manager import get_user_manager
from group_manager import get_group_manager


# Create instances of managers for each model

user_manager = get_user_manager()

group_manager = get_group_manager()


logger = logging.getLogger(__name__)

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
    logging.info(f"Creating User: {str(user)}")
    return user_manager.create(user)


@app.post("/group")
def create_group(group: Group) -> Group:
    logging.info(f"Creating Group: {str(group)}")
    return group_manager.create(group)


##############################################
# Update Endpoints for User, Group
##############################################


@app.put("/user")
def update_user(user: User) -> User:
    logging.info(f"Updating User: {str(user)}")
    return user_manager.update(user)


@app.put("/group")
def update_group(group: Group) -> Group:
    logging.info(f"Updating Group: {str(group)}")
    return group_manager.update(group)


##############################################
# Delete Endpoints for User, Group
##############################################


@app.delete("/user/id")
def delete_user(user_id: str):
    return user_manager.delete(user_id=user_id)


@app.delete("/group/id")
def delete_group(group_id: str):
    return group_manager.delete(group_id=group_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5000)
