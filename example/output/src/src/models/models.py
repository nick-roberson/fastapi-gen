from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import FieldInfo


class User(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: Optional[str] = FieldInfo(
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

    def to_dict(self) -> Dict:
        return self.dict()


class Restaurant(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: Optional[str] = FieldInfo(
        default=None,
        description="The unique identifier of the restaurant",
        required=False,
    )
    name: str = FieldInfo(description="The name of the restaurant", required=True)
    location: str = FieldInfo(
        description="The physical location of the restaurant", required=True
    )
    cuisine: Optional[str] = FieldInfo(
        default=None,
        description="The type of cuisine the restaurant offers",
        required=False,
    )
    rating: Optional[float] = FieldInfo(
        default=None, description="The average rating of the restaurant", required=False
    )
    price_range: Optional[str] = FieldInfo(
        default=None, description="The price range of the restaurant", required=False
    )

    def to_dict(self) -> Dict:
        return self.dict()


class Reservation(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: Optional[str] = FieldInfo(
        default=None,
        description="The unique identifier of the reservation",
        required=False,
    )
    restaurant_id: str = FieldInfo(
        description="The ID of the restaurant where the reservation is made",
        required=True,
    )
    user_id: str = FieldInfo(
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

    def to_dict(self) -> Dict:
        return self.dict()


class Review(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: Optional[str] = FieldInfo(
        default=None, description="The unique identifier of the review", required=False
    )
    restaurant_id: str = FieldInfo(
        description="The ID of the restaurant being reviewed", required=True
    )
    user_id: str = FieldInfo(
        description="The ID of the user who wrote the review", required=True
    )
    rating: float = FieldInfo(description="The rating given by the user", required=True)
    comment: Optional[str] = FieldInfo(
        default=None, description="The textual comment of the review", required=False
    )

    def to_dict(self) -> Dict:
        return self.dict()
