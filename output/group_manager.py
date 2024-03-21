import logging
import uuid
from typing import List

from models.models import Group
from mongo import get_client, get_collection

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

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, group: Group) -> Group:
        """Create a new Group"""
        logging.info("Creating Group: {}".format(group))
        try:
            # Generate id for the model
            if not group.id:
                group.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_one(group.model_dump(mode="json"))

            # Return the created Group
            return group
        except Exception as e:
            raise e

    def create_many(self, group_list: List[Group]) -> List[Group]:
        """Create a list of Group"""
        logging.info("Creating Group: {}".format(group_list))
        try:
            # Generate ids for the models
            for model in group_list:
                if not model.id:
                    model.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_many(
                [group.model_dump(mode="json") for group in group_list]
            )

            # Return the Group list
            return group_list
        except Exception as e:
            raise e

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, group_id: str) -> Group:
        """Get a Group by its id"""
        logging.info("Getting Group: {}.format(group_id)")
        try:
            return self.collection.find_one({"id": group_id})
        except Exception as e:
            raise e

    def get_many(self, group_ids: List[str]) -> List[Group]:
        """Get a list of Group by their ids"""
        logging.info("Getting Group: {}".format(group_ids))
        try:
            return list(self.collection.find({"id": {"$in": group_ids}}))
        except Exception as e:
            raise e

    def get_all(self) -> List[Group]:
        """Get all Group"""
        logging.info(f"Getting all Group")
        try:
            return list(self.collection.find())
        except Exception as e:
            raise e

    ########################################################
    # Update Operations                                    #
    ########################################################

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
            raise e

    def update_many(self, group_list: List[Group]) -> List[Group]:
        """Update a list of Group"""
        logging.info("Updating Group: {}".format(group_list))
        try:
            # Update
            for group in group_list:
                self.update(group)

            # Return new copies
            return self.get_many([group.id for group in group_list])
        except Exception as e:
            raise e

    ########################################################
    # Delete Operations                                    #
    ########################################################

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
            raise e

    def delete_many(self, group_ids: List[str]) -> List[Group]:
        """Delete a list of Group"""
        logging.info("Deleting Group: {}".format(group_ids))
        try:
            # Find in database
            objs = self.get_many(group_ids)
            if not objs:
                raise Exception("Groups not found")
            if len(objs) != len(group_ids):
                raise Exception("Some Groups not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": group_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            raise e
