import logging
import uuid
from typing import List, Union

from src.db.utils import get_client, get_collection
from src.models.models import User, UserQuery

logger = logging.getLogger(__name__)

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

    def generate_id(self) -> Union[str, int]:
        """Generate a new id for the User"""
        return str(uuid.uuid4())

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: UserQuery) -> List[User]:
        """Query User"""
        logger.info("Querying User: {}".format(query))
        try:
            # Build query
            query_dict = query.model_dump(mode="json")
            return list(self.collection.find(query_dict))
        except Exception as e:
            logger.error(f"Error querying User: {e}")
            raise f"Error querying User: {e}"

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: User) -> User:
        """Create a new User"""
        logger.info("Creating User: {}".format(model))
        try:
            # Generate id for the model
            if not model.id:
                model.id = self.generate_id()

            # Insert into database
            self.collection.insert_one(model.model_dump(mode="json"))

            # Return the created User
            return model
        except Exception as e:
            logger.error(f"Error creating User: {e}")
            raise f"Error creating User: {e}"

    def create_many(self, model_list: List[User]) -> List[User]:
        """Create a list of User"""
        logger.info("Creating User: {}".format(model_list))
        try:
            # Generate ids for the models
            for model in model_list:
                if not model.id:
                    model.id = self.generate_id()

            # Insert into database
            self.collection.insert_many(
                [model.model_dump(mode="json") for model in model_list]
            )

            # Return the User list
            return model_list
        except Exception as e:
            logger.error(f"Error creating Users: {e}")
            raise f"Error creating Users: {e}"

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, model_id: str) -> User:
        """Get a User by its id"""
        logger.info("Getting User: {}.format(model_id)")
        try:
            return self.collection.find_one({"id": model_id})
        except Exception as e:
            logger.error(f"Error getting User: {e}")
            raise f"Error getting User: {e}"

    def get_many(self, model_ids: List[str]) -> List[User]:
        """Get a list of User by their ids"""
        logger.info("Getting User: {}".format(model_ids))
        try:
            return list(self.collection.find({"id": {"$in": model_ids}}))
        except Exception as e:
            logger.error(f"Error getting Users: {e}")
            raise f"Error getting Users: {e}"

    def get_all(self) -> List[User]:
        """Get all User"""
        logger.info(f"Getting all User")
        try:
            return list(self.collection.find())
        except Exception as e:
            logger.error(f"Error getting all User: {e}")
            raise f"Error getting all User: {e}"

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: User) -> User:
        """Update a User"""
        logger.info("Updating User: {}".format(model))
        try:
            # Raise error if id is not present on the model
            if not model.id:
                raise Exception("User id is required")

            # Update
            self.collection.update_one(
                {"id": model.id}, {"$set": model.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(model.id)
        except Exception as e:
            logger.error(f"Error updating User: {e}")
            raise f"Error updating User: {e}"

    def update_many(self, model_list: List[User]) -> List[User]:
        """Update a list of User"""
        logger.info("Updating User: {}".format(model_list))
        try:
            # Update
            for model in model_list:
                self.update(model)

            # Return new copies
            return self.get_many([model.id for model in model_list])
        except Exception as e:
            logger.error(f"Error updating Users: {e}")
            raise f"Error updating Users: {e}"

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: str) -> User:
        """Delete a User"""
        logger.info("Deleting User: {}".format(model_id))
        try:
            # Find in database
            obj = self.get(model_id)
            if not obj:
                raise Exception("User not found")

            # Delete if found
            self.collection.delete_one({"id": model_id})

            # Return the deleted object
            return obj
        except Exception as e:
            logger.error(f"Error deleting User: {e}")
            raise f"Error deleting User: {e}"

    def delete_many(self, model_ids: List[str]) -> List[User]:
        """Delete a list of User"""
        logger.info("Deleting User: {}".format(model_ids))
        try:
            # Find in database
            objs = self.get_many(model_ids)
            if not objs:
                raise Exception("Users not found")
            if len(objs) != len(model_ids):
                raise Exception("Some Users not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": model_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            logger.error(f"Error deleting Users: {e}")
            raise f"Error deleting Users: {e}"
