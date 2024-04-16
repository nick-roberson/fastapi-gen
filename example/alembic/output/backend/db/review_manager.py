import logging
from datetime import datetime
from typing import List

from db.constants import DB_URL
from db.models import DBReview
from models.models import Review, ReviewQuery
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

    ########################################################
    # Query Operations                                     #
    ########################################################

    def query(self, query: ReviewQuery) -> List[Review]:
        """Query the Review records from the database."""
        logging.info(f"Querying Review records: {query}")
        try:
            with self.session_factory() as session:

                # Build the query
                query_builder = session.query(DBReview)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBReview, key) == value
                        )

                # Execute the query
                items = query_builder.all()
                if not items:
                    return []

                # Return the Review records
                logging.info(f"Successfully queried Review records: {items}")
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to query Review records: {e}")
            raise f"Failed to query Review records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Get Operations                                       #
    ########################################################

    def get(self, model_id: int) -> Review:
        """Retrieve a Review record from the database by its ID."""
        logging.info(f"Retrieving Review record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(model_id)
                if not item:
                    return None

                # Return the Review record
                logging.info(f"Successfully retrieved Review record: {item}")
                return Review.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Review record: {e}")
            raise f"Failed to retrieve Review record: {e}"
        finally:
            self.close_session()

    def get_many(self, model_ids: List[int]) -> List[Review]:
        """Retrieve multiple Review records from the database by their IDs."""
        logging.info(f"Retrieving multiple Review records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Review records by their IDs
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                if not items:
                    return []

                # Return the Review records
                logging.info(f"Successfully retrieved multiple Review records: {items}")
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Review records: {e}")
            raise f"Failed to retrieve multiple Review records: {e}"
        finally:
            self.close_session()

    def get_all(self) -> List[Review]:
        """Retrieve all Review records from the database."""
        logging.info("Retrieving all Review records")
        try:
            with self.session_factory() as session:

                # Retrieve all Review records
                items = session.query(DBReview).all()
                if not items:
                    return []

                # Return the Review records
                logging.info(f"Successfully retrieved all Review records: {items}")
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to retrieve all Review records: {e}")
            raise f"Failed to retrieve all Review records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Create Operations                                    #
    ########################################################

    def create(self, model: Review) -> Review:
        """Create a new Review record in the database."""
        logging.info(f"Creating new Review record: {model}")
        try:
            with self.session_factory() as session:

                # Create a new Review record
                new_item = DBReview(**model.dict())

                # Clear the id of the new model to ensure it is created as a new record
                new_item.id = None

                # Add the new Review record to the session and commit
                session.add(new_item)
                session.commit()

                # Refresh and return the new Review record
                session.refresh(new_item)
                logging.info(f"Successfully created new Review record: {new_item}")
                return Review.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Review record: {e}")
            raise f"Failed to create new Review record: {e}"
        finally:
            self.close_session()

    def create_many(self, model_list: List[Review]) -> List[Review]:
        """Create multiple new Review records in the database."""
        logging.info(f"Creating multiple new Review records: {model_list}")
        try:
            with self.session_factory() as session:

                # Create new Review records
                new_items = [DBReview(**model.dict()) for model in model_list]

                # Clear the ids of the new models to ensure they are created as new records
                for item in new_items:
                    item.id = None

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
            raise f"Failed to create multiple new Review records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Update Operations                                    #
    ########################################################

    def update(self, model: Review) -> Review:
        """Update an existing Review record in the database."""
        logging.info(f"Updating Review record with ID {id}: {model}")
        try:
            with self.session_factory() as session:

                # If id is not present on update, raise an exception
                if not model.id:
                    raise Exception("ID is required to update Review record")

                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(model.id)
                if not item:
                    raise Exception("Review record does not exist")

                # Update the Review record with the new data
                for key, value in model.dict().items():
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
            raise f"Failed to update Review record: {e}"
        finally:
            self.close_session()

    def update_many(self, model_list: List[Review]) -> List[Review]:
        """Update multiple existing Review records in the database."""
        logging.info(f"Updating multiple Review records: {model_list}")
        try:
            with self.session_factory() as session:
                # Update the Review records with the new data
                updated_items = []

                # Get all the items by id, raise exception if any are missing
                model_ids = [model.id for model in model_list]
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some Review records do not exist")

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

                # Refresh and return the updated Review records
                for item in updated_items:
                    session.refresh(item)

                # Return the updated items
                logging.info(
                    f"Successfully updated multiple Review records: {updated_items}"
                )
                return [Review.from_orm(item) for item in updated_items]

        except Exception as e:
            logging.error(f"Failed to update multiple Review records: {e}")
            raise f"Failed to update multiple Review records: {e}"
        finally:
            self.close_session()

    ########################################################
    # Delete Operations                                    #
    ########################################################

    def delete(self, model_id: int) -> Review:
        """Delete a Review record from the database by its ID."""
        logging.info(f"Deleting Review record with ID: {model_id}")
        try:
            with self.session_factory() as session:

                # Retrieve the Review record by its ID
                item = session.query(DBReview).get(model_id)
                if not item:
                    raise Exception("Review record does not exist")

                # Delete the Review record
                session.delete(item)
                session.commit()

                # Return the deleted Review record
                logging.info(f"Successfully deleted Review record: {item}")
                return Review.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Review record: {e}")
            raise f"Failed to delete Review record: {e}"
        finally:
            self.close_session()

    def delete_many(self, model_ids: List[int]) -> List[Review]:
        """Delete multiple Review records from the database by their IDs."""
        logging.info(f"Deleting multiple Review records with IDs: {model_ids}")
        try:
            with self.session_factory() as session:

                # Retrieve the Review records by their IDs
                items = session.query(DBReview).filter(DBReview.id.in_(model_ids)).all()
                if len(items) != len(model_ids):
                    raise Exception("Some Review records do not exist")

                # Delete the Review records
                for item in items:
                    session.delete(item)

                # Commit the changes
                session.commit()

                # Return the deleted Review records
                logging.info(f"Successfully deleted multiple Review records: {items}")
                return [Review.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Review records: {e}")
            raise f"Failed to delete multiple Review records: {e}"
        finally:
            self.close_session()

    def close_session(self):
        """This method is now redundant since each action opens and closes its session."""
        pass
