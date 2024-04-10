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
from db.models import DBReview
from models.models import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Singleton Manager for Review
__REVIEW_MANAGER = None


def get_review_manager():
    global __REVIEW_MANAGER
    if not __REVIEW_MANAGER:
        __REVIEW_MANAGER = ReviewManager()
    return __REVIEW_MANAGER


class ReviewManager:
    """Review manager to handle all database operations for the Review records."""

    def __init__(self):
        """Initialize the CaseManager."""
        engine = create_engine(DB_URL)
        self.session_factory = sessionmaker(bind=engine)
        logging.info("CaseManager successfully initialized")

    def get(self, id: int) -> Review:
        """Retrieve a Review record from the database by its ID."""
        logging.info(f"Retrieving Review record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(id)
                logging.info(f"Successfully retrieved Review record: {item}")
                return Review.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to retrieve Review record: {e}")
            raise e
        finally:
            self.close_session()

    def get_all(self) -> List[Review]:
        """Retrieve all Review records from the database."""
        logging.info("Retrieving all Review records")
        try:
            with self.session_factory() as session:
                # Retrieve all Review records
                items = session.query(DBReview).all()
                logging.info(f"Successfully retrieved all Review records: {items}")
                return [Review.from_orm(item) for item in items]
        except Exception as e:
            logging.error(f"Failed to retrieve all Review records: {e}")
            raise e
        finally:
            self.close_session()

    def create(self, data: Review) -> Review:
        """Create a new Review record in the database."""
        logging.info(f"Creating new Review record: {data}")
        try:
            with self.session_factory() as session:
                # Create a new Review record
                new_item = DBReview(**data.dict())

                # Add the new Review record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new Review record
                session.refresh(new_item)
                logging.info(f"Successfully created new Review record: {new_item}")
                return Review.from_orm(new_item)
        except Exception as e:
            logging.error(f"Failed to create new Review record: {e}")
            raise e
        finally:
            self.close_session()

    def create_many(self, data: List[Review]) -> List[Review]:
        """Create multiple new Review records in the database."""
        logging.info(f"Creating multiple new Review records: {data}")
        try:
            with self.session_factory() as session:
                # Create new Review records
                new_items = [DBReview(**item.dict()) for item in data]

                # Add the new Review records to the session and commit
                session.add_all(new_items)
                session.commit()

                # Refresh and return the new Review records
                for item in new_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully created multiple new Review records: {new_items}"
                )
                return [Review.from_orm(item) for item in new_items]
        except Exception as e:
            logging.error(f"Failed to create multiple new Review records: {e}")
            raise e
        finally:
            self.close_session()

    def update(self, id: int, data: Review) -> Review:
        """Update an existing Review record in the database."""
        logging.info(f"Updating Review record with ID {id}: {data}")
        try:
            with self.session_factory() as session:
                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(id)

                # Update the Review record with the new data
                for key, value in data.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()

                # Commit the changes
                session.commit()

                # Refresh and return the updated Review record
                session.refresh(item)
                logging.info(f"Successfully updated Review record: {item}")
                return Review.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to update Review record: {e}")
            raise e
        finally:
            self.close_session()

    def update_many(self, data: List[Review]) -> List[Review]:
        """Update multiple existing Review records in the database."""
        logging.info(f"Updating multiple Review records: {data}")
        try:
            with self.session_factory() as session:
                # Update the Review records with the new data
                updated_items = []
                for item_data in data:
                    # Retrieve the Review record by its ID
                    item = session.query(DBReview).get(item_data.id)

                    # Update the Review record with the new data
                    for key, value in item_data.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()

                    # Add the updated Review record to the list
                    updated_items.append(item)

                # Commit the changes
                session.commit()

                # Refresh and return the updated Review records
                for item in updated_items:
                    session.refresh(item)
                logging.info(
                    f"Successfully updated multiple Review records: {updated_items}"
                )
                return [Review.from_orm(item) for item in updated_items]
        except Exception as e:
            logging.error(f"Failed to update multiple Review records: {e}")
            raise e
        finally:
            self.close_session()

    def delete(self, id: int) -> Review:
        """Delete a Review record from the database by its ID."""
        logging.info(f"Deleting Review record with ID: {id}")
        try:
            with self.session_factory() as session:
                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(id)

                # Delete the Review record
                session.delete(item)
                session.commit()

                logging.info(f"Successfully deleted Review record: {item}")
                return Review.from_orm(item)
        except Exception as e:
            logging.error(f"Failed to delete Review record: {e}")
            raise e
        finally:
            self.close_session()

    def delete_many(self, ids: List[int]) -> List[Review]:
        """Delete multiple Review records from the database by their IDs."""
        logging.info(f"Deleting multiple Review records with IDs: {ids}")
        try:
            with self.session_factory() as session:
                # Retrieve the Review records by their IDs
                items = session.query(DBReview).filter(DBReview.id.in_(ids)).all()

                # Delete the Review records
                for item in items:
                    session.delete(item)
                session.commit()

                logging.info(f"Successfully deleted multiple Review records: {items}")
                return [Review.from_orm(item) for item in items]
        except Exception as e:
            logging.error(f"Failed to delete multiple Review records: {e}")
            raise e
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
