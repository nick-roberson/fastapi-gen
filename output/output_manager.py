# Standard Imports
import uuid

# Import Models
from models.models import Output

# Import MongoDB Utils
from mongo.utils import get_collection, get_client

# For each model, generate a list of managers that will handle CRUD operations

# Singleton Manager for Output
__OUTPUT_MANAGER = None


def get_output_manager():
    global __OUTPUT_MANAGER
    if not __OUTPUT_MANAGER:
        __OUTPUT_MANAGER = OutputManager()
    return __OUTPUT_MANAGER


class OutputManager:

    collection_name: str = "output"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def create(self, output: Output) -> Output:
        """Create a new Output"""
        try:
            if not output.id:
                output.id = str(uuid.uuid4())
            self.collection.insert_one(output.dict())
            return output
        except Exception as e:
            print(e)

    def get_all(self) -> list:
        """Get all Output"""
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, output_id: str) -> Output:
        """Get a Output by its id"""
        try:
            return self.collection.find_one({"id": output_id})
        except Exception as e:
            print(e)

    def update(self, output: Output) -> None:
        """Update a Output"""
        try:
            self.collection.update_one({"id": output.id}, {"$set": output.dict()})
        except Exception as e:
            print(e)

    def delete(self, output_id: str) -> None:
        """Delete a Output"""
        try:
            self.collection.delete_one({"id": output_id})
        except Exception as e:
            print(e)
