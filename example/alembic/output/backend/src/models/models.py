from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import FieldInfo


class User(BaseModel):
    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Core model fields
    id: Optional[int] = FieldInfo(
        default=None, description="The unique identifier of the user", required=False
    )
    username: str = FieldInfo(description="The username of the user", required=True)
    email: str = FieldInfo(description="The email address of the user", required=True)
    phone_number: Optional[str] = FieldInfo(
        default=None, description="The phone number of the user", required=False
    )
    preferences: Optional[list] = FieldInfo(
        default=[], description="The dining preferences of the user", required=False
    )
    role: Optional[str] = FieldInfo(
        default="user",
        description="The role of the user (e.g., admin, user, restaurant_owner)",
        required=False,
    )

    # Optional created_at and updated_at fields
    created_at: Optional[datetime] = FieldInfo(
        default=None, alias="created_at", description="The time the record was created"
    )
    updated_at: Optional[datetime] = FieldInfo(
        default=None,
        alias="updated_at",
        description="The time the record was last updated",
    )

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model()


class UserQuery(BaseModel):
    """Query model for User"""

    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Query model fields
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    preferences: Optional[list] = None
    role: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model_dump()


class Restaurant(BaseModel):
    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Core model fields
    id: Optional[int] = FieldInfo(
        default=None, description="The unique identifier of the alembic", required=False
    )
    name: str = FieldInfo(description="The name of the alembic", required=True)
    location: str = FieldInfo(
        description="The physical location of the alembic", required=True
    )
    cuisine: Optional[str] = FieldInfo(
        default=None,
        description="The type of cuisine the alembic offers",
        required=False,
    )
    rating: Optional[float] = FieldInfo(
        default=None, description="The average rating of the alembic", required=False
    )
    price_range: Optional[str] = FieldInfo(
        default=None, description="The price range of the alembic", required=False
    )

    # Optional created_at and updated_at fields
    created_at: Optional[datetime] = FieldInfo(
        default=None, alias="created_at", description="The time the record was created"
    )
    updated_at: Optional[datetime] = FieldInfo(
        default=None,
        alias="updated_at",
        description="The time the record was last updated",
    )

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model()


class RestaurantQuery(BaseModel):
    """Query model for Restaurant"""

    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Query model fields
    id: Optional[int] = None
    name: Optional[str] = None
    location: Optional[str] = None
    cuisine: Optional[str] = None
    rating: Optional[float] = None
    price_range: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model_dump()


class Reservation(BaseModel):
    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Core model fields
    id: Optional[int] = FieldInfo(
        default=None,
        description="The unique identifier of the reservation",
        required=False,
    )
    restaurant_id: int = FieldInfo(
        description="The ID of the alembic where the reservation is made", required=True
    )
    user_id: int = FieldInfo(
        description="The ID of the user who made the reservation", required=True
    )
    reservation_time: datetime = FieldInfo(
        description="The date and time of the reservation", required=True
    )
    party_size: int = FieldInfo(
        description="The size of the party for the reservation", required=True
    )
    special_requests: Optional[str] = FieldInfo(
        default=None,
        description="Any special requests made by the user",
        required=False,
    )

    # Optional created_at and updated_at fields
    created_at: Optional[datetime] = FieldInfo(
        default=None, alias="created_at", description="The time the record was created"
    )
    updated_at: Optional[datetime] = FieldInfo(
        default=None,
        alias="updated_at",
        description="The time the record was last updated",
    )

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model()


class ReservationQuery(BaseModel):
    """Query model for Reservation"""

    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Query model fields
    id: Optional[int] = None
    restaurant_id: Optional[int] = None
    user_id: Optional[int] = None
    reservation_time: Optional[datetime] = None
    party_size: Optional[int] = None
    special_requests: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model_dump()


class Review(BaseModel):
    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Core model fields
    id: Optional[int] = FieldInfo(
        default=None, description="The unique identifier of the review", required=False
    )
    restaurant_id: int = FieldInfo(
        description="The ID of the alembic being reviewed", required=True
    )
    user_id: int = FieldInfo(
        description="The ID of the user who wrote the review", required=True
    )
    rating: float = FieldInfo(description="The rating given by the user", required=True)
    comment: Optional[str] = FieldInfo(
        default=None, description="The textual comment of the review", required=False
    )

    # Optional created_at and updated_at fields
    created_at: Optional[datetime] = FieldInfo(
        default=None, alias="created_at", description="The time the record was created"
    )
    updated_at: Optional[datetime] = FieldInfo(
        default=None,
        alias="updated_at",
        description="The time the record was last updated",
    )

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model()


class ReviewQuery(BaseModel):
    """Query model for Review"""

    # Pydantic model configuration, enables from_orm and to_orm methods
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    # Query model fields
    id: Optional[int] = None
    restaurant_id: Optional[int] = None
    user_id: Optional[int] = None
    rating: Optional[float] = None
    comment: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert the model to a dictionary"""
        return self.model_dump()
