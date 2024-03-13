# Standard Imports
import uuid

# Import Models
from models.models import Group

# Import MongoDB Utils
from mongo import get_collection, get_client

# For each model, generate a list of managers that will handle CRUD operations

# Singleton Manager for Group
__GROUP_MANAGER = None


def get_group_manager():
    global __GROUP_MANAGER
    if not __GROUP_MANAGER:
        __GROUP_MANAGER = GroupManager()
    return __GROUP_MANAGER


class GroupManager:

    collection_name: str = "group"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def create(self, group: Group) -> Group:
        """Create a new Group"""
        try:
            if not group.id:
                group.id = str(uuid.uuid4())
            self.collection.insert_one(group.dict())
            return group
        except Exception as e:
            print(e)

    def get_all(self) -> list:
        """Get all Group"""
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, group_id: str) -> Group:
        """Get a Group by its id"""
        try:
            return self.collection.find_one({"id": group_id})
        except Exception as e:
            print(e)

    def update(self, group: Group) -> None:
        """Update a Group"""
        try:
            self.collection.update_one({"id": group.id}, {"$set": group.dict()})
        except Exception as e:
            print(e)

    def delete(self, group_id: str) -> None:
        """Delete a Group"""
        try:
            self.collection.delete_one({"id": group_id})
        except Exception as e:
            print(e)
