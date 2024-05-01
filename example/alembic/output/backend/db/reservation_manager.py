import logging
import uuid
from typing import List, Union

from src.db.utils import get_client, get_collection
from src.models.models import Reservation, ReservationQuery

logger = logging.getLogger(__name__)

# Singleton Manager for Reservation
__RESERVATION_MANAGER = None


def get_reservation_manager():
    global __RESERVATION_MANAGER
    if not __RESERVATION_MANAGER:
        __RESERVATION_MANAGER = ReservationManager()
    return __RESERVATION_MANAGER


class ReservationManager:

    collection_name: str = "reservation"

    def __init__(self):
        self.client = get_client()
        self.collection = get_collection(self.client, self.collection_name)

    def generate_id(self) -> Union[str, int]:
        """Generate a new id for the User"""
        return str(uuid.uuid4())

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: ReservationQuery) -> List[Reservation]:
        """Query Reservation"""
        logger.info("Querying Reservation: {}".format(query))
        try:
            # Build query
            query_dict = query.model_dump(mode="json")
            return list(self.collection.find(query_dict))
        except Exception as e:
            logger.error(f"Error querying Reservation: {e}")
            raise f"Error querying Reservation: {e}"

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Reservation) -> Reservation:
        """Create a new Reservation"""
        logger.info("Creating Reservation: {}".format(model))
        try:
            # Generate id for the model
            if not model.id:
                model.id = self.generate_id()

            # Insert into database
            self.collection.insert_one(model.model_dump(mode="json"))

            # Return the created Reservation
            return model
        except Exception as e:
            logger.error(f"Error creating Reservation: {e}")
            raise f"Error creating Reservation: {e}"

    def create_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Create a list of Reservation"""
        logger.info("Creating Reservation: {}".format(model_list))
        try:
            # Generate ids for the models
            for model in model_list:
                if not model.id:
                    model.id = self.generate_id()

            # Insert into database
            self.collection.insert_many(
                [model.model_dump(mode="json") for model in model_list]
            )

            # Return the Reservation list
            return model_list
        except Exception as e:
            logger.error(f"Error creating Reservations: {e}")
            raise f"Error creating Reservations: {e}"

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, model_id: str) -> Reservation:
        """Get a Reservation by its id"""
        logger.info("Getting Reservation: {}.format(model_id)")
        try:
            return self.collection.find_one({"id": model_id})
        except Exception as e:
            logger.error(f"Error getting Reservation: {e}")
            raise f"Error getting Reservation: {e}"

    def get_many(self, model_ids: List[str]) -> List[Reservation]:
        """Get a list of Reservation by their ids"""
        logger.info("Getting Reservation: {}".format(model_ids))
        try:
            return list(self.collection.find({"id": {"$in": model_ids}}))
        except Exception as e:
            logger.error(f"Error getting Reservations: {e}")
            raise f"Error getting Reservations: {e}"

    def get_all(self) -> List[Reservation]:
        """Get all Reservation"""
        logger.info(f"Getting all Reservation")
        try:
            return list(self.collection.find())
        except Exception as e:
            logger.error(f"Error getting all Reservation: {e}")
            raise f"Error getting all Reservation: {e}"

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Reservation) -> Reservation:
        """Update a Reservation"""
        logger.info("Updating Reservation: {}".format(model))
        try:
            # Raise error if id is not present on the model
            if not model.id:
                raise Exception("Reservation id is required")

            # Update
            self.collection.update_one(
                {"id": model.id}, {"$set": model.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(model.id)
        except Exception as e:
            logger.error(f"Error updating Reservation: {e}")
            raise f"Error updating Reservation: {e}"

    def update_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Update a list of Reservation"""
        logger.info("Updating Reservation: {}".format(model_list))
        try:
            # Update
            for model in model_list:
                self.update(model)

            # Return new copies
            return self.get_many([model.id for model in model_list])
        except Exception as e:
            logger.error(f"Error updating Reservations: {e}")
            raise f"Error updating Reservations: {e}"

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: str) -> Reservation:
        """Delete a Reservation"""
        logger.info("Deleting Reservation: {}".format(model_id))
        try:
            # Find in database
            obj = self.get(model_id)
            if not obj:
                raise Exception("Reservation not found")

            # Delete if found
            self.collection.delete_one({"id": model_id})

            # Return the deleted object
            return obj
        except Exception as e:
            logger.error(f"Error deleting Reservation: {e}")
            raise f"Error deleting Reservation: {e}"

    def delete_many(self, model_ids: List[str]) -> List[Reservation]:
        """Delete a list of Reservation"""
        logger.info("Deleting Reservation: {}".format(model_ids))
        try:
            # Find in database
            objs = self.get_many(model_ids)
            if not objs:
                raise Exception("Reservations not found")
            if len(objs) != len(model_ids):
                raise Exception("Some Reservations not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": model_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            logger.error(f"Error deleting Reservations: {e}")
            raise f"Error deleting Reservations: {e}"
