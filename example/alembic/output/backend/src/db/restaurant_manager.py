import logging
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.constants import get_url
from src.db.models import DBRestaurant
from src.models.models import Restaurant, RestaurantQuery

# Singleton Manager for Restaurant
__RESTAURANT_MANAGER = None


def get_restaurant_manager():
    global __RESTAURANT_MANAGER
    if not __RESTAURANT_MANAGER:
        __RESTAURANT_MANAGER = RestaurantManager()
    return __RESTAURANT_MANAGER


class RestaurantManager:
    """Manager to handle all database operations for the Restaurant records."""

    _session_factory = None

    @classmethod
    def get_session_factory(cls):
        if cls._session_factory is None:
            engine = create_engine(get_url())
            cls._session_factory = sessionmaker(bind=engine)
            logging.info("Database engine and session factory initialized")
        return cls._session_factory

    def query(self, query: RestaurantQuery) -> List[Restaurant]:
        """Query the Restaurant records from the database."""
        logging.info(f"Querying Restaurant records: {query}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                query_builder = session.query(DBRestaurant)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBRestaurant, key) == value
                        )
                items = query_builder.all()
                return [Restaurant.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to query Restaurant records: {e}")
            raise

    def get(self, model_id: int) -> Restaurant:
        """Retrieve a Restaurant record from the database by its ID."""
        logging.info(f"Retrieving Restaurant record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBRestaurant).get(model_id)
                if not item:
                    return None
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Restaurant record: {e}")
            raise

    def get_many(self, model_ids: List[int]) -> List[Restaurant]:
        """Retrieve multiple Restaurant records from the database by their IDs."""
        logging.info(f"Retrieving multiple Restaurant records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                return [Restaurant.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Restaurant records: {e}")
            raise

    def get_all(self) -> List[Restaurant]:
        """Retrieve all Restaurant records from the database."""
        logging.info(f"Retrieving all Restaurant records")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBRestaurant).all()
                return [Restaurant.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve all Restaurant records: {e}")
            raise

    def create(self, model: Restaurant) -> Restaurant:
        """Create a new Restaurant record in the database."""
        logging.info(f"Creating new Restaurant record: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_item = DBRestaurant(**model.dict())
                new_item.id = None  # Ensuring it's treated as a new record
                session.add(new_item)
                session.commit()
                session.refresh(new_item)
                return Restaurant.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Restaurant record: {e}")
            raise

    def create_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Create multiple new Restaurant records in the database."""
        logging.info(f"Creating multiple new Restaurant records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_items = [DBRestaurant(**model.dict()) for model in model_list]
                for item in new_items:
                    item.id = None
                session.add_all(new_items)
                session.commit()
                for item in new_items:
                    session.refresh(item)
                return [Restaurant.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new Restaurant records: {e}")
            raise

    def update(self, model: Restaurant) -> Restaurant:
        """Update an existing Restaurant record in the database."""
        logging.info(f"Updating Restaurant record with ID {model.id}: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBRestaurant).get(model.id)
                if not item:
                    raise Exception("Restaurant record does not exist")
                for key, value in model.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()
                session.commit()
                session.refresh(item)
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update Restaurant record: {e}")
            raise

    def update_many(self, model_list: List[Restaurant]) -> List[Restaurant]:
        """Update multiple existing Restaurant records in the database."""
        logging.info(f"Updating multiple Restaurant records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                model_ids = [model.id for model in model_list]
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Restaurant records do not exist")
                item_map = {item.id: item for item in items}
                for model in model_list:
                    item = item_map[model.id]
                    for key, value in model.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()
                session.commit()
                for item in items:
                    session.refresh(item)
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to update multiple Restaurant records: {e}")
            raise

    def delete(self, model_id: int) -> Restaurant:
        """Delete a Restaurant record from the database by its ID."""
        logging.info(f"Deleting Restaurant record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBRestaurant).get(model_id)
                if not item:
                    raise Exception("Restaurant record does not exist")
                session.delete(item)
                session.commit()
                return Restaurant.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Restaurant record: {e}")
            raise

    def delete_many(self, model_ids: List[int]) -> List[Restaurant]:
        """Delete multiple Restaurant records from the database by their IDs."""
        logging.info(f"Deleting multiple Restaurant records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = (
                    session.query(DBRestaurant)
                    .filter(DBRestaurant.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Restaurant records do not exist")
                for item in items:
                    session.delete(item)
                session.commit()
                return [Restaurant.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Restaurant records: {e}")
            raise
