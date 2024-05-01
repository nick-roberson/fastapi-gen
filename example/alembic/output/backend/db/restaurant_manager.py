import logging
import uuid
from typing import List, Union

from src.db.utils import get_client, get_collection
from src.models.models import Restaurant, RestaurantQuery

logger = logging.getLogger(__name__)

# Singleton Manager for Restaurant
__RESTAURANT_MANAGER = None


def get_restaurant_manager():
    global __RESTAURANT_MANAGER
    if not __RESTAURANT_MANAGER:
        __RESTAURANT_MANAGER = RestaurantManager()
    return __RESTAURANT_MANAGER


class RestaurantManager:

    collection_name: str = "restaurant"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def generate_id(self) -> Union[str, int]:
        """Generate a new id for the User"""
        return str(uuid.uuid4())

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: RestaurantQuery) -> List[Restaurant]:
        """Query Restaurant"""
        logger.info("Querying Restaurant: {}".format(query))
        try:
            # Build query
            query_dict = query.model_dump(mode="json")
            return list(self.collection.find(query_dict))
        except Exception as e:
            logger.error(f"Error querying Restaurant: {e}")
            raise f"Error querying Restaurant: {e}"

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Restaurant) -> Restaurant:
        """Create a new Restaurant"""
        logger.info("Creating Restaurant: {}".format(model))
        try:
            # Generate id for the model
            if not model.id:
                model.id = self.generate_id()

            # Insert into database
            self.collection.insert_one(model.model_dump(mode="json"))

            # Return the created Restaurant
            return model
        except Exception as e:
            logger.error(f"Error creating Restaurant: {e}")
            raise f"Error creating Restaurant: {e}"

    def create_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Create a list of Restaurant"""
        logger.info("Creating Restaurant: {}".format(model_list))
        try:
            # Generate ids for the models
            for model in model_list:
                if not model.id:
                    model.id = self.generate_id()

            # Insert into database
            self.collection.insert_many(
                [model.model_dump(mode="json") for model in model_list]
            )

            # Return the Restaurant list
            return model_list
        except Exception as e:
            logger.error(f"Error creating Restaurants: {e}")
            raise f"Error creating Restaurants: {e}"

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, model_id: str) -> Restaurant:
        """Get a Restaurant by its id"""
        logger.info("Getting Restaurant: {}.format(model_id)")
        try:
            return self.collection.find_one({"id": model_id})
        except Exception as e:
            logger.error(f"Error getting Restaurant: {e}")
            raise f"Error getting Restaurant: {e}"

    def get_many(self, model_ids: List[str]) -> List[Restaurant]:
        """Get a list of Restaurant by their ids"""
        logger.info("Getting Restaurant: {}".format(model_ids))
        try:
            return list(self.collection.find({"id": {"$in": model_ids}}))
        except Exception as e:
            logger.error(f"Error getting Restaurants: {e}")
            raise f"Error getting Restaurants: {e}"

    def get_all(self) -> List[Restaurant]:
        """Get all Restaurant"""
        logger.info(f"Getting all Restaurant")
        try:
            return list(self.collection.find())
        except Exception as e:
            logger.error(f"Error getting all Restaurant: {e}")
            raise f"Error getting all Restaurant: {e}"

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Restaurant) -> Restaurant:
        """Update a Restaurant"""
        logger.info("Updating Restaurant: {}".format(model))
        try:
            # Raise error if id is not present on the model
            if not model.id:
                raise Exception("Restaurant id is required")

            # Update
            self.collection.update_one(
                {"id": model.id}, {"$set": model.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(model.id)
        except Exception as e:
            logger.error(f"Error updating Restaurant: {e}")
            raise f"Error updating Restaurant: {e}"

    def update_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Update a list of Restaurant"""
        logger.info("Updating Restaurant: {}".format(model_list))
        try:
            # Update
            for model in model_list:
                self.update(model)

            # Return new copies
            return self.get_many([model.id for model in model_list])
        except Exception as e:
            logger.error(f"Error updating Restaurants: {e}")
            raise f"Error updating Restaurants: {e}"

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: str) -> Restaurant:
        """Delete a Restaurant"""
        logger.info("Deleting Restaurant: {}".format(model_id))
        try:
            # Find in database
            obj = self.get(model_id)
            if not obj:
                raise Exception("Restaurant not found")

            # Delete if found
            self.collection.delete_one({"id": model_id})

            # Return the deleted object
            return obj
        except Exception as e:
            logger.error(f"Error deleting Restaurant: {e}")
            raise f"Error deleting Restaurant: {e}"

    def delete_many(self, model_ids: List[str]) -> List[Restaurant]:
        """Delete a list of Restaurant"""
        logger.info("Deleting Restaurant: {}".format(model_ids))
        try:
            # Find in database
            objs = self.get_many(model_ids)
            if not objs:
                raise Exception("Restaurants not found")
            if len(objs) != len(model_ids):
                raise Exception("Some Restaurants not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": model_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            logger.error(f"Error deleting Restaurants: {e}")
            raise f"Error deleting Restaurants: {e}"
