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
from db.models import DBUser
from models.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Singleton Manager for User
__USER_MANAGER = None


def get_user_manager():
    global __USER_MANAGER
    if not __USER_MANAGER:
        __USER_MANAGER = UserManager()
    return __USER_MANAGER


class UserManager:
    """User manager to handle all database operations for the User records."""

    def __init__(self):
        """Initialize the CaseManager."""
        engine = create_engine(DB_URL)
        self.session_factory = sessionmaker(bind=engine)
        logging.info("CaseManager successfully initialized")

    def get(self, id: int) -> User:
        """Retrieve a User record from the database by its ID."""
        logging.info(f"Retrieving User record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the User record by its ID
                item = session.query(DBUser).get(id)
                logging.info(f"Successfully retrieved User record: {item}")
                return User.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to retrieve User record: {e}")
            raise e
        finally:
            self.close_session()

    def get_all(self) -> List[User]:
        """Retrieve all User records from the database."""
        logging.info("Retrieving all User records")
        try:
            with self.session_factory() as session:
                # Retrieve all User records
                items = session.query(DBUser).all()
                logging.info(f"Successfully retrieved all User records: {items}")
                return [User.from_orm(item) for item in items]
        except Exception as e:
            logging.error(f"Failed to retrieve all User records: {e}")
            raise e
        finally:
            self.close_session()

    def create(self, data: User) -> User:
        """Create a new User record in the database."""
        logging.info(f"Creating new User record: {data}")
        try:
            with self.session_factory() as session:
                # Create a new User record
                new_item = DBUser(**data.dict())

                # Add the new User record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new User record
                session.refresh(new_item)
                logging.info(f"Successfully created new User record: {new_item}")
                return User.from_orm(new_item)
        except Exception as e:
            logging.error(f"Failed to create new User record: {e}")
            raise e
        finally:
            self.close_session()

    def create_many(self, data: List[User]) -> List[User]:
        """Create multiple new User records in the database."""
        logging.info(f"Creating multiple new User records: {data}")
        try:
            with self.session_factory() as session:
                # Create new User records
                new_items = [DBUser(**item.dict()) for item in data]

                # Add the new User records to the session and commit
                session.add_all(new_items)
                session.commit()

                # Refresh and return the new User records
                for item in new_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully created multiple new User records: {new_items}"
                )
                return [User.from_orm(item) for item in new_items]
        except Exception as e:
            logging.error(f"Failed to create multiple new User records: {e}")
            raise e
        finally:
            self.close_session()

    def update(self, id: int, data: User) -> User:
        """Update an existing User record in the database."""
        logging.info(f"Updating User record with ID {id}: {data}")
        try:
            with self.session_factory() as session:
                # Retrieve the User record by its ID
                item = session.query(DBUser).get(id)

                # Update the User record with the new data
                for key, value in data.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()

                # Commit the changes
                session.commit()

                # Refresh and return the updated User record
                session.refresh(item)
                logging.info(f"Successfully updated User record: {item}")
                return User.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to update User record: {e}")
            raise e
        finally:
            self.close_session()

    def update_many(self, data: List[User]) -> List[User]:
        """Update multiple existing User records in the database."""
        logging.info(f"Updating multiple User records: {data}")
        try:
            with self.session_factory() as session:
                # Update the User records with the new data
                updated_items = []
                for item_data in data:
                    # Retrieve the User record by its ID
                    item = session.query(DBUser).get(item_data.id)

                    # Update the User record with the new data
                    for key, value in item_data.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()

                    # Add the updated User record to the list
                    updated_items.append(item)

                # Commit the changes
                session.commit()

                # Refresh and return the updated User records
                for item in updated_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully updated multiple User records: {updated_items}"
                )
                return [User.from_orm(item) for item in updated_items]
        except Exception as e:
            logging.error(f"Failed to update multiple User records: {e}")
            raise e
        finally:
            self.close_session()

    def delete(self, id: int) -> User:
        """Delete a User record from the database by its ID."""
        logging.info(f"Deleting User record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the User record by its ID
                item = session.query(DBUser).get(id)

                # Delete the User record
                session.delete(item)
                session.commit()

                logging.info(f"Successfully deleted User record: {item}")
                return User.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to delete User record: {e}")
            raise e
        finally:
            self.close_session()

    def delete_many(self, ids: List[int]) -> List[User]:
        """Delete multiple User records from the database by their IDs."""
        logging.info(f"Deleting multiple User records with IDs: {ids}")
        try:
            with self.session_factory() as session:
                # Retrieve the User records by their IDs
                items = session.query(DBUser).filter(DBUser.id.in_(ids)).all()

                # Delete the User records
                for item in items:
                    session.delete(item)
                session.commit()

                logging.info(f"Successfully deleted multiple User records: {items}")
                return [User.from_orm(item) for item in items]
        except Exception as e:
            logging.error(f"Failed to delete multiple User records: {e}")
            raise e
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
