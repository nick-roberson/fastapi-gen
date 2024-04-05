import logging
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.models import Reservation, Restaurant, Review, User
from reservation_manager import get_reservation_manager
from restaurant_manager import get_restaurant_manager
from review_manager import get_review_manager
from user_manager import get_user_manager

# Create instances of managers for each model

user_manager = get_user_manager()

restaurant_manager = get_restaurant_manager()

reservation_manager = get_reservation_manager()

review_manager = get_review_manager()


# Create FastAPI App and Allow CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


##############################################
# Get Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.get("/user")
def get_user(user_id: str) -> User:
    """Get a User"""
    print(f"Getting User with id: {id}")
    return user_manager.get(user_id=user_id)


@app.get("/users")
def get_users() -> List[User]:
    print(f"Getting all Users")
    return user_manager.get_all()


@app.get("/restaurant")
def get_restaurant(restaurant_id: str) -> Restaurant:
    """Get a Restaurant"""
    print(f"Getting Restaurant with id: {id}")
    return restaurant_manager.get(restaurant_id=restaurant_id)


@app.get("/restaurants")
def get_restaurants() -> List[Restaurant]:
    print(f"Getting all Restaurants")
    return restaurant_manager.get_all()


@app.get("/reservation")
def get_reservation(reservation_id: str) -> Reservation:
    """Get a Reservation"""
    print(f"Getting Reservation with id: {id}")
    return reservation_manager.get(reservation_id=reservation_id)


@app.get("/reservations")
def get_reservations() -> List[Reservation]:
    print(f"Getting all Reservations")
    return reservation_manager.get_all()


@app.get("/review")
def get_review(review_id: str) -> Review:
    """Get a Review"""
    print(f"Getting Review with id: {id}")
    return review_manager.get(review_id=review_id)


@app.get("/reviews")
def get_reviews() -> List[Review]:
    print(f"Getting all Reviews")
    return review_manager.get_all()


##############################################
# Create Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.post("/user")
def create_user(user: User) -> User:
    """Create a User"""
    print(f"Creating User: {str(user)}")
    return user_manager.create(user)


@app.post("/users")
def create_users(users: List[User]) -> List[User]:
    """Create multiple Users"""
    print(f"Creating Users: {str(users)}")
    return user_manager.create_many(users)


@app.post("/restaurant")
def create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant"""
    print(f"Creating Restaurant: {str(restaurant)}")
    return restaurant_manager.create(restaurant)


@app.post("/restaurants")
def create_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Create multiple Restaurants"""
    print(f"Creating Restaurants: {str(restaurants)}")
    return restaurant_manager.create_many(restaurants)


@app.post("/reservation")
def create_reservation(reservation: Reservation) -> Reservation:
    """Create a Reservation"""
    print(f"Creating Reservation: {str(reservation)}")
    return reservation_manager.create(reservation)


@app.post("/reservations")
def create_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Create multiple Reservations"""
    print(f"Creating Reservations: {str(reservations)}")
    return reservation_manager.create_many(reservations)


@app.post("/review")
def create_review(review: Review) -> Review:
    """Create a Review"""
    print(f"Creating Review: {str(review)}")
    return review_manager.create(review)


@app.post("/reviews")
def create_reviews(reviews: List[Review]) -> List[Review]:
    """Create multiple Reviews"""
    print(f"Creating Reviews: {str(reviews)}")
    return review_manager.create_many(reviews)


##############################################
# Update Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.put("/user")
def update_user(user: User) -> User:
    """Update a User"""
    print(f"Updating User: {str(user)}")
    return user_manager.update(user)


@app.put("/users")
def update_users(users: List[User]) -> List[User]:
    """Update multiple Users"""
    print(f"Updating Users: {str(users)}")
    return user_manager.udpate_many(users)


@app.put("/restaurant")
def update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant"""
    print(f"Updating Restaurant: {str(restaurant)}")
    return restaurant_manager.update(restaurant)


@app.put("/restaurants")
def update_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Update multiple Restaurants"""
    print(f"Updating Restaurants: {str(restaurants)}")
    return restaurant_manager.udpate_many(restaurants)


@app.put("/reservation")
def update_reservation(reservation: Reservation) -> Reservation:
    """Update a Reservation"""
    print(f"Updating Reservation: {str(reservation)}")
    return reservation_manager.update(reservation)


@app.put("/reservations")
def update_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Update multiple Reservations"""
    print(f"Updating Reservations: {str(reservations)}")
    return reservation_manager.udpate_many(reservations)


@app.put("/review")
def update_review(review: Review) -> Review:
    """Update a Review"""
    print(f"Updating Review: {str(review)}")
    return review_manager.update(review)


@app.put("/reviews")
def update_reviews(reviews: List[Review]) -> List[Review]:
    """Update multiple Reviews"""
    print(f"Updating Reviews: {str(reviews)}")
    return review_manager.udpate_many(reviews)


##############################################
# Delete Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.delete("/user")
def delete_user(user_id: str):
    """Delete a User"""
    print(f"Deleting User with id: {id}")
    return user_manager.delete(user_id=user_id)


@app.delete("/users")
def delete_users(user_ids: List[str]):
    """Delete multiple Users"""
    print(f"Deleting Users: {str(user_ids)}")
    return user_manager.delete_many(user_ids=user_ids)


@app.delete("/restaurant")
def delete_restaurant(restaurant_id: str):
    """Delete a Restaurant"""
    print(f"Deleting Restaurant with id: {id}")
    return restaurant_manager.delete(restaurant_id=restaurant_id)


@app.delete("/restaurants")
def delete_restaurants(restaurant_ids: List[str]):
    """Delete multiple Restaurants"""
    print(f"Deleting Restaurants: {str(restaurant_ids)}")
    return restaurant_manager.delete_many(restaurant_ids=restaurant_ids)


@app.delete("/reservation")
def delete_reservation(reservation_id: str):
    """Delete a Reservation"""
    print(f"Deleting Reservation with id: {id}")
    return reservation_manager.delete(reservation_id=reservation_id)


@app.delete("/reservations")
def delete_reservations(reservation_ids: List[str]):
    """Delete multiple Reservations"""
    print(f"Deleting Reservations: {str(reservation_ids)}")
    return reservation_manager.delete_many(reservation_ids=reservation_ids)


@app.delete("/review")
def delete_review(review_id: str):
    """Delete a Review"""
    print(f"Deleting Review with id: {id}")
    return review_manager.delete(review_id=review_id)


@app.delete("/reviews")
def delete_reviews(review_ids: List[str]):
    """Delete multiple Reviews"""
    print(f"Deleting Reviews: {str(review_ids)}")
    return review_manager.delete_many(review_ids=review_ids)


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Start the server
    uvicorn.run(app, host="localhost", port=8000)
