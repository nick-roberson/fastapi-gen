# Standard Imports
import logging
import uuid
from typing import List

# Import Models
from models.models import Group

# Import MongoDB Utils
from mongo import get_client, get_collection

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
        logging.info("Creating Group: {}".format(group))
        try:
            if not group.id:
                group.id = str(uuid.uuid4())
            self.collection.insert_one(group.model_dump(mode="json"))
            return group
        except Exception as e:
            print(e)

    def get_all(self) -> List[Group]:
        """Get all Group"""
        logging.info(f"Getting all Group")
        try:
            return list(self.collection.find())
        except Exception as e:
            print(e)

    def get(self, group_id: str) -> Group:
        """Get a Group by its id"""
        logging.info("Getting Group: {}.format(group_id)")
        try:
            return self.collection.find_one({"id": group_id})
        except Exception as e:
            print(e)

    def update(self, group: Group) -> Group:
        """Update a Group"""
        logging.info("Updating Group: {}".format(group))
        try:
            # Raise error if id is not present on the model
            if not group.id:
                raise Exception("Group id is required")

            # Update
            self.collection.update_one(
                {"id": group.id}, {"$set": group.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(group.id)
        except Exception as e:
            print(e)

    def delete(self, group_id: str) -> Group:
        """Delete a Group"""
        logging.info("Deleting Group: {}".format(group_id))
        try:
            # Find in database
            obj = self.get(group_id)
            if not obj:
                raise Exception("Group not found")

            # Delete if found
            self.collection.delete_one({"id": group_id})

            # Return the deleted object
            return obj
        except Exception as e:
            print(e)
