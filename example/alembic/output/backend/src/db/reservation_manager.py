import logging
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.constants import get_url
from src.db.models import DBReservation
from src.models.models import Reservation, ReservationQuery

# Singleton Manager for Reservation
__RESERVATION_MANAGER = None


def get_reservation_manager():
    global __RESERVATION_MANAGER
    if not __RESERVATION_MANAGER:
        __RESERVATION_MANAGER = ReservationManager()
    return __RESERVATION_MANAGER


class ReservationManager:
    """Manager to handle all database operations for the Reservation records."""

    _session_factory = None

    @classmethod
    def get_session_factory(cls):
        if cls._session_factory is None:
            engine = create_engine(get_url())
            cls._session_factory = sessionmaker(bind=engine)
            logging.info("Database engine and session factory initialized")
        return cls._session_factory

    def query(self, query: ReservationQuery) -> List[Reservation]:
        """Query the Reservation records from the database."""
        logging.info(f"Querying Reservation records: {query}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                query_builder = session.query(DBReservation)
                for key, value in query.dict().items():
                    if value is not None:
                        query_builder = query_builder.filter(
                            getattr(DBReservation, key) == value
                        )
                items = query_builder.all()
                return [Reservation.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to query Reservation records: {e}")
            raise

    def get(self, model_id: int) -> Reservation:
        """Retrieve a Reservation record from the database by its ID."""
        logging.info(f"Retrieving Reservation record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReservation).get(model_id)
                if not item:
                    return None
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to retrieve Reservation record: {e}")
            raise

    def get_many(self, model_ids: List[int]) -> List[Reservation]:
        """Retrieve multiple Reservation records from the database by their IDs."""
        logging.info(f"Retrieving multiple Reservation records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                return [Reservation.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve multiple Reservation records: {e}")
            raise

    def get_all(self, skip: int = 0, limit: int = 0) -> List[Reservation]:
        """Retrieve all Reservation records from the database."""
        logging.info(f"Retrieving all Reservation records")
        session_factory = self.get_session_factory()
        try:
            # Get models with pagination enabled
            with session_factory() as session:
                items = session.query(DBReservation).offset(skip).limit(limit).all()
                return [Reservation.from_orm(item) for item in items] if items else []

        except Exception as e:
            logging.error(f"Failed to retrieve all Reservation records: {e}")
            raise

    def create(self, model: Reservation) -> Reservation:
        """Create a new Reservation record in the database."""
        logging.info(f"Creating new Reservation record: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_item = DBReservation(**model.dict())
                new_item.id = None  # Ensuring it's treated as a new record
                session.add(new_item)
                session.commit()
                session.refresh(new_item)
                return Reservation.from_orm(new_item)

        except Exception as e:
            logging.error(f"Failed to create new Reservation record: {e}")
            raise

    def create_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Create multiple new Reservation records in the database."""
        logging.info(f"Creating multiple new Reservation records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                new_items = [DBReservation(**model.dict()) for model in model_list]
                for item in new_items:
                    item.id = None
                session.add_all(new_items)
                session.commit()
                for item in new_items:
                    session.refresh(item)
                return [Reservation.from_orm(item) for item in new_items]

        except Exception as e:
            logging.error(f"Failed to create multiple new Reservation records: {e}")
            raise

    def update(self, model: Reservation) -> Reservation:
        """Update an existing Reservation record in the database."""
        logging.info(f"Updating Reservation record with ID {model.id}: {model}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReservation).get(model.id)
                if not item:
                    raise Exception("Reservation record does not exist")
                for key, value in model.dict().items():
                    setattr(item, key, value)
                item.updated_at = datetime.now()
                session.commit()
                session.refresh(item)
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to update Reservation record: {e}")
            raise

    def update_many(self, model_list: List[Reservation]) -> List[Reservation]:
        """Update multiple existing Reservation records in the database."""
        logging.info(f"Updating multiple Reservation records: {model_list}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                model_ids = [model.id for model in model_list]
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Reservation records do not exist")
                item_map = {item.id: item for item in items}
                for model in model_list:
                    item = item_map[model.id]
                    for key, value in model.dict().items():
                        setattr(item, key, value)
                    item.updated_at = datetime.now()
                session.commit()
                for item in items:
                    session.refresh(item)
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to update multiple Reservation records: {e}")
            raise

    def delete(self, model_id: int) -> Reservation:
        """Delete a Reservation record from the database by its ID."""
        logging.info(f"Deleting Reservation record with ID: {model_id}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                item = session.query(DBReservation).get(model_id)
                if not item:
                    raise Exception("Reservation record does not exist")
                session.delete(item)
                session.commit()
                return Reservation.from_orm(item)

        except Exception as e:
            logging.error(f"Failed to delete Reservation record: {e}")
            raise

    def delete_many(self, model_ids: List[int]) -> List[Reservation]:
        """Delete multiple Reservation records from the database by their IDs."""
        logging.info(f"Deleting multiple Reservation records with IDs: {model_ids}")
        session_factory = self.get_session_factory()
        try:
            with session_factory() as session:
                items = (
                    session.query(DBReservation)
                    .filter(DBReservation.id.in_(model_ids))
                    .all()
                )
                if len(items) != len(model_ids):
                    raise Exception("Some Reservation records do not exist")
                for item in items:
                    session.delete(item)
                session.commit()
                return [Reservation.from_orm(item) for item in items]

        except Exception as e:
            logging.error(f"Failed to delete multiple Reservation records: {e}")
            raise
