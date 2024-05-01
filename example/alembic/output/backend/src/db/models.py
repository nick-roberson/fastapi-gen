from sqlalchemy import (JSON, Boolean, Column, DateTime, Float, Integer,
                        String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy.sql import func

Base = declarative_base()


class DBUser(Base):

    # Define Table Name
    __tablename__ = "user"

    # Define Columns

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(1000), nullable=False, default="")

    email = Column(String(1000), nullable=False, default="")

    phone_number = Column(String(1000), nullable=True, default="")

    preferences = Column(JSON, nullable=True, default=[])

    role = Column(String(1000), nullable=True, default="user")

    # Define Updated and Created At (Auto) (Could be used for DB Replication)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class DBRestaurant(Base):

    # Define Table Name
    __tablename__ = "restaurant"

    # Define Columns

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(1000), nullable=False, default="")

    location = Column(String(1000), nullable=False, default="")

    cuisine = Column(String(1000), nullable=True, default="")

    rating = Column(Float, nullable=True, default=None)

    price_range = Column(String(1000), nullable=True, default="")

    # Define Updated and Created At (Auto) (Could be used for DB Replication)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class DBReservation(Base):

    # Define Table Name
    __tablename__ = "reservation"

    # Define Columns

    id = Column(Integer, primary_key=True, autoincrement=True)

    restaurant_id = Column(Integer, nullable=False, default=None)

    user_id = Column(Integer, nullable=False, default=None)

    reservation_time = Column(DateTime, nullable=False, default=func.now())

    party_size = Column(Integer, nullable=False, default=None)

    special_requests = Column(String(1000), nullable=True, default="")

    # Define Updated and Created At (Auto) (Could be used for DB Replication)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class DBReview(Base):

    # Define Table Name
    __tablename__ = "review"

    # Define Columns

    id = Column(Integer, primary_key=True, autoincrement=True)

    restaurant_id = Column(Integer, nullable=False, default=None)

    user_id = Column(Integer, nullable=False, default=None)

    rating = Column(Float, nullable=False, default=None)

    comment = Column(String(1000), nullable=True, default="")

    # Define Updated and Created At (Auto) (Could be used for DB Replication)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
