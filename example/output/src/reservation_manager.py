import logging
import uuid
from typing import List

from models.models import Reservation
from mongo import get_client, get_collection

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

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, reservation: Reservation) -> Reservation:
        """Create a new Reservation"""
        print("Creating Reservation: {}".format(reservation))
        try:
            # Generate id for the model
            if not reservation.id:
                reservation.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_one(reservation.model_dump(mode="json"))

            # Return the created Reservation
            return reservation
        except Exception as e:
            raise e

    def create_many(self, reservation_list: List[Reservation]) -> List[Reservation]:
        """Create a list of Reservation"""
        print("Creating Reservation: {}".format(reservation_list))
        try:
            # Generate ids for the models
            for model in reservation_list:
                if not model.id:
                    model.id = str(uuid.uuid4())

            # Insert into database
            self.collection.insert_many(
                [
                    reservation.model_dump(mode="json")
                    for reservation in reservation_list
                ]
            )

            # Return the Reservation list
            return reservation_list
        except Exception as e:
            raise e

    ########################################################
    # Read Operations                                      #
    ########################################################

    def get(self, reservation_id: str) -> Reservation:
        """Get a Reservation by its id"""
        print("Getting Reservation: {}.format(reservation_id)")
        try:
            return self.collection.find_one({"id": reservation_id})
        except Exception as e:
            raise e

    def get_many(self, reservation_ids: List[str]) -> List[Reservation]:
        """Get a list of Reservation by their ids"""
        print("Getting Reservation: {}".format(reservation_ids))
        try:
            return list(self.collection.find({"id": {"$in": reservation_ids}}))
        except Exception as e:
            raise e

    def get_all(self) -> List[Reservation]:
        """Get all Reservation"""
        print(f"Getting all Reservation")
        try:
            return list(self.collection.find())
        except Exception as e:
            raise e

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, reservation: Reservation) -> Reservation:
        """Update a Reservation"""
        print("Updating Reservation: {}".format(reservation))
        try:
            # Raise error if id is not present on the model
            if not reservation.id:
                raise Exception("Reservation id is required")

            # Update
            self.collection.update_one(
                {"id": reservation.id}, {"$set": reservation.model_dump(mode="json")}
            )

            # Return new copy
            return self.get(reservation.id)
        except Exception as e:
            raise e

    def update_many(self, reservation_list: List[Reservation]) -> List[Reservation]:
        """Update a list of Reservation"""
        print("Updating Reservation: {}".format(reservation_list))
        try:
            # Update
            for reservation in reservation_list:
                self.update(reservation)

            # Return new copies
            return self.get_many([reservation.id for reservation in reservation_list])
        except Exception as e:
            raise e

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, reservation_id: str) -> Reservation:
        """Delete a Reservation"""
        print("Deleting Reservation: {}".format(reservation_id))
        try:
            # Find in database
            obj = self.get(reservation_id)
            if not obj:
                raise Exception("Reservation not found")

            # Delete if found
            self.collection.delete_one({"id": reservation_id})

            # Return the deleted object
            return obj
        except Exception as e:
            raise e

    def delete_many(self, reservation_ids: List[str]) -> List[Reservation]:
        """Delete a list of Reservation"""
        print("Deleting Reservation: {}".format(reservation_ids))
        try:
            # Find in database
            objs = self.get_many(reservation_ids)
            if not objs:
                raise Exception("Reservations not found")
            if len(objs) != len(reservation_ids):
                raise Exception("Some Reservations not found")

            # Delete if found
            self.collection.delete_many({"id": {"$in": reservation_ids}})

            # Return the deleted objects
            return objs
        except Exception as e:
            raise e
