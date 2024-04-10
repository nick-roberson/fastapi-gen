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

    def get(self, id: int) -> DBRestaurant:
        """Retrieve a Restaurant record from the database by its ID."""
        logging.info(f"Retrieving Restaurant record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(id)
                logging.info(f"Successfully retrieved Restaurant record: {item}")
                return item
        except Exception as e:
            logging.error(f"Failed to retrieve Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def get_all(self) -> List[DBRestaurant]:
        """Retrieve all Restaurant records from the database."""
        logging.info("Retrieving all Restaurant records")
        try:
            with self.session_factory() as session:
                # Retrieve all Restaurant records
                items = session.query(DBRestaurant).all()
                logging.info(f"Successfully retrieved all Restaurant records: {items}")
                return items
        except Exception as e:
            logging.error(f"Failed to retrieve all Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def create(self, data: dict) -> DBRestaurant:
        """Create a new Restaurant record in the database."""
        logging.info(f"Creating new Restaurant record: {data}")
        try:
            with self.session_factory() as session:
                # Create a new Restaurant record
                new_item = DBRestaurant(**data)

                # Add the new Restaurant record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new Restaurant record
                session.refresh(new_item)
                logging.info(f"Successfully created new Restaurant record: {new_item}")
                return new_item
        except Exception as e:
            logging.error(f"Failed to create new Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def create_many(self, data: List[dict]) -> List[DBRestaurant]:
        """Create multiple new Restaurant records in the database."""
        logging.info(f"Creating multiple new Restaurant records: {data}")
        try:
            with self.session_factory() as session:
                # Create new Restaurant records
                new_items = [DBRestaurant(**item) for item in data]

                # Add the new Restaurant records to the session and commit
                session.add_all(new_items)
                session.commit()

                # Refresh and return the new Restaurant records
                for item in new_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully created multiple new Restaurant records: {new_items}"
                )
                return new_items
        except Exception as e:
            logging.error(f"Failed to create multiple new Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def update(self, id: int, data: dict) -> DBRestaurant:
        """Update an existing Restaurant record in the database."""
        logging.info(f"Updating Restaurant record with ID {id}: {data}")
        try:
            with self.session_factory() as session:
                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(id)

                # Update the Restaurant record with the new data
                for key, value in data.items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()

                # Commit the changes
                session.commit()

                # Refresh and return the updated Restaurant record
                session.refresh(item)
                logging.info(f"Successfully updated Restaurant record: {item}")
                return item
        except Exception as e:
            logging.error(f"Failed to update Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def update_many(self, data: List[dict]) -> List[DBRestaurant]:
        """Update multiple existing Restaurant records in the database."""
        logging.info(f"Updating multiple Restaurant records: {data}")
        try:
            with self.session_factory() as session:
                # Update the Restaurant records with the new data
                updated_items = []
                for item_data in data:
                    # Retrieve the Restaurant record by its ID
                    item = session.query(DBRestaurant).get(item_data["id"])

                    # Update the Restaurant record with the new data
                    for key, value in item_data.items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()

                    # Add the updated Restaurant record to the list
                    updated_items.append(item)

                # Commit the changes
                session.commit()

                # Refresh and return the updated Restaurant records
                for item in updated_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully updated multiple Restaurant records: {updated_items}"
                )
                return updated_items
        except Exception as e:
            logging.error(f"Failed to update multiple Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def delete(self, id: int) -> DBRestaurant:
        """Delete a Restaurant record from the database by its ID."""
        logging.info(f"Deleting Restaurant record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(id)

                # Delete the Restaurant record
                session.delete(item)
                session.commit()

                logging.info(f"Successfully deleted Restaurant record: {item}")
                return item
        except Exception as e:
            logging.error(f"Failed to delete Restaurant record: {e}")
            raise e
        finally:
            self.close_session()

    def delete_many(self, ids: List[int]) -> List[DBRestaurant]:
        """Delete multiple Restaurant records from the database by their IDs."""
        logging.info(f"Deleting multiple Restaurant records with IDs: {ids}")
        try:
            with self.session_factory() as session:
                # Retrieve the Restaurant records by their IDs
                items = (
                    session.query(DBRestaurant).filter(DBRestaurant.id.in_(ids)).all()
                )

                # Delete the Restaurant records
                for item in items:
                    session.delete(item)
                session.commit()

                logging.info(
                    f"Successfully deleted multiple Restaurant records: {items}"
                )
                return items
        except Exception as e:
            logging.error(f"Failed to delete multiple Restaurant records: {e}")
            raise e
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
