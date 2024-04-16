import logging
from datetime import datetime
from typing import List

from db.constants import DB_URL
from db.models import DBRestaurant
from models.models import Restaurant, RestaurantQuery
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

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: RestaurantQuery) -> List[Restaurant]:
        """Query the Restaurant records from the database."""
        logging.info(f"Querying Restaurant records: {query}")
        try:
            with self.session_factory() as session:

                # Build the query
                query_builder = session.query(DBRestaurant)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBRestaurant, key) == value
                        )

                # Execute the query
                items = query_builder.all()
                if not items:
                    return []

                # Return the Restaurant records
                logging.info(f"Successfully queried Restaurant records: {items}")
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to query Restaurant records: {e}")
            raise f"Failed to query Restaurant records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Get Operations                                       #
    ########################################################

    def get(self, model_id: int) -> Restaurant:
        """Retrieve a Restaurant record from the database by its ID."""
        logging.info(f"Retrieving Restaurant record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(model_id)
                if not item:
                    return None

                # Return the Restaurant record
                logging.info(f"Successfully retrieved Restaurant record: {item}")
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Restaurant record: {e}")
            raise f"Failed to retrieve Restaurant record: {e}"
        finally:
            self.close_session()

    def get_many(self, model_ids: List[int]) -> List[Restaurant]:
        """Retrieve multiple Restaurant records from the database by their IDs."""
        logging.info(f"Retrieving multiple Restaurant records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant records by their IDs
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if not items:
                    return []

                # Return the Restaurant records
                logging.info(
                    f"Successfully retrieved multiple Restaurant records: {items}"
                )
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Restaurant records: {e}")
            raise f"Failed to retrieve multiple Restaurant records: {e}"
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
            raise f"Failed to retrieve all Restaurant records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Restaurant) -> Restaurant:
        """Create a new Restaurant record in the database."""
        logging.info(f"Creating new Restaurant record: {model}")
        try:
            with self.session_factory() as session:

                # Create a new Restaurant record
                new_item = DBRestaurant(**model.dict())

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
            raise f"Failed to create new Restaurant record: {e}"
        finally:
            self.close_session()

    def create_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Create multiple new Restaurant records in the database."""
        logging.info(f"Creating multiple new Restaurant records: {model_list}")
        try:
            with self.session_factory() as session:

                # Create new Restaurant records
                new_items = [DBRestaurant(**model.dict()) for model in model_list]

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
            raise f"Failed to create multiple new Restaurant records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Restaurant) -> Restaurant:
        """Update an existing Restaurant record in the database."""
        logging.info(f"Updating Restaurant record with ID {id}: {model}")
        try:
            with self.session_factory() as session:

                # If id is not present on update, raise an exception
                if not model.id:
                    raise Exception("ID is required to update Restaurant record")

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(model.id)
                if not item:
                    raise Exception("Restaurant record does not exist")

                # Update the Restaurant record with the new data
                for key, value in model.dict().items():
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
            raise f"Failed to update Restaurant record: {e}"
        finally:
            self.close_session()

    def update_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Update multiple existing Restaurant records in the database."""
        logging.info(f"Updating multiple Restaurant records: {model_list}")
        try:
            with self.session_factory() as session:
                # Update the Restaurant records with the new data
                updated_items = []

                # Get all the items by id, raise exception if any are missing
                model_ids = [model.id for model in model_list]
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Restaurant records do not exist")

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
            raise f"Failed to update multiple Restaurant records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: int) -> Restaurant:
        """Delete a Restaurant record from the database by its ID."""
        logging.info(f"Deleting Restaurant record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant record by its ID
                item = session.query(DBRestaurant).get(model_id)
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
            raise f"Failed to delete Restaurant record: {e}"
        finally:
            self.close_session()

    def delete_many(self, model_ids: List[int]) -> List[Restaurant]:
        """Delete multiple Restaurant records from the database by their IDs."""
        logging.info(f"Deleting multiple Restaurant records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Restaurant records by their IDs
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
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
            raise f"Failed to delete multiple Restaurant records: {e}"
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
