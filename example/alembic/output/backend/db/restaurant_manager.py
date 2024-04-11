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
from db.models import DBRestaurant
from models.models import Restaurant
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Singleton Manager for Restaurant
__RESTAURANT_MANAGER = None


def get_restaurant_manager():
    global __RESTAURANT_MANAGER
    if not __RESTAURANT_MANAGER:
        __RESTAURANT_MANAGER = RestaurantManager()
    return __RESTAURANT_MANAGER


class RestaurantManager:
    """Restaurant manager to handle all database operations for the Restaurant records."""

    def __init__(self):
        """Initialize the CaseManager."""
        engine = create_engine(DB_URL)
        self.session_factory = sessionmaker(bind=engine)
        logging.info("CaseManager successfully initialized")

    def get(self, id: int) -> Restaurant:
        """Retrieve a Restaurant record from the database by its ID."""
        logging.info(f"Retrieving Restaurant record with ID: {id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(id)
                if not item:
                    return None

                # Return the Restaurant record
                logging.info(f"Successfully retrieved Restaurant record: {item}")
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def get_all(self) -> List[Restaurant]:
        """Retrieve all Restaurant records from the database."""
        logging.info("Retrieving all Restaurant records")
        try:
            with self.session_factory() as session:

                # Retrieve all Restaurant records
                items = session.query(DBRestaurant).all()
                if not items:
                    return []

                # Return the Restaurant records
                logging.info(f"Successfully retrieved all Restaurant records: {items}")
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve all Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def create(self, data: Restaurant) -> Restaurant:
        """Create a new Restaurant record in the database."""
        logging.info(f"Creating new Restaurant record: {data}")
        try:
            with self.session_factory() as session:

                # Create a new Restaurant record
                new_item = DBRestaurant(**data.dict())

                # Clear the id of the new model to ensure it is created as a new record
                new_item.id = None

                # Add the new Restaurant record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new Restaurant record
                session.refresh(new_item)
                logging.info(f"Successfully created new Restaurant record: {new_item}")
                return Restaurant.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def create_many(self, data: List[Restaurant]) -> List[Restaurant]:
        """Create multiple new Restaurant records in the database."""
        logging.info(f"Creating multiple new Restaurant records: {data}")
        try:
            with self.session_factory() as session:

                # Create new Restaurant records
                new_items = [DBRestaurant(**item.dict()) for item in data]

                # Clear the ids of the new models to ensure they are created as new records
                for item in new_items:
                    item.id = None

                # Add the new Restaurant records to the session and commit
                session.add_all(new_items)
                session.commit()

                # Refresh and return the new Restaurant records
                for item in new_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully created multiple new Restaurant records: {new_items}"
                )
                return [Restaurant.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def update(self, data: Restaurant) -> Restaurant:
        """Update an existing Restaurant record in the database."""
        logging.info(f"Updating Restaurant record with ID {id}: {data}")
        try:
            with self.session_factory() as session:

                # If id is not present on update, raise an exception
                if not data.id:
                    raise Exception("ID is required to update Restaurant record")

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(data.id)
                if not item:
                    raise Exception("Restaurant record does not exist")

                # Update the Restaurant record with the new data
                for key, value in data.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()

                # Commit the changes
                session.commit()

                # Refresh and return the updated Restaurant record
                session.refresh(item)
                logging.info(f"Successfully updated Restaurant record: {item}")
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def update_many(self, data: List[Restaurant]) -> List[Restaurant]:
        """Update multiple existing Restaurant records in the database."""
        logging.info(f"Updating multiple Restaurant records: {data}")
        try:
            with self.session_factory() as session:
                # Update the Restaurant records with the new data
                updated_items = []

                # Get all the items by id, raise exception if any are missing
                model_ids = [item.id for item in data]
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Restaurant records do not exist")

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

                # Refresh and return the updated Restaurant records
                for item in updated_items:
                    session.refresh(item)

                # Return the updated items
                logging.info(
                    f"Successfully updated multiple Restaurant records: {updated_items}"
                )
                return [Restaurant.from_orm(item) for item in updated_items]

        except Exception as e:
            logging.error(f"Failed to update multiple Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def delete(self, id: int) -> Restaurant:
        """Delete a Restaurant record from the database by its ID."""
        logging.info(f"Deleting Restaurant record with ID: {id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(id)
                if not item:
                    raise Exception("Restaurant record does not exist")

                # Delete the Restaurant record
                session.delete(item)
                session.commit()

                # Return the deleted Restaurant record
                logging.info(f"Successfully deleted Restaurant record: {item}")
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def delete_many(self, ids: List[int]) -> List[Restaurant]:
        """Delete multiple Restaurant records from the database by their IDs."""
        logging.info(f"Deleting multiple Restaurant records with IDs: {ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant records by their IDs
                items = (
                    session.query(DBRestaurant).filter(DBRestaurant.id.in_(ids)).all()
                )
                if len(items) != len(ids):
                    raise Exception("Some Restaurant records do not exist")

                # Delete the Restaurant records
                for item in items:
                    session.delete(item)

                # Commit the changes
                session.commit()

                # Return the deleted Restaurant records
                logging.info(
                    f"Successfully deleted multiple Restaurant records: {items}"
                )
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
