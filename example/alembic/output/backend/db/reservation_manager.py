import logging
from datetime import datetime
from typing import List

from db.constants import DB_URL
from db.models import DBReservation
from models.models import Reservation, ReservationQuery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Singleton Manager for Reservation
__RESERVATION_MANAGER = None


def get_reservation_manager():
    global __RESERVATION_MANAGER
    if not __RESERVATION_MANAGER:
        __RESERVATION_MANAGER = ReservationManager()
    return __RESERVATION_MANAGER


class ReservationManager:
    """Reservation manager to handle all database operations for the Reservation records."""

    def __init__(self):
        """Initialize the CaseManager."""
        engine = create_engine(DB_URL)
        self.session_factory = sessionmaker(bind=engine)
        logging.info("CaseManager successfully initialized")

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: ReservationQuery) -> List[Reservation]:
        """Query the Reservation records from the database."""
        logging.info(f"Querying Reservation records: {query}")
        try:
            with self.session_factory() as session:

                # Build the query
                query_builder = session.query(DBReservation)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBReservation, key) == value
                        )

                # Execute the query
                items = query_builder.all()
                if not items:
                    return []

                # Return the Reservation records
                logging.info(f"Successfully queried Reservation records: {items}")
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to query Reservation records: {e}")
            raise f"Failed to query Reservation records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Get Operations                                       #
    ########################################################

    def get(self, model_id: int) -> Reservation:
        """Retrieve a Reservation record from the database by its ID."""
        logging.info(f"Retrieving Reservation record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(model_id)
                if not item:
                    return None

                # Return the Reservation record
                logging.info(f"Successfully retrieved Reservation record: {item}")
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Reservation record: {e}")
            raise f"Failed to retrieve Reservation record: {e}"
        finally:
            self.close_session()

    def get_many(self, model_ids: List[int]) -> List[Reservation]:
        """Retrieve multiple Reservation records from the database by their IDs."""
        logging.info(f"Retrieving multiple Reservation records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation records by their IDs
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if not items:
                    return []

                # Return the Reservation records
                logging.info(
                    f"Successfully retrieved multiple Reservation records: {items}"
                )
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Reservation records: {e}")
            raise f"Failed to retrieve multiple Reservation records: {e}"
        finally:
            self.close_session()

    def get_all(self) -> List[Reservation]:
        """Retrieve all Reservation records from the database."""
        logging.info("Retrieving all Reservation records")
        try:
            with self.session_factory() as session:

                # Retrieve all Reservation records
                items = session.query(DBReservation).all()
                if not items:
                    return []

                # Return the Reservation records
                logging.info(f"Successfully retrieved all Reservation records: {items}")
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve all Reservation records: {e}")
            raise f"Failed to retrieve all Reservation records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Reservation) -> Reservation:
        """Create a new Reservation record in the database."""
        logging.info(f"Creating new Reservation record: {model}")
        try:
            with self.session_factory() as session:

                # Create a new Reservation record
                new_item = DBReservation(**model.dict())

                # Clear the id of the new model to ensure it is created as a new record
                new_item.id = None

                # Add the new Reservation record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new Reservation record
                session.refresh(new_item)
                logging.info(f"Successfully created new Reservation record: {new_item}")
                return Reservation.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Reservation record: {e}")
            raise f"Failed to create new Reservation record: {e}"
        finally:
            self.close_session()

    def create_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Create multiple new Reservation records in the database."""
        logging.info(f"Creating multiple new Reservation records: {model_list}")
        try:
            with self.session_factory() as session:

                # Create new Reservation records
                new_items = [DBReservation(**model.dict()) for model in model_list]

                # Clear the ids of the new models to ensure they are created as new records
                for item in new_items:
                    item.id = None

                # Add the new Reservation records to the session and commit
                session.add_all(new_items)
                session.commit()

                # Refresh and return the new Reservation records
                for item in new_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully created multiple new Reservation records: {new_items}"
                )
                return [Reservation.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new Reservation records: {e}")
            raise f"Failed to create multiple new Reservation records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Reservation) -> Reservation:
        """Update an existing Reservation record in the database."""
        logging.info(f"Updating Reservation record with ID {id}: {model}")
        try:
            with self.session_factory() as session:

                # If id is not present on update, raise an exception
                if not model.id:
                    raise Exception("ID is required to update Reservation record")

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(model.id)
                if not item:
                    raise Exception("Reservation record does not exist")

                # Update the Reservation record with the new data
                for key, value in model.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()

                # Commit the changes
                session.commit()

                # Refresh and return the updated Reservation record
                session.refresh(item)
                logging.info(f"Successfully updated Reservation record: {item}")
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update Reservation record: {e}")
            raise f"Failed to update Reservation record: {e}"
        finally:
            self.close_session()

    def update_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Update multiple existing Reservation records in the database."""
        logging.info(f"Updating multiple Reservation records: {model_list}")
        try:
            with self.session_factory() as session:
                # Update the Reservation records with the new data
                updated_items = []

                # Get all the items by id, raise exception if any are missing
                model_ids = [model.id for model in model_list]
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Reservation records do not exist")

                item_map = {item.id: item for item in items}
                update_map = {model.id: model for model in model_list}

                # Update the items with the new data
                for id, item in item_map.items():
                    new_update = update_map[id]
                    for key, value in new_update.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()
                    updated_items.append(item)

                # Commit the changes
                session.commit()

                # Refresh and return the updated Reservation records
                for item in updated_items:
                    session.refresh(item)

                # Return the updated items
                logging.info(
                    f"Successfully updated multiple Reservation records: {updated_items}"
                )
                return [Reservation.from_orm(item) for item in updated_items]

        except Exception as e:
            logging.error(f"Failed to update multiple Reservation records: {e}")
            raise f"Failed to update multiple Reservation records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: int) -> Reservation:
        """Delete a Reservation record from the database by its ID."""
        logging.info(f"Deleting Reservation record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(model_id)
                if not item:
                    raise Exception("Reservation record does not exist")

                # Delete the Reservation record
                session.delete(item)
                session.commit()

                # Return the deleted Reservation record
                logging.info(f"Successfully deleted Reservation record: {item}")
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Reservation record: {e}")
            raise f"Failed to delete Reservation record: {e}"
        finally:
            self.close_session()

    def delete_many(self, model_ids: List[int]) -> List[Reservation]:
        """Delete multiple Reservation records from the database by their IDs."""
        logging.info(f"Deleting multiple Reservation records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation records by their IDs
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Reservation records do not exist")

                # Delete the Reservation records
                for item in items:
                    session.delete(item)

                # Commit the changes
                session.commit()

                # Return the deleted Reservation records
                logging.info(
                    f"Successfully deleted multiple Reservation records: {items}"
                )
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Reservation records: {e}")
            raise f"Failed to delete multiple Reservation records: {e}"
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
