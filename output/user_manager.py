# Standard Imports
import logging
import uuid
from typing import List

# Import Models
from models.models import User

# Import MongoDB Utils
from mongo import get_client, get_collection

# For each model, generate a list of managers that will handle CRUD operations

# Singleton Manager for User
__USER_MANAGER = None


def get_user_manager():
    global __USER_MANAGER
    if not __USER_MANAGER:
        __USER_MANAGER = UserManager()
    return __USER_MANAGER


class UserManager:

    collection_name: str = "user"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def create(self, user: User) -> User:
        """Create a new User"""
        logging.info("Creating User: {}".format(user))
        try:
            if not user.id:
                user.id = str(uuid.uuid4())
            self.collection.insert_one(user.model_dump(mode="json"))
            return user
        except Exception as e:
            print(e)

    def get_all(self) -> List[User]:
        """Get all User"""
        logging.info(f"Getting all User")
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, user_id: str) -> User:
        """Get a User by its id"""
        logging.info("Getting User: {}.format(user_id)")
        try:
            return self.collection.find_one({"id": user_id})
        except Exception as e:
            print(e)

    def update(self, user: User) -> User:
        """Update a User"""
        logging.info("Updating User: {}".format(user))
        try:
            # Raise error if id is not present on the model
            if not user.id:
                raise Exception("User id is required")

            # Update
            self.collection.update_one(
                {"id": user.id}, {"$set": user.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(user.id)
        except Exception as e:
            print(e)

    def delete(self, user_id: str) -> User:
        """Delete a User"""
        logging.info("Deleting User: {}".format(user_id))
        try:
            # Find in database
            obj = self.get(user_id)
            if not obj:
                raise Exception("User not found")

            # Delete if found
            self.collection.delete_one({"id": user_id})

            # Return the deleted object
            return obj
        except Exception as e:
            print(e)
