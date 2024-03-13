# Standard Imports
import uuid

# Import Models
from models.models import Task

# Import MongoDB Utils
from mongo.utils import get_collection, get_client

# For each model, generate a list of managers that will handle CRUD operations

# Singleton Manager for Task
__TASK_MANAGER = None


def get_task_manager():
    global __TASK_MANAGER
    if not __TASK_MANAGER:
        __TASK_MANAGER = TaskManager()
    return __TASK_MANAGER


class TaskManager:

    collection_name: str = "task"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def create(self, task: Task) -> Task:
        """Create a new Task"""
        try:
            if not task.id:
                task.id = str(uuid.uuid4())
            self.collection.insert_one(task.dict())
            return task
        except Exception as e:
            print(e)

    def get_all(self) -> list:
        """Get all Task"""
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, task_id: str) -> Task:
        """Get a Task by its id"""
        try:
            return self.collection.find_one({"id": task_id})
        except Exception as e:
            print(e)

    def update(self, task: Task) -> None:
        """Update a Task"""
        try:
            self.collection.update_one({"id": task.id}, {"$set": task.dict()})
        except Exception as e:
            print(e)

    def delete(self, task_id: str) -> None:
        """Delete a Task"""
        try:
            self.collection.delete_one({"id": task_id})
        except Exception as e:
            print(e)
