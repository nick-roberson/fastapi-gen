import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, HTTPException
from src.db.restaurant_manager import get_restaurant_manager
from src.models.models import Restaurant, RestaurantQuery

# Create instances of managers for each model

restaurant_manager = get_restaurant_manager()


# Define Router
router = APIRouter()


########################################################################################################################
# Query Endpoints for Restaurant
########################################################################################################################


@router.post("/restaurant/query")
def query_restaurant(query: RestaurantQuery) -> List[Restaurant]:
    """Query Restaurants"""
    logging.info(f"Querying Restaurants with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.dict().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in RestaurantQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Restaurants with the given query, if none found raise 404
    models = restaurant_manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return the Restaurants
    return models


########################################################################################################################
# Get Endpoints for Restaurant
########################################################################################################################


@router.get("/restaurant")
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


@router.get("/restaurants")
def get_restaurants() -> List[Restaurant]:
    """Get all Restaurants"""
    logging.info(f"Getting all Restaurants")

    # Get all Restaurants, if none found raise 404
    models = restaurant_manager.get_all()
    if not models:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return all Restaurants
    return models


########################################################################################################################
# Create Endpoints for Restaurant
########################################################################################################################


def _create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant helper function"""
    logging.info(f"Creating Restaurant: {str(restaurant)}")

    # Create the Restaurant, if failed raise 400
    model = restaurant_manager.create(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurant")

    # Return the created Restaurant
    return model


@router.post("/restaurant")
def create_restaurant(restaurant: Restaurant) -> Restaurant:
    """Create a Restaurant"""
    # Call the helper function to create the Restaurant
    return _create_restaurant(restaurant)


@router.post("/restaurant/async")
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


@router.post("/restaurants")
def create_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Create multiple Restaurants"""
    # Call the helper function to create the Restaurants
    return _create_restaurants(restaurants)


@router.post("/restaurants/async")
def create_restaurants_async(
    restaurants: List[Restaurant], background_tasks: BackgroundTasks
):
    """Create multiple Restaurants asynchronously"""
    logging.info(f"Creating Restaurants asynchronously: {str(restaurants)}")
    # Create the Restaurants asynchronously
    background_tasks.add_task(_create_restaurants, restaurants)
    # Return the created Restaurants
    return {"message": "Creating Restaurants asynchronously"}


########################################################################################################################
# Update Endpoints for Restaurant
########################################################################################################################


def _update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant helper function"""
    logging.info(f"Updating Restaurant: {str(restaurant)}")

    # Update the Restaurant, if failed raise 400
    model = restaurant_manager.update(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurant")

    # Return the updated Restaurant
    return model


@router.put("/restaurant")
def update_restaurant(restaurant: Restaurant) -> Restaurant:
    """Update a Restaurant"""
    # Call the helper function to update the Restaurant
    return _update_restaurant(restaurant)


@router.put("/restaurant/async")
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


@router.put("/restaurants")
def update_restaurants(restaurants: List[Restaurant]) -> List[Restaurant]:
    """Update multiple Restaurants"""
    # Call the helper function to update the Restaurants
    return _update_restaurants(restaurants)


@router.put("/restaurants/async")
def update_restaurants_async(
    restaurants: List[Restaurant], background_tasks: BackgroundTasks
):
    """Update multiple Restaurants asynchronously"""
    logging.info(f"Updating Restaurants asynchronously: {str(restaurants)}")
    # Update the Restaurants asynchronously
    background_tasks.add_task(_update_restaurants, restaurants)
    # Return the updated Restaurants
    return {"message": "Updating Restaurants asynchronously"}


########################################################################################################################
# Delete Endpoints for Restaurant
########################################################################################################################


def _delete_restaurant(restaurant_id: int) -> Restaurant:
    """Delete a Restaurant helper function"""
    logging.info(f"Deleting Restaurant with id: {id}")

    # Delete the Restaurant, if failed raise 404
    model = restaurant_manager.delete(restaurant_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurant")

    # Return the deleted Restaurant
    return model


@router.delete("/restaurant")
def delete_restaurant(restaurant_id: int) -> Restaurant:
    """Delete a Restaurant"""
    # Call the helper function to delete the Restaurant
    return _delete_restaurant(restaurant_id)


@router.delete("/restaurant/async")
def delete_restaurant_async(restaurant_id: int, background_tasks: BackgroundTasks):
    """Delete a Restaurant asynchronously"""
    logging.info(f"Deleting Restaurant asynchronously with id: {id}")
    # Delete the Restaurant asynchronously
    background_tasks.add_task(_delete_restaurant, restaurant_id)
    # Return the deleted Restaurant
    return {"message": "Deleting Restaurant asynchronously"}


def _delete_restaurants(restaurant_ids: List[int]) -> List[Restaurant]:
    """Delete multiple Restaurants helper function"""
    logging.info(f"Deleting Restaurants: {str(restaurant_ids)}")

    # Delete the Restaurants, if failed raise 404
    models = restaurant_manager.delete_many(restaurant_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurants")

    # Return the deleted Restaurants
    return models


@router.delete("/restaurants")
def delete_restaurants(restaurant_ids: List[int]) -> List[Restaurant]:
    """Delete multiple Restaurants"""
    # Call the helper function to delete the Restaurants
    return _delete_restaurants(restaurant_ids)


@router.delete("/restaurants/async")
def delete_restaurants_async(
    restaurant_ids: List[int], background_tasks: BackgroundTasks
):
    """Delete multiple Restaurants asynchronously"""
    logging.info(f"Deleting Restaurants asynchronously: {str(restaurant_ids)}")
    # Delete the Restaurants asynchronously
    background_tasks.add_task(_delete_restaurants, restaurant_ids)
    # Return the deleted Restaurants
    return {"message": "Deleting Restaurants asynchronously"}
