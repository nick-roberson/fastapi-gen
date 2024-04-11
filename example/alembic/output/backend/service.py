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

# Default Host and Port
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8000

########################################################################################################################
# Root and Health Endpoints
########################################################################################################################


@app.get("/")
async def root():
    """Root Endpoint"""
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    """Health Endpoint"""
    return {"message": "Healthy"}


########################################################################################################################
# Get Endpoints for User, Restaurant, Reservation, Review
########################################################################################################################


@app.get("/user")
def get_user(user_id: str) -> User:
    """Get a User"""
    logging.info(f"Getting User with id: {id}")

    # Get the User with the given id, if none found raise 404
    model = user_manager.get(user_id=user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    # Return the User
    return model


@app.get("/users")
def get_users() -> List[User]:
    """Get all Users"""
    logging.info(f"Getting all Users")

    # Get all Users, if none found raise 404
    models = user_manager.get_all()
    if not models:
        raise HTTPException(status_code=404, detail=f"No Users found")

    # Return all Users
    return models


@app.get("/restaurant")
def get_restaurant(restaurant_id: str) -> Restaurant:
    """Get a Restaurant"""
    logging.info(f"Getting Restaurant with id: {id}")

    # Get the Restaurant with the given id, if none found raise 404
    model = restaurant_manager.get(restaurant_id=restaurant_id)
    if not model:
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
    if not models:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return all Restaurants
    return models


@app.get("/reservation")
def get_reservation(reservation_id: str) -> Reservation:
    """Get a Reservation"""
    logging.info(f"Getting Reservation with id: {id}")

    # Get the Reservation with the given id, if none found raise 404
    model = reservation_manager.get(reservation_id=reservation_id)
    if not model:
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
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reservations found")

    # Return all Reservations
    return models


@app.get("/review")
def get_review(review_id: str) -> Review:
    """Get a Review"""
    logging.info(f"Getting Review with id: {id}")

    # Get the Review with the given id, if none found raise 404
    model = review_manager.get(review_id=review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")

    # Return the Review
    return model


@app.get("/reviews")
def get_reviews() -> List[Review]:
    """Get all Reviews"""
    logging.info(f"Getting all Reviews")

    # Get all Reviews, if none found raise 404
    models = review_manager.get_all()
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reviews found")

    # Return all Reviews
    return models


########################################################################################################################
# Create Endpoints for User, Restaurant, Reservation, Review
########################################################################################################################


def _create_user(user: User) -> User:
    """Create a User helper function"""
    logging.info(f"Creating User: {str(user)}")

    # Create the User, if failed raise 400
    model = user_manager.create(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create User")

    # Return the created User
    return model


@app.post("/user")
def create_user(user: User) -> User:
    """Create a User"""
    # Call the helper function to create the User
    return _create_user(user)


@app.post("/user/async")
def create_user_async(user: User, background_tasks: BackgroundTasks):
    """Create a User asynchronously"""
    logging.info(f"Creating User asynchronously: {str(user)}")
    # Create the User asynchronously
    background_tasks.add_task(_create_user, user)
    # Return the created User
    return {"message": "Creating User asynchronously"}


def _create_users(users: List[User]) -> List[User]:
    """Create multiple Users helper function"""
    logging.info(f"Creating Users: {str(users)}")

    # Create the Users, if failed raise 400
    models = user_manager.create_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Users")

    # Return the created Users
    return models


@app.post("/users")
def create_users(users: List[User]) -> List[User]:
    """Create multiple Users"""
    # Call the helper function to create the Users
    return _create_users(users)


@app.post("/users/async")
def create_users_async(users: List[User], background_tasks: BackgroundTasks):
    """Create multiple Users asynchronously"""
    logging.info(f"Creating Users asynchronously: {str(users)}")
    # Create the Users asynchronously
    background_tasks.add_task(_create_users, users)
    # Return the created Users
    return {"message": "Creating Users asynchronously"}


def _create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant helper function"""
    logging.info(f"Creating Restaurant: {str(restaurant)}")

    # Create the Restaurant, if failed raise 400
    model = restaurant_manager.create(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurant")

    # Return the created Restaurant
    return model


@app.post("/restaurant")
def create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant"""
    # Call the helper function to create the Restaurant
    return _create_restaurant(restaurant)


@app.post("/restaurant/async")
def create_restaurant_async(restaurant: Restaurant, background_tasks: BackgroundTasks):
    """Create a Restaurant asynchronously"""
    logging.info(f"Creating Restaurant asynchronously: {str(restaurant)}")
    # Create the Restaurant asynchronously
    background_tasks.add_task(_create_restaurant, restaurant)
    # Return the created Restaurant
    return {"message": "Creating Restaurant asynchronously"}


def _create_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Create multiple Restaurants helper function"""
    logging.info(f"Creating Restaurants: {str(restaurants)}")

    # Create the Restaurants, if failed raise 400
    models = restaurant_manager.create_many(restaurants)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurants")

    # Return the created Restaurants
    return models


@app.post("/restaurants")
def create_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Create multiple Restaurants"""
    # Call the helper function to create the Restaurants
    return _create_restaurants(restaurants)


@app.post("/restaurants/async")
def create_restaurants_async(
    restaurants: List[Restaurant], background_tasks: BackgroundTasks
):
    """Create multiple Restaurants asynchronously"""
    logging.info(f"Creating Restaurants asynchronously: {str(restaurants)}")
    # Create the Restaurants asynchronously
    background_tasks.add_task(_create_restaurants, restaurants)
    # Return the created Restaurants
    return {"message": "Creating Restaurants asynchronously"}


def _create_reservation(reservation: Reservation) -> Reservation:
    """Create a Reservation helper function"""
    logging.info(f"Creating Reservation: {str(reservation)}")

    # Create the Reservation, if failed raise 400
    model = reservation_manager.create(reservation)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservation")

    # Return the created Reservation
    return model


@app.post("/reservation")
def create_reservation(reservation: Reservation) -> Reservation:
    """Create a Reservation"""
    # Call the helper function to create the Reservation
    return _create_reservation(reservation)


@app.post("/reservation/async")
def create_reservation_async(
    reservation: Reservation, background_tasks: BackgroundTasks
):
    """Create a Reservation asynchronously"""
    logging.info(f"Creating Reservation asynchronously: {str(reservation)}")
    # Create the Reservation asynchronously
    background_tasks.add_task(_create_reservation, reservation)
    # Return the created Reservation
    return {"message": "Creating Reservation asynchronously"}


def _create_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Create multiple Reservations helper function"""
    logging.info(f"Creating Reservations: {str(reservations)}")

    # Create the Reservations, if failed raise 400
    models = reservation_manager.create_many(reservations)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservations")

    # Return the created Reservations
    return models


@app.post("/reservations")
def create_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Create multiple Reservations"""
    # Call the helper function to create the Reservations
    return _create_reservations(reservations)


@app.post("/reservations/async")
def create_reservations_async(
    reservations: List[Reservation], background_tasks: BackgroundTasks
):
    """Create multiple Reservations asynchronously"""
    logging.info(f"Creating Reservations asynchronously: {str(reservations)}")
    # Create the Reservations asynchronously
    background_tasks.add_task(_create_reservations, reservations)
    # Return the created Reservations
    return {"message": "Creating Reservations asynchronously"}


def _create_review(review: Review) -> Review:
    """Create a Review helper function"""
    logging.info(f"Creating Review: {str(review)}")

    # Create the Review, if failed raise 400
    model = review_manager.create(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Review")

    # Return the created Review
    return model


@app.post("/review")
def create_review(review: Review) -> Review:
    """Create a Review"""
    # Call the helper function to create the Review
    return _create_review(review)


@app.post("/review/async")
def create_review_async(review: Review, background_tasks: BackgroundTasks):
    """Create a Review asynchronously"""
    logging.info(f"Creating Review asynchronously: {str(review)}")
    # Create the Review asynchronously
    background_tasks.add_task(_create_review, review)
    # Return the created Review
    return {"message": "Creating Review asynchronously"}


def _create_reviews(reviews: List[Review]) -> List[Review]:
    """Create multiple Reviews helper function"""
    logging.info(f"Creating Reviews: {str(reviews)}")

    # Create the Reviews, if failed raise 400
    models = review_manager.create_many(reviews)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Reviews")

    # Return the created Reviews
    return models


@app.post("/reviews")
def create_reviews(reviews: List[Review]) -> List[Review]:
    """Create multiple Reviews"""
    # Call the helper function to create the Reviews
    return _create_reviews(reviews)


@app.post("/reviews/async")
def create_reviews_async(reviews: List[Review], background_tasks: BackgroundTasks):
    """Create multiple Reviews asynchronously"""
    logging.info(f"Creating Reviews asynchronously: {str(reviews)}")
    # Create the Reviews asynchronously
    background_tasks.add_task(_create_reviews, reviews)
    # Return the created Reviews
    return {"message": "Creating Reviews asynchronously"}


########################################################################################################################
# Update Endpoints for User, Restaurant, Reservation, Review
########################################################################################################################


def _update_user(user: User) -> User:
    """Update a User helper function"""
    logging.info(f"Updating User: {str(user)}")

    # Update the User, if failed raise 400
    model = user_manager.update(user)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update User")

    # Return the updated User
    return model


@app.put("/user")
def update_user(user: User) -> User:
    """Update a User"""
    # Call the helper function to update the User
    return _update_user(user)


@app.put("/user/async")
def update_user_async(user: User, background_tasks: BackgroundTasks):
    """Update a User asynchronously"""
    logging.info(f"Updating User asynchronously: {str(user)}")
    # Update the User asynchronously
    background_tasks.add_task(_update_user, user)
    # Return the updated User
    return {"message": "Updating User asynchronously"}


def _update_users(users: List[User]) -> List[User]:
    """Update multiple Users helper function"""
    logging.info(f"Updating Users: {str(users)}")

    # Update the Users, if failed raise 400
    models = user_manager.update_many(users)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Users")

    # Return the updated Users
    return models


@app.put("/users")
def update_users(users: List[User]) -> List[User]:
    """Update multiple Users"""
    # Call the helper function to update the Users
    return _update_users(users)


@app.put("/users/async")
def update_users_async(users: List[User], background_tasks: BackgroundTasks):
    """Update multiple Users asynchronously"""
    logging.info(f"Updating Users asynchronously: {str(users)}")
    # Update the Users asynchronously
    background_tasks.add_task(_update_users, users)
    # Return the updated Users
    return {"message": "Updating Users asynchronously"}


def _update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant helper function"""
    logging.info(f"Updating Restaurant: {str(restaurant)}")

    # Update the Restaurant, if failed raise 400
    model = restaurant_manager.update(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurant")

    # Return the updated Restaurant
    return model


@app.put("/restaurant")
def update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant"""
    # Call the helper function to update the Restaurant
    return _update_restaurant(restaurant)


@app.put("/restaurant/async")
def update_restaurant_async(restaurant: Restaurant, background_tasks: BackgroundTasks):
    """Update a Restaurant asynchronously"""
    logging.info(f"Updating Restaurant asynchronously: {str(restaurant)}")
    # Update the Restaurant asynchronously
    background_tasks.add_task(_update_restaurant, restaurant)
    # Return the updated Restaurant
    return {"message": "Updating Restaurant asynchronously"}


def _update_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Update multiple Restaurants helper function"""
    logging.info(f"Updating Restaurants: {str(restaurants)}")

    # Update the Restaurants, if failed raise 400
    models = restaurant_manager.update_many(restaurants)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurants")

    # Return the updated Restaurants
    return models


@app.put("/restaurants")
def update_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Update multiple Restaurants"""
    # Call the helper function to update the Restaurants
    return _update_restaurants(restaurants)


@app.put("/restaurants/async")
def update_restaurants_async(
    restaurants: List[Restaurant], background_tasks: BackgroundTasks
):
    """Update multiple Restaurants asynchronously"""
    logging.info(f"Updating Restaurants asynchronously: {str(restaurants)}")
    # Update the Restaurants asynchronously
    background_tasks.add_task(_update_restaurants, restaurants)
    # Return the updated Restaurants
    return {"message": "Updating Restaurants asynchronously"}


def _update_reservation(reservation: Reservation) -> Reservation:
    """Update a Reservation helper function"""
    logging.info(f"Updating Reservation: {str(reservation)}")

    # Update the Reservation, if failed raise 400
    model = reservation_manager.update(reservation)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservation")

    # Return the updated Reservation
    return model


@app.put("/reservation")
def update_reservation(reservation: Reservation) -> Reservation:
    """Update a Reservation"""
    # Call the helper function to update the Reservation
    return _update_reservation(reservation)


@app.put("/reservation/async")
def update_reservation_async(
    reservation: Reservation, background_tasks: BackgroundTasks
):
    """Update a Reservation asynchronously"""
    logging.info(f"Updating Reservation asynchronously: {str(reservation)}")
    # Update the Reservation asynchronously
    background_tasks.add_task(_update_reservation, reservation)
    # Return the updated Reservation
    return {"message": "Updating Reservation asynchronously"}


def _update_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Update multiple Reservations helper function"""
    logging.info(f"Updating Reservations: {str(reservations)}")

    # Update the Reservations, if failed raise 400
    models = reservation_manager.update_many(reservations)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservations")

    # Return the updated Reservations
    return models


@app.put("/reservations")
def update_reservations(reservations: List[Reservation]) -> List[Reservation]:
    """Update multiple Reservations"""
    # Call the helper function to update the Reservations
    return _update_reservations(reservations)


@app.put("/reservations/async")
def update_reservations_async(
    reservations: List[Reservation], background_tasks: BackgroundTasks
):
    """Update multiple Reservations asynchronously"""
    logging.info(f"Updating Reservations asynchronously: {str(reservations)}")
    # Update the Reservations asynchronously
    background_tasks.add_task(_update_reservations, reservations)
    # Return the updated Reservations
    return {"message": "Updating Reservations asynchronously"}


def _update_review(review: Review) -> Review:
    """Update a Review helper function"""
    logging.info(f"Updating Review: {str(review)}")

    # Update the Review, if failed raise 400
    model = review_manager.update(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Review")

    # Return the updated Review
    return model


@app.put("/review")
def update_review(review: Review) -> Review:
    """Update a Review"""
    # Call the helper function to update the Review
    return _update_review(review)


@app.put("/review/async")
def update_review_async(review: Review, background_tasks: BackgroundTasks):
    """Update a Review asynchronously"""
    logging.info(f"Updating Review asynchronously: {str(review)}")
    # Update the Review asynchronously
    background_tasks.add_task(_update_review, review)
    # Return the updated Review
    return {"message": "Updating Review asynchronously"}


def _update_reviews(reviews: List[Review]) -> List[Review]:
    """Update multiple Reviews helper function"""
    logging.info(f"Updating Reviews: {str(reviews)}")

    # Update the Reviews, if failed raise 400
    models = review_manager.update_many(reviews)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Reviews")

    # Return the updated Reviews
    return models


@app.put("/reviews")
def update_reviews(reviews: List[Review]) -> List[Review]:
    """Update multiple Reviews"""
    # Call the helper function to update the Reviews
    return _update_reviews(reviews)


@app.put("/reviews/async")
def update_reviews_async(reviews: List[Review], background_tasks: BackgroundTasks):
    """Update multiple Reviews asynchronously"""
    logging.info(f"Updating Reviews asynchronously: {str(reviews)}")
    # Update the Reviews asynchronously
    background_tasks.add_task(_update_reviews, reviews)
    # Return the updated Reviews
    return {"message": "Updating Reviews asynchronously"}


########################################################################################################################
# Delete Endpoints for User, Restaurant, Reservation, Review
########################################################################################################################


def _delete_user(user_id: str) -> User:
    """Delete a User helper function"""
    logging.info(f"Deleting User with id: {id}")

    # Delete the User, if failed raise 404
    model = user_manager.delete(user_id=user_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete User")

    # Return the deleted User
    return model


@app.delete("/user")
def delete_user(user_id: str) -> User:
    """Delete a User"""
    # Call the helper function to delete the User
    return _delete_user(user_id)


@app.delete("/user/async")
def delete_user_async(user_id: str, background_tasks: BackgroundTasks):
    """Delete a User asynchronously"""
    logging.info(f"Deleting User asynchronously with id: {id}")
    # Delete the User asynchronously
    background_tasks.add_task(_delete_user, user_id)
    # Return the deleted User
    return {"message": "Deleting User asynchronously"}


def _delete_users(user_ids: List[str]) -> List[User]:
    """Delete multiple Users helper function"""
    logging.info(f"Deleting Users: {str(user_ids)}")

    # Delete the Users, if failed raise 404
    models = user_manager.delete_many(user_ids=user_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Users")

    # Return the deleted Users
    return models


@app.delete("/users")
def delete_users(user_ids: List[str]) -> List[User]:
    """Delete multiple Users"""
    # Call the helper function to delete the Users
    return _delete_users(user_ids)


@app.delete("/users/async")
def delete_users_async(user_ids: List[str], background_tasks: BackgroundTasks):
    """Delete multiple Users asynchronously"""
    logging.info(f"Deleting Users asynchronously: {str(user_ids)}")
    # Delete the Users asynchronously
    background_tasks.add_task(_delete_users, user_ids)
    # Return the deleted Users
    return {"message": "Deleting Users asynchronously"}


def _delete_restaurant(restaurant_id: str) -> Restaurant:
    """Delete a Restaurant helper function"""
    logging.info(f"Deleting Restaurant with id: {id}")

    # Delete the Restaurant, if failed raise 404
    model = restaurant_manager.delete(restaurant_id=restaurant_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurant")

    # Return the deleted Restaurant
    return model


@app.delete("/restaurant")
def delete_restaurant(restaurant_id: str) -> Restaurant:
    """Delete a Restaurant"""
    # Call the helper function to delete the Restaurant
    return _delete_restaurant(restaurant_id)


@app.delete("/restaurant/async")
def delete_restaurant_async(restaurant_id: str, background_tasks: BackgroundTasks):
    """Delete a Restaurant asynchronously"""
    logging.info(f"Deleting Restaurant asynchronously with id: {id}")
    # Delete the Restaurant asynchronously
    background_tasks.add_task(_delete_restaurant, restaurant_id)
    # Return the deleted Restaurant
    return {"message": "Deleting Restaurant asynchronously"}


def _delete_restaurants(restaurant_ids: List[str]) -> List[Restaurant]:
    """Delete multiple Restaurants helper function"""
    logging.info(f"Deleting Restaurants: {str(restaurant_ids)}")

    # Delete the Restaurants, if failed raise 404
    models = restaurant_manager.delete_many(restaurant_ids=restaurant_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurants")

    # Return the deleted Restaurants
    return models


@app.delete("/restaurants")
def delete_restaurants(restaurant_ids: List[str]) -> List[Restaurant]:
    """Delete multiple Restaurants"""
    # Call the helper function to delete the Restaurants
    return _delete_restaurants(restaurant_ids)


@app.delete("/restaurants/async")
def delete_restaurants_async(
    restaurant_ids: List[str], background_tasks: BackgroundTasks
):
    """Delete multiple Restaurants asynchronously"""
    logging.info(f"Deleting Restaurants asynchronously: {str(restaurant_ids)}")
    # Delete the Restaurants asynchronously
    background_tasks.add_task(_delete_restaurants, restaurant_ids)
    # Return the deleted Restaurants
    return {"message": "Deleting Restaurants asynchronously"}


def _delete_reservation(reservation_id: str) -> Reservation:
    """Delete a Reservation helper function"""
    logging.info(f"Deleting Reservation with id: {id}")

    # Delete the Reservation, if failed raise 404
    model = reservation_manager.delete(reservation_id=reservation_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservation")

    # Return the deleted Reservation
    return model


@app.delete("/reservation")
def delete_reservation(reservation_id: str) -> Reservation:
    """Delete a Reservation"""
    # Call the helper function to delete the Reservation
    return _delete_reservation(reservation_id)


@app.delete("/reservation/async")
def delete_reservation_async(reservation_id: str, background_tasks: BackgroundTasks):
    """Delete a Reservation asynchronously"""
    logging.info(f"Deleting Reservation asynchronously with id: {id}")
    # Delete the Reservation asynchronously
    background_tasks.add_task(_delete_reservation, reservation_id)
    # Return the deleted Reservation
    return {"message": "Deleting Reservation asynchronously"}


def _delete_reservations(reservation_ids: List[str]) -> List[Reservation]:
    """Delete multiple Reservations helper function"""
    logging.info(f"Deleting Reservations: {str(reservation_ids)}")

    # Delete the Reservations, if failed raise 404
    models = reservation_manager.delete_many(reservation_ids=reservation_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservations")

    # Return the deleted Reservations
    return models


@app.delete("/reservations")
def delete_reservations(reservation_ids: List[str]) -> List[Reservation]:
    """Delete multiple Reservations"""
    # Call the helper function to delete the Reservations
    return _delete_reservations(reservation_ids)


@app.delete("/reservations/async")
def delete_reservations_async(
    reservation_ids: List[str], background_tasks: BackgroundTasks
):
    """Delete multiple Reservations asynchronously"""
    logging.info(f"Deleting Reservations asynchronously: {str(reservation_ids)}")
    # Delete the Reservations asynchronously
    background_tasks.add_task(_delete_reservations, reservation_ids)
    # Return the deleted Reservations
    return {"message": "Deleting Reservations asynchronously"}


def _delete_review(review_id: str) -> Review:
    """Delete a Review helper function"""
    logging.info(f"Deleting Review with id: {id}")

    # Delete the Review, if failed raise 404
    model = review_manager.delete(review_id=review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Review")

    # Return the deleted Review
    return model


@app.delete("/review")
def delete_review(review_id: str) -> Review:
    """Delete a Review"""
    # Call the helper function to delete the Review
    return _delete_review(review_id)


@app.delete("/review/async")
def delete_review_async(review_id: str, background_tasks: BackgroundTasks):
    """Delete a Review asynchronously"""
    logging.info(f"Deleting Review asynchronously with id: {id}")
    # Delete the Review asynchronously
    background_tasks.add_task(_delete_review, review_id)
    # Return the deleted Review
    return {"message": "Deleting Review asynchronously"}


def _delete_reviews(review_ids: List[str]) -> List[Review]:
    """Delete multiple Reviews helper function"""
    logging.info(f"Deleting Reviews: {str(review_ids)}")

    # Delete the Reviews, if failed raise 404
    models = review_manager.delete_many(review_ids=review_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reviews")

    # Return the deleted Reviews
    return models


@app.delete("/reviews")
def delete_reviews(review_ids: List[str]) -> List[Review]:
    """Delete multiple Reviews"""
    # Call the helper function to delete the Reviews
    return _delete_reviews(review_ids)


@app.delete("/reviews/async")
def delete_reviews_async(review_ids: List[str], background_tasks: BackgroundTasks):
    """Delete multiple Reviews asynchronously"""
    logging.info(f"Deleting Reviews asynchronously: {str(review_ids)}")
    # Delete the Reviews asynchronously
    background_tasks.add_task(_delete_reviews, review_ids)
    # Return the deleted Reviews
    return {"message": "Deleting Reviews asynchronously"}


########################################################################################################################
# Logging
########################################################################################################################


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


########################################################################################################################
# Parse Command Line Arguments
########################################################################################################################


def parse_args():
    """Parse Command Line Arguments"""
    parser = argparse.ArgumentParser(description="Run the FastAPI Server")
    parser.add_argument(
        "--host", "-h", type=str, default=DEFAULT_HOST, help="Host to run the server on"
    )
    parser.add_argument(
        "--port", "-p", type=int, default=DEFAULT_PORT, help="Port to run the server on"
    )
    return parser.parse_args()


########################################################################################################################
# Run the Server
########################################################################################################################


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Parse Command Line Arguments
    args = parse_args()
    # Start the server
    uvicorn.run(app, host=args.host, port=args.port)
