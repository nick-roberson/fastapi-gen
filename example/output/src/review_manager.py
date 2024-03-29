import logging
import uuid
from typing import List

from models.models import Review
from mongo import get_client, get_collection

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

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, review: Review) -> Review:
        """Create a new Review"""
        logging.info("Creating Review: {}".format(review))
        try:
            # Generate id for the model
            if not review.id:
                review.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_one(review.model_dump(mode="json"))

            # Return the created Review
            return review
        except Exception as e:
            raise e

    def create_many(self, review_list: List[Review]) -> List[Review]:
        """Create a list of Review"""
        logging.info("Creating Review: {}".format(review_list))
        try:
            # Generate ids for the models
            for model in review_list:
                if not model.id:
                    model.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_many(
                [review.model_dump(mode="json") for review in review_list]
            )

            # Return the Review list
            return review_list
        except Exception as e:
            raise e

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, review_id: str) -> Review:
        """Get a Review by its id"""
        logging.info("Getting Review: {}.format(review_id)")
        try:
            return self.collection.find_one({"id": review_id})
        except Exception as e:
            raise e

    def get_many(self, review_ids: List[str]) -> List[Review]:
        """Get a list of Review by their ids"""
        logging.info("Getting Review: {}".format(review_ids))
        try:
            return list(self.collection.find({"id": {"$in": review_ids}}))
        except Exception as e:
            raise e

    def get_all(self) -> List[Review]:
        """Get all Review"""
        logging.info(f"Getting all Review")
        try:
            return list(self.collection.find())
        except Exception as e:
            raise e

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, review: Review) -> Review:
        """Update a Review"""
        logging.info("Updating Review: {}".format(review))
        try:
            # Raise error if id is not present on the model
            if not review.id:
                raise Exception("Review id is required")

            # Update
            self.collection.update_one(
                {"id": review.id}, {"$set": review.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(review.id)
        except Exception as e:
            raise e

    def update_many(self, review_list: List[Review]) -> List[Review]:
        """Update a list of Review"""
        logging.info("Updating Review: {}".format(review_list))
        try:
            # Update
            for review in review_list:
                self.update(review)

            # Return new copies
            return self.get_many([review.id for review in review_list])
        except Exception as e:
            raise e

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, review_id: str) -> Review:
        """Delete a Review"""
        logging.info("Deleting Review: {}".format(review_id))
        try:
            # Find in database
            obj = self.get(review_id)
            if not obj:
                raise Exception("Review not found")

            # Delete if found
            self.collection.delete_one({"id": review_id})

            # Return the deleted object
            return obj
        except Exception as e:
            raise e

    def delete_many(self, review_ids: List[str]) -> List[Review]:
        """Delete a list of Review"""
        logging.info("Deleting Review: {}".format(review_ids))
        try:
            # Find in database
            objs = self.get_many(review_ids)
            if not objs:
                raise Exception("Reviews not found")
            if len(objs) != len(review_ids):
                raise Exception("Some Reviews not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": review_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            raise e
