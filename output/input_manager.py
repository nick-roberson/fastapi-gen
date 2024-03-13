# Standard Imports
import uuid

# Import Models
from models.models import Input

# Import MongoDB Utils
from mongo.utils import get_collection, get_client

# For each model, generate a list of managers that will handle CRUD operations

# Singleton Manager for Input
__INPUT_MANAGER = None


def get_input_manager():
    global __INPUT_MANAGER
    if not __INPUT_MANAGER:
        __INPUT_MANAGER = InputManager()
    return __INPUT_MANAGER


class InputManager:

    collection_name: str = "input"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def create(self, input: Input) -> Input:
        """Create a new Input"""
        try:
            if not input.id:
                input.id = str(uuid.uuid4())
            self.collection.insert_one(input.dict())
            return input
        except Exception as e:
            print(e)

    def get_all(self) -> list:
        """Get all Input"""
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, input_id: str) -> Input:
        """Get a Input by its id"""
        try:
            return self.collection.find_one({"id": input_id})
        except Exception as e:
            print(e)

    def update(self, input: Input) -> None:
        """Update a Input"""
        try:
            self.collection.update_one({"id": input.id}, {"$set": input.dict()})
        except Exception as e:
            print(e)

    def delete(self, input_id: str) -> None:
        """Delete a Input"""
        try:
            self.collection.delete_one({"id": input_id})
        except Exception as e:
            print(e)
