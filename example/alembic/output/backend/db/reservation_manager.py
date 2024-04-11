""" Template for alembic model manager, includes the following endpoints:
- create_model
- create_models
- get_model
- get_models
- update_model
- delete_model
"""

import logging
from datetime import datetime
from typing import List

from db.constants import DB_URL
from db.models import DBReservation
from models.models import Reservation
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

    def get(self, id: int) -> Reservation:
        """Retrieve a Reservation record from the database by its ID."""
        logging.info(f"Retrieving Reservation record with ID: {id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(id)
                if not item:
                    return None

                # Return the Reservation record
                logging.info(f"Successfully retrieved Reservation record: {item}")
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Reservation record: {e}")
            raise e
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
            raise e
        finally:
            self.close_session()

    def create(self, data: Reservation) -> Reservation:
        """Create a new Reservation record in the database."""
        logging.info(f"Creating new Reservation record: {data}")
        try:
            with self.session_factory() as session:

                # Create a new Reservation record
                new_item = DBReservation(**data.dict())

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
            raise e
        finally:
            self.close_session()

    def create_many(self, data: List[Reservation]) -> List[Reservation]:
        """Create multiple new Reservation records in the database."""
        logging.info(f"Creating multiple new Reservation records: {data}")
        try:
            with self.session_factory() as session:

                # Create new Reservation records
                new_items = [DBReservation(**item.dict()) for item in data]

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
            raise e
        finally:
            self.close_session()

    def update(self, data: Reservation) -> Reservation:
        """Update an existing Reservation record in the database."""
        logging.info(f"Updating Reservation record with ID {id}: {data}")
        try:
            with self.session_factory() as session:

                # If id is not present on update, raise an exception
                if not data.id:
                    raise Exception("ID is required to update Reservation record")

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(data.id)
                if not item:
                    raise Exception("Reservation record does not exist")

                # Update the Reservation record with the new data
                for key, value in data.dict().items():
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
            raise e
        finally:
            self.close_session()

    def update_many(self, data: List[Reservation]) -> List[Reservation]:
        """Update multiple existing Reservation records in the database."""
        logging.info(f"Updating multiple Reservation records: {data}")
        try:
            with self.session_factory() as session:
                # Update the Reservation records with the new data
                updated_items = []

                # Get all the items by id, raise exception if any are missing
                model_ids = [item.id for item in data]
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Reservation records do not exist")

                item_map = {item.id: item for item in items}
                update_map = {item.id: item for item in data}

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
            raise e
        finally:
            self.close_session()

    def delete(self, id: int) -> Reservation:
        """Delete a Reservation record from the database by its ID."""
        logging.info(f"Deleting Reservation record with ID: {id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation record by its ID
                item = session.query(DBReservation).get(id)
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
            raise e
        finally:
            self.close_session()

    def delete_many(self, ids: List[int]) -> List[Reservation]:
        """Delete multiple Reservation records from the database by their IDs."""
        logging.info(f"Deleting multiple Reservation records with IDs: {ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Reservation records by their IDs
                items = (
                    session.query(DBReservation).filter(DBReservation.id.in_(ids)).all()
                )
                if len(items) != len(ids):
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
            raise e
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
