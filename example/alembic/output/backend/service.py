import argparse
import logging
from typing import List

import uvicorn
from db.reservation_manager import get_reservation_manager
from db.restaurant_manager import get_restaurant_manager
from db.review_manager import get_review_manager
from db.user_manager import get_user_manager
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.models import Reservation, Restaurant, Review, User

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
    """Root Endpoint"""
    return {"message": "Hello World"}


##############################################
# Get Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.get("/user")
def get_user(user_id: str) -> User:
    """Get a User"""
    logging.info(f"Getting User with id: {id}")

    # Get the User with the given id, if none found raise 404
    model = user_manager.get(user_id=user_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    # Return the User
    return model


@app.get("/users")
def get_users() -> List[User]:
    """Get all Users"""
    logging.info(f"Getting all Users")

    # Get all Users, if none found raise 404
    models = user_manager.get_all()
    if models is None:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return all Users
    return models


@app.get("/restaurant")
def get_restaurant(restaurant_id: str) -> Restaurant:
    """Get a Restaurant"""
    logging.info(f"Getting Restaurant with id: {id}")

    # Get the Restaurant with the given id, if none found raise 404
    model = restaurant_manager.get(restaurant_id=restaurant_id)
    if model is None:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )

    # Return the Restaurant
    return model


@app.get("/restaurants")
def get_restaurants() -> List[Restaurant]:
    """Get all Restaurants"""
    logging.info(f"Getting all Restaurants")

    # Get all Restaurants, if none found raise 404
    models = restaurant_manager.get_all()
    if models is None:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return all Restaurants
    return models


@app.get("/reservation")
def get_reservation(reservation_id: str) -> Reservation:
    """Get a Reservation"""
    logging.info(f"Getting Reservation with id: {id}")

    # Get the Reservation with the given id, if none found raise 404
    model = reservation_manager.get(reservation_id=reservation_id)
    if model is None:
        raise HTTPException(
            status_code=404, detail=f"Reservation with id {id} not found"
        )

    # Return the Reservation
    return model


@app.get("/reservations")
def get_reservations() -> List[Reservation]:
    """Get all Reservations"""
    logging.info(f"Getting all Reservations")

    # Get all Reservations, if none found raise 404
    models = reservation_manager.get_all()
    if models is None:
        raise HTTPException(status_code=404, detail=f"No Reservations found")

    # Return all Reservations
    return models


