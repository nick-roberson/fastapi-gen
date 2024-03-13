import logging
import uuid
from typing import List

from models.models import User
from mongo import get_client, get_collection

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

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, user: User) -> User:
        """Create a new User"""
        logging.info("Creating User: {}".format(user))
        try:
            # Generate id for the model
            if not user.id:
                user.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_one(user.model_dump(mode="json"))

            # Return the created User
            return user
        except Exception as e:
            raise e

    def create_many(self, user_list: List[User]) -> List[User]:
        """Create a list of User"""
        logging.info("Creating User: {}".format(user_list))
        try:
            # Generate ids for the models
            for model in user_list:
                if not model.id:
                    model.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_many(
                [user.model_dump(mode="json") for user in user_list]
            )

            # Return the User list
            return user_list
        except Exception as e:
            raise e

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, user_id: str) -> User:
        """Get a User by its id"""
        logging.info("Getting User: {}.format(user_id)")
        try:
            return self.collection.find_one({"id": user_id})
        except Exception as e:
            raise e

    def get_many(self, user_ids: List[str]) -> List[User]:
        """Get a list of User by their ids"""
        logging.info("Getting User: {}".format(user_ids))
        try:
            return list(self.collection.find({"id": {"$in": user_ids}}))
        except Exception as e:
            raise e

    def get_all(self) -> List[User]:
        """Get all User"""
        logging.info(f"Getting all User")
        try:
            return list(self.collection.find())
        except Exception as e:
            raise e

    ########################################################
    # Update Operations                                    #
    ########################################################

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
            raise e

    def update_many(self, user_list: List[User]) -> List[User]:
        """Update a list of User"""
        logging.info("Updating User: {}".format(user_list))
        try:
            # Update
            for user in user_list:
                self.update(user)

            # Return new copies
            return self.get_many([user.id for user in user_list])
        except Exception as e:
            raise e

    ########################################################
    # Delete Operations                                    #
    ########################################################

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
            raise e

    def delete_many(self, user_ids: List[str]) -> List[User]:
        """Delete a list of User"""
        logging.info("Deleting User: {}".format(user_ids))
        try:
            # Find in database
            objs = self.get_many(user_ids)
            if not objs:
                raise Exception("Users not found")
            if len(objs) != len(user_ids):
                raise Exception("Some Users not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": user_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            raise e
