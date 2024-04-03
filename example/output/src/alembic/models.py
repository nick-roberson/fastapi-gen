from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    phone_number = Column(String, index=True)
    preferences = Column(
        String
    )  # This is a simplification; for real JSON support, use JSON type based on your database
    role = Column(String, default="user")


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False)
    cuisine = Column(String)
    rating = Column(Float)
    price_range = Column(String)


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey("restaurants.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    party_size = Column(Integer, nullable=False)
    special_requests = Column(String)

    restaurant = relationship("Restaurant")
    user = relationship("User")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey("restaurants.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(String)

    restaurant = relationship("Restaurant")
    user = relationship("User")