@app.get("/review")
def get_review(review_id: str) -> Review:
    """Get a Review"""
    logging.info(f"Getting Review with id: {id}")

    # Get the Review with the given id, if none found raise 404
    model = review_manager.get(review_id=review_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")

    # Return the Review
    return model


@app.get("/reviews")
def get_reviews() -> List[Review]:
    """Get all Reviews"""
    logging.info(f"Getting all Reviews")

    # Get all Reviews, if none found raise 404
    models = review_manager.get_all()
    if models is None:
        raise HTTPException(status_code=404, detail=f"No Reviews found")

    # Return all Reviews
    return models


##############################################
# Create Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.post("/user")
def create_user(user: User) -> User:
    """Create a User"""
    logging.info(f"Creating User: {str(user)}")

    # Create the User, if failed raise 400
    model = user_manager.create(user)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to create User")

    # Return the created User
    return model


@app.post("/users")
def create_users(users: List[User]) -> List[User]:
    """Create multiple Users"""
    logging.info(f"Creating Users: {str(users)}")

    # Create the Users, if failed raise 400
    models = user_manager.create_many(users)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Users")

    # Return the created Users
    return models


@app.post("/restaurant")
def create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant"""
    logging.info(f"Creating Restaurant: {str(restaurant)}")

    # Create the Restaurant, if failed raise 400
    model = restaurant_manager.create(restaurant)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurant")

    # Return the created Restaurant
    return model


@app.post("/restaurants")
def create_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Create multiple Restaurants"""
    logging.info(f"Creating Restaurants: {str(restaurants)}")

    # Create the Restaurants, if failed raise 400
    models = restaurant_manager.create_many(restaurants)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurants")

    # Return the created Restaurants
    return models


@app.post("/reservation")
def create_reservation(reservation: Reservation) -> Reservation:
    """Create a Reservation"""
    logging.info(f"Creating Reservation: {str(reservation)}")

    # Create the Reservation, if failed raise 400
    model = reservation_manager.create(reservation)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservation")

    # Return the created Reservation
    return model


@app.post("/reservations")
def create_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Create multiple Reservations"""
    logging.info(f"Creating Reservations: {str(reservations)}")

    # Create the Reservations, if failed raise 400
    models = reservation_manager.create_many(reservations)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservations")

    # Return the created Reservations
    return models


@app.post("/review")
def create_review(review: Review) -> Review:
    """Create a Review"""
    logging.info(f"Creating Review: {str(review)}")

    # Create the Review, if failed raise 400
    model = review_manager.create(review)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Review")

    # Return the created Review
    return model


@app.post("/reviews")
def create_reviews(reviews: List[Review]) -> List[Review]:
    """Create multiple Reviews"""
    logging.info(f"Creating Reviews: {str(reviews)}")

    # Create the Reviews, if failed raise 400
    models = review_manager.create_many(reviews)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to create Reviews")

    # Return the created Reviews
    return models


##############################################
# Update Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.put("/user")
def update_user(user: User) -> User:
    """Update a User"""
    logging.info(f"Updating User: {str(user)}")

    # Update the User, if failed raise 400
    model = user_manager.update(user)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to update User")

    # Return the updated User
    return model


@app.put("/users")
def update_users(users: List[User]) -> List[User]:
    """Update multiple Users"""
    logging.info(f"Updating Users: {str(users)}")

    # Update the Users, if failed raise 400
    models = user_manager.update_many(users)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Users")

    # Return the updated Users
    return models


@app.put("/restaurant")
def update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant"""
    logging.info(f"Updating Restaurant: {str(restaurant)}")

    # Update the Restaurant, if failed raise 400
    model = restaurant_manager.update(restaurant)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurant")

    # Return the updated Restaurant
    return model


@app.put("/restaurants")
def update_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Update multiple Restaurants"""
    logging.info(f"Updating Restaurants: {str(restaurants)}")

    # Update the Restaurants, if failed raise 400
    models = restaurant_manager.update_many(restaurants)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurants")

    # Return the updated Restaurants
    return models


@app.put("/reservation")
def update_reservation(reservation: Reservation) -> Reservation:
    """Update a Reservation"""
    logging.info(f"Updating Reservation: {str(reservation)}")

    # Update the Reservation, if failed raise 400
    model = reservation_manager.update(reservation)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservation")

    # Return the updated Reservation
    return model


@app.put("/reservations")
def update_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Update multiple Reservations"""
    logging.info(f"Updating Reservations: {str(reservations)}")

    # Update the Reservations, if failed raise 400
    models = reservation_manager.update_many(reservations)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservations")

    # Return the updated Reservations
    return models


@app.put("/review")
def update_review(review: Review) -> Review:
    """Update a Review"""
    logging.info(f"Updating Review: {str(review)}")

    # Update the Review, if failed raise 400
    model = review_manager.update(review)
    if model is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Review")

    # Return the updated Review
    return model


@app.put("/reviews")
def update_reviews(reviews: List[Review]) -> List[Review]:
    """Update multiple Reviews"""
    logging.info(f"Updating Reviews: {str(reviews)}")

    # Update the Reviews, if failed raise 400
    models = review_manager.update_many(reviews)
    if models is None:
        raise HTTPException(status_code=400, detail=f"Failed to update Reviews")

    # Return the updated Reviews
    return models


##############################################
# Delete Endpoints for User, Restaurant, Reservation, Review
##############################################


@app.delete("/user")
def delete_user(user_id: str) -> User:
    """Delete a User"""
    logging.info(f"Deleting User with id: {id}")

    # Delete the User, if failed raise 404
    model = user_manager.delete(user_id=user_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete User")

    # Return the deleted User
    return model


@app.delete("/users")
def delete_users(user_ids: List[str]) -> List[User]:
    """Delete multiple Users"""
    logging.info(f"Deleting Users: {str(user_ids)}")

    # Delete the Users, if failed raise 404
    models = user_manager.delete_many(user_ids=user_ids)
    if models is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Users")

    # Return the deleted Users
    return models


@app.delete("/restaurant")
def delete_restaurant(restaurant_id: str) -> Restaurant:
    """Delete a Restaurant"""
    logging.info(f"Deleting Restaurant with id: {id}")

    # Delete the Restaurant, if failed raise 404
    model = restaurant_manager.delete(restaurant_id=restaurant_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurant")

    # Return the deleted Restaurant
    return model


@app.delete("/restaurants")
def delete_restaurants(restaurant_ids: List[str]) -> List[Restaurant]:
    """Delete multiple Restaurants"""
    logging.info(f"Deleting Restaurants: {str(restaurant_ids)}")

    # Delete the Restaurants, if failed raise 404
    models = restaurant_manager.delete_many(restaurant_ids=restaurant_ids)
    if models is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurants")

    # Return the deleted Restaurants
    return models


@app.delete("/reservation")
def delete_reservation(reservation_id: str) -> Reservation:
    """Delete a Reservation"""
    logging.info(f"Deleting Reservation with id: {id}")

    # Delete the Reservation, if failed raise 404
    model = reservation_manager.delete(reservation_id=reservation_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservation")

    # Return the deleted Reservation
    return model


@app.delete("/reservations")
def delete_reservations(reservation_ids: List[str]) -> List[Reservation]:
    """Delete multiple Reservations"""
    logging.info(f"Deleting Reservations: {str(reservation_ids)}")

    # Delete the Reservations, if failed raise 404
    models = reservation_manager.delete_many(reservation_ids=reservation_ids)
    if models is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservations")

    # Return the deleted Reservations
    return models


@app.delete("/review")
def delete_review(review_id: str) -> Review:
    """Delete a Review"""
    logging.info(f"Deleting Review with id: {id}")

    # Delete the Review, if failed raise 404
    model = review_manager.delete(review_id=review_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Review")

    # Return the deleted Review
    return model


@app.delete("/reviews")
def delete_reviews(review_ids: List[str]) -> List[Review]:
    """Delete multiple Reviews"""
    logging.info(f"Deleting Reviews: {str(review_ids)}")

    # Delete the Reviews, if failed raise 404
    models = review_manager.delete_many(review_ids=review_ids)
    if models is None:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reviews")

    # Return the deleted Reviews
    return models


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


def parse_args():
    """Parse Command Line Arguments"""
    parser = argparse.ArgumentParser(description="Run the FastAPI Server")
    parser.add_argument(
        "--host", type=str, default="localhost", help="Host to run the server on"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the server on"
    )
    return parser.parse_args()


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Parse Command Line Arguments
    args = parse_args()
    # Start the server
    uvicorn.run(app, host=args.host, port=args.port)
