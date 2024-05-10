import logging
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.constants import get_url
from src.db.models import DBUser
from src.models.models import User, UserQuery

# Singleton Manager for User
__USER_MANAGER = None


def get_user_manager():
    global __USER_MANAGER
    if not __USER_MANAGER:
        __USER_MANAGER = UserManager()
    return __USER_MANAGER


class UserManager:
    """Manager to handle all database operations for the User records."""

    _session_factory = None

    @classmethod
    def get_session_factory(cls):
        if cls._session_factory is None:
            engine = create_engine(get_url())
            cls._session_factory = sessionmaker(bind=engine)
            logging.info("Database engine and session factory initialized")
        return cls._session_factory

    def query(self, query: UserQuery) -> List[User]:
        """Query the User records from the database."""
        logging.info(f"Querying User records: {query}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                query_builder = session.query(DBUser)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBUser, key) == value
                        )
                items = query_builder.all()
                return [User.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to query User records: {e}")
            raise

    def get(self, model_id: int) -> User:
        """Retrieve a User record from the database by its ID."""
        logging.info(f"Retrieving User record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBUser).get(model_id)
                if not item:
                    return None
                return User.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve User record: {e}")
            raise

    def get_many(self, model_ids: List[int]) -> List[User]:
        """Retrieve multiple User records from the database by their IDs."""
        logging.info(f"Retrieving multiple User records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBUser).filter(DBUser.id.in_(model_ids)).all()
                return [User.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve multiple User records: {e}")
            raise

    def get_all(self, skip: int = 0, limit: int = 0) -> List[User]:
        """Retrieve all User records from the database."""
        logging.info(f"Retrieving all User records")
        session_factory = self.get_session_factory()
        try:
            # Get models with pagination enabled
            with session_factory() as session:
                items = session.query(DBUser).offset(skip).limit(limit).all()
                return [User.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve all User records: {e}")
            raise

    def create(self, model: User) -> User:
        """Create a new User record in the database."""
        logging.info(f"Creating new User record: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_item = DBUser(**model.dict())
                new_item.id = None  # Ensuring it's treated as a new record
                session.add(new_item)
                session.commit()
                session.refresh(new_item)
                return User.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new User record: {e}")
            raise

    def create_many(self, model_list: List[User]) -> List[User]:
        """Create multiple new User records in the database."""
        logging.info(f"Creating multiple new User records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_items = [DBUser(**model.dict()) for model in model_list]
                for item in new_items:
                    item.id = None
                session.add_all(new_items)
                session.commit()
                for item in new_items:
                    session.refresh(item)
                return [User.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new User records: {e}")
            raise

    def update(self, model: User) -> User:
        """Update an existing User record in the database."""
        logging.info(f"Updating User record with ID {model.id}: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBUser).get(model.id)
                if not item:
                    raise Exception("User record does not exist")
                for key, value in model.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()
                session.commit()
                session.refresh(item)
                return User.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update User record: {e}")
            raise

    def update_many(self, model_list: List[User]) -> List[User]:
        """Update multiple existing User records in the database."""
        logging.info(f"Updating multiple User records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                model_ids = [model.id for model in model_list]
                items = session.query(DBUser).filter(DBUser.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some User records do not exist")
                item_map = {item.id: item for item in items}
                for model in model_list:
                    item = item_map[model.id]
                    for key, value in model.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()
                session.commit()
                for item in items:
                    session.refresh(item)
                return [User.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to update multiple User records: {e}")
            raise

    def delete(self, model_id: int) -> User:
        """Delete a User record from the database by its ID."""
        logging.info(f"Deleting User record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBUser).get(model_id)
                if not item:
                    raise Exception("User record does not exist")
                session.delete(item)
                session.commit()
                return User.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete User record: {e}")
            raise

    def delete_many(self, model_ids: List[int]) -> List[User]:
        """Delete multiple User records from the database by their IDs."""
        logging.info(f"Deleting multiple User records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBUser).filter(DBUser.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some User records do not exist")
                for item in items:
                    session.delete(item)
                session.commit()
                return [User.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple User records: {e}")
            raise
