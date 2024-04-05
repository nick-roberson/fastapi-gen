import logging
import uuid
from typing import List

from models.models import Restaurant
from mongo import get_client, get_collection

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

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, restaurant: Restaurant) -> Restaurant:
        """Create a new Restaurant"""
        print("Creating Restaurant: {}".format(restaurant))
        try:
            # Generate id for the model
            if not restaurant.id:
                restaurant.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_one(restaurant.model_dump(mode="json"))

            # Return the created Restaurant
            return restaurant
        except Exception as e:
            raise e

    def create_many(self, restaurant_list: List[Restaurant]) -> List[Restaurant]:
        """Create a list of Restaurant"""
        print("Creating Restaurant: {}".format(restaurant_list))
        try:
            # Generate ids for the models
            for model in restaurant_list:
                if not model.id:
                    model.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_many(
                [restaurant.model_dump(mode="json") for restaurant in restaurant_list]
            )

            # Return the Restaurant list
            return restaurant_list
        except Exception as e:
            raise e

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, restaurant_id: str) -> Restaurant:
        """Get a Restaurant by its id"""
        print("Getting Restaurant: {}.format(restaurant_id)")
        try:
            return self.collection.find_one({"id": restaurant_id})
        except Exception as e:
            raise e

    def get_many(self, restaurant_ids: List[str]) -> List[Restaurant]:
        """Get a list of Restaurant by their ids"""
        print("Getting Restaurant: {}".format(restaurant_ids))
        try:
            return list(self.collection.find({"id": {"$in": restaurant_ids}}))
        except Exception as e:
            raise e

    def get_all(self) -> List[Restaurant]:
        """Get all Restaurant"""
        print(f"Getting all Restaurant")
        try:
            return list(self.collection.find())
        except Exception as e:
            raise e

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, restaurant: Restaurant) -> Restaurant:
        """Update a Restaurant"""
        print("Updating Restaurant: {}".format(restaurant))
        try:
            # Raise error if id is not present on the model
            if not restaurant.id:
                raise Exception("Restaurant id is required")

            # Update
            self.collection.update_one(
                {"id": restaurant.id}, {"$set": restaurant.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(restaurant.id)
        except Exception as e:
            raise e

    def update_many(self, restaurant_list: List[Restaurant]) -> List[Restaurant]:
        """Update a list of Restaurant"""
        print("Updating Restaurant: {}".format(restaurant_list))
        try:
            # Update
            for restaurant in restaurant_list:
                self.update(restaurant)

            # Return new copies
            return self.get_many([restaurant.id for restaurant in restaurant_list])
        except Exception as e:
            raise e

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, restaurant_id: str) -> Restaurant:
        """Delete a Restaurant"""
        print("Deleting Restaurant: {}".format(restaurant_id))
        try:
            # Find in database
            obj = self.get(restaurant_id)
            if not obj:
                raise Exception("Restaurant not found")

            # Delete if found
            self.collection.delete_one({"id": restaurant_id})

            # Return the deleted object
            return obj
        except Exception as e:
            raise e

    def delete_many(self, restaurant_ids: List[str]) -> List[Restaurant]:
        """Delete a list of Restaurant"""
        print("Deleting Restaurant: {}".format(restaurant_ids))
        try:
            # Find in database
            objs = self.get_many(restaurant_ids)
            if not objs:
                raise Exception("Restaurants not found")
            if len(objs) != len(restaurant_ids):
                raise Exception("Some Restaurants not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": restaurant_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            raise e
