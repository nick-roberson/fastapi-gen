import logging
import uuid
from typing import List, Union

from src.db.utils import get_client, get_collection
from src.models.models import Review, ReviewQuery

logger = logging.getLogger(__name__)

# Singleton Manager for Review
__REVIEW_MANAGER = None


def get_review_manager():
    global __REVIEW_MANAGER
    if not __REVIEW_MANAGER:
        __REVIEW_MANAGER = ReviewManager()
    return __REVIEW_MANAGER


class ReviewManager:

    collection_name: str = "review"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def generate_id(self) -> Union[str, int]:
        """Generate a new id for the User"""
        return str(uuid.uuid4())

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: ReviewQuery) -> List[Review]:
        """Query Review"""
        logger.info("Querying Review: {}".format(query))
        try:
            # Build query
            query_dict = query.model_dump(mode="json")
            return list(self.collection.find(query_dict))
        except Exception as e:
            logger.error(f"Error querying Review: {e}")
            raise f"Error querying Review: {e}"

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Review) -> Review:
        """Create a new Review"""
        logger.info("Creating Review: {}".format(model))
        try:
            # Generate id for the model
            if not model.id:
                model.id = self.generate_id()

            # Insert into database
            self.collection.insert_one(model.model_dump(mode="json"))

            # Return the created Review
            return model
        except Exception as e:
            logger.error(f"Error creating Review: {e}")
            raise f"Error creating Review: {e}"

    def create_many(self, model_list: List[Review]) -> List[Review]:
        """Create a list of Review"""
        logger.info("Creating Review: {}".format(model_list))
        try:
            # Generate ids for the models
            for model in model_list:
                if not model.id:
                    model.id = self.generate_id()

            # Insert into database
            self.collection.insert_many(
                [model.model_dump(mode="json") for model in model_list]
            )

            # Return the Review list
            return model_list
        except Exception as e:
            logger.error(f"Error creating Reviews: {e}")
            raise f"Error creating Reviews: {e}"

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, model_id: str) -> Review:
        """Get a Review by its id"""
        logger.info("Getting Review: {}.format(model_id)")
        try:
            return self.collection.find_one({"id": model_id})
        except Exception as e:
            logger.error(f"Error getting Review: {e}")
            raise f"Error getting Review: {e}"

    def get_many(self, model_ids: List[str]) -> List[Review]:
        """Get a list of Review by their ids"""
        logger.info("Getting Review: {}".format(model_ids))
        try:
            return list(self.collection.find({"id": {"$in": model_ids}}))
        except Exception as e:
            logger.error(f"Error getting Reviews: {e}")
            raise f"Error getting Reviews: {e}"

    def get_all(self) -> List[Review]:
        """Get all Review"""
        logger.info(f"Getting all Review")
        try:
            return list(self.collection.find())
        except Exception as e:
            logger.error(f"Error getting all Review: {e}")
            raise f"Error getting all Review: {e}"

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Review) -> Review:
        """Update a Review"""
        logger.info("Updating Review: {}".format(model))
        try:
            # Raise error if id is not present on the model
            if not model.id:
                raise Exception("Review id is required")

            # Update
            self.collection.update_one(
                {"id": model.id}, {"$set": model.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(model.id)
        except Exception as e:
            logger.error(f"Error updating Review: {e}")
            raise f"Error updating Review: {e}"

    def update_many(self, model_list: List[Review]) -> List[Review]:
        """Update a list of Review"""
        logger.info("Updating Review: {}".format(model_list))
        try:
            # Update
            for model in model_list:
                self.update(model)

            # Return new copies
            return self.get_many([model.id for model in model_list])
        except Exception as e:
            logger.error(f"Error updating Reviews: {e}")
            raise f"Error updating Reviews: {e}"

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: str) -> Review:
        """Delete a Review"""
        logger.info("Deleting Review: {}".format(model_id))
        try:
            # Find in database
            obj = self.get(model_id)
            if not obj:
                raise Exception("Review not found")

            # Delete if found
            self.collection.delete_one({"id": model_id})

            # Return the deleted object
            return obj
        except Exception as e:
            logger.error(f"Error deleting Review: {e}")
            raise f"Error deleting Review: {e}"

    def delete_many(self, model_ids: List[str]) -> List[Review]:
        """Delete a list of Review"""
        logger.info("Deleting Review: {}".format(model_ids))
        try:
            # Find in database
            objs = self.get_many(model_ids)
            if not objs:
                raise Exception("Reviews not found")
            if len(objs) != len(model_ids):
                raise Exception("Some Reviews not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": model_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            logger.error(f"Error deleting Reviews: {e}")
            raise f"Error deleting Reviews: {e}"
