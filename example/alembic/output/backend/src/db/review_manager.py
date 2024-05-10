import logging
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.constants import get_url
from src.db.models import DBReview
from src.models.models import Review, ReviewQuery

# Singleton Manager for Review
__REVIEW_MANAGER = None


def get_review_manager():
    global __REVIEW_MANAGER
    if not __REVIEW_MANAGER:
        __REVIEW_MANAGER = ReviewManager()
    return __REVIEW_MANAGER


class ReviewManager:
    """Manager to handle all database operations for the Review records."""

    _session_factory = None

    @classmethod
    def get_session_factory(cls):
        if cls._session_factory is None:
            engine = create_engine(get_url())
            cls._session_factory = sessionmaker(bind=engine)
            logging.info("Database engine and session factory initialized")
        return cls._session_factory

    def query(self, query: ReviewQuery) -> List[Review]:
        """Query the Review records from the database."""
        logging.info(f"Querying Review records: {query}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                query_builder = session.query(DBReview)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBReview, key) == value
                        )
                items = query_builder.all()
                return [Review.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to query Review records: {e}")
            raise

    def get(self, model_id: int) -> Review:
        """Retrieve a Review record from the database by its ID."""
        logging.info(f"Retrieving Review record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReview).get(model_id)
                if not item:
                    return None
                return Review.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Review record: {e}")
            raise

    def get_many(self, model_ids: List[int]) -> List[Review]:
        """Retrieve multiple Review records from the database by their IDs."""
        logging.info(f"Retrieving multiple Review records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                return [Review.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Review records: {e}")
            raise

    def get_all(self) -> List[Review]:
        """Retrieve all Review records from the database."""
        logging.info(f"Retrieving all Review records")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBReview).all()
                return [Review.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve all Review records: {e}")
            raise

    def create(self, model: Review) -> Review:
        """Create a new Review record in the database."""
        logging.info(f"Creating new Review record: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_item = DBReview(**model.dict())
                new_item.id = None  # Ensuring it's treated as a new record
                session.add(new_item)
                session.commit()
                session.refresh(new_item)
                return Review.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Review record: {e}")
            raise

    def create_many(self, model_list: List[Review]) -> List[Review]:
        """Create multiple new Review records in the database."""
        logging.info(f"Creating multiple new Review records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_items = [DBReview(**model.dict()) for model in model_list]
                for item in new_items:
                    item.id = None
                session.add_all(new_items)
                session.commit()
                for item in new_items:
                    session.refresh(item)
                return [Review.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new Review records: {e}")
            raise

    def update(self, model: Review) -> Review:
        """Update an existing Review record in the database."""
        logging.info(f"Updating Review record with ID {model.id}: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReview).get(model.id)
                if not item:
                    raise Exception("Review record does not exist")
                for key, value in model.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()
                session.commit()
                session.refresh(item)
                return Review.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update Review record: {e}")
            raise

    def update_many(self, model_list: List[Review]) -> List[Review]:
        """Update multiple existing Review records in the database."""
        logging.info(f"Updating multiple Review records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                model_ids = [model.id for model in model_list]
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some Review records do not exist")
                item_map = {item.id: item for item in items}
                for model in model_list:
                    item = item_map[model.id]
                    for key, value in model.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()
                session.commit()
                for item in items:
                    session.refresh(item)
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to update multiple Review records: {e}")
            raise

    def delete(self, model_id: int) -> Review:
        """Delete a Review record from the database by its ID."""
        logging.info(f"Deleting Review record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReview).get(model_id)
                if not item:
                    raise Exception("Review record does not exist")
                session.delete(item)
                session.commit()
                return Review.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Review record: {e}")
            raise

    def delete_many(self, model_ids: List[int]) -> List[Review]:
        """Delete multiple Review records from the database by their IDs."""
        logging.info(f"Deleting multiple Review records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some Review records do not exist")
                for item in items:
                    session.delete(item)
                session.commit()
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Review records: {e}")
            raise
