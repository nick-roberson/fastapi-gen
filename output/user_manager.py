# Standard Imports
import uuid

# Import Models
from models.models import User

# Import MongoDB Utils
from mongo import get_collection, get_client

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
        try:
            if not user.id:
                user.id = str(uuid.uuid4())
            self.collection.insert_one(user.dict())
            return user
        except Exception as e:
            print(e)

    def get_all(self) -> list:
        """Get all User"""
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, user_id: str) -> User:
        """Get a User by its id"""
        try:
            return self.collection.find_one({"id": user_id})
        except Exception as e:
            print(e)

    def update(self, user: User) -> None:
        """Update a User"""
        try:
            self.collection.update_one({"id": user.id}, {"$set": user.dict()})
        except Exception as e:
            print(e)

    def delete(self, user_id: str) -> None:
        """Delete a User"""
        try:
            self.collection.delete_one({"id": user_id})
        except Exception as e:
            print(e)
