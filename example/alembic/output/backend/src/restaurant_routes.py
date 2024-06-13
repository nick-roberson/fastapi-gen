import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from src.db.restaurant_manager import RestaurantManager
from src.models.models import Restaurant, RestaurantQuery

# Define Router
router = APIRouter()


def get_manager() -> RestaurantManager:
    """Get the Restaurant Manager"""
    return RestaurantManager()


########################################################################################################################
# Query Endpoints for Restaurant
########################################################################################################################


@router.post("/restaurant/query")
def query_restaurant(
    query: RestaurantQuery, manager: RestaurantManager = Depends(get_manager)
) -> List[Restaurant]:
    """Query Restaurants"""
    logging.info(f"Querying Restaurants with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.model_dump().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in RestaurantQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Restaurants with the given query, if none found raise 404
    models = manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return the Restaurants
    return models


########################################################################################################################
# Get Endpoints for Restaurant
########################################################################################################################


@router.get("/restaurant")
def get_restaurant(
    restaurant_id: str, manager: RestaurantManager = Depends(get_manager)
) -> Restaurant:
    """Get a Restaurant"""
    logging.info(f"Getting Restaurant with id: {id}")

    # Get the Restaurant with the given id, if none found raise 404
    model = manager.get(restaurant_id=restaurant_id)
    if not model:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )

    # Return the Restaurant
    return model


@router.get("/restaurants")
def get_restaurants(
    skip: int = 0, limit: int = 100, manager: RestaurantManager = Depends(get_manager)
) -> List[Restaurant]:
    """Get all Restaurants"""
    logging.info(f"Getting all Restaurants")

    # Get all Restaurants, if none found raise 404
    models = manager.get_all(skip=skip, limit=limit)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Restaurants found")

    # Return all Restaurants
    return models


########################################################################################################################
# Create Endpoints for Restaurant
########################################################################################################################


def _create_restaurant(
    restaurant: Restaurant, manager: RestaurantManager
) -> Restaurant:
    """Create a Restaurant helper function"""
    logging.info(f"Creating Restaurant: {str(restaurant)}")

    # Create the Restaurant, if failed raise 400
    model = manager.create(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurant")

    # Return the created Restaurant
    return model


@router.post("/restaurant")
def create_restaurant(
    restaurant: Restaurant, manager: RestaurantManager = Depends(get_manager)
) -> Restaurant:
    """Create a Restaurant"""
    # Call the helper function to create the Restaurant
    return _create_restaurant(restaurant, manager)


@router.post("/restaurant/async")
async def create_restaurant_async(
    restaurant: Restaurant,
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Create a Restaurant asynchronously"""
    logging.info(f"Creating Restaurant asynchronously: {str(restaurant)}")
    # Create the Restaurant asynchronously
    background_tasks.add_task(_create_restaurant, restaurant, manager)
    # Return the created Restaurant
    return {"message": "Creating Restaurant asynchronously"}


def _create_restaurants(
    restaurants: List[Restaurant], manager: RestaurantManager
) -> List[Restaurant]:
    """Create multiple Restaurants helper function"""
    logging.info(f"Creating Restaurants: {str(restaurants)}")

    # Create the Restaurants, if failed raise 400
    models = manager.create_many(restaurants)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Restaurants")

    # Return the created Restaurants
    return models


@router.post("/restaurants")
def create_restaurants(
    restaurants: List[Restaurant], manager: RestaurantManager = Depends(get_manager)
) -> List[Restaurant]:
    """Create multiple Restaurants"""
    # Call the helper function to create the Restaurants
    return _create_restaurants(restaurants, manager)


@router.post("/restaurants/async")
async def create_restaurants_async(
    restaurants: List[Restaurant],
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Create multiple Restaurants asynchronously"""
    logging.info(f"Creating Restaurants asynchronously: {str(restaurants)}")
    # Create the Restaurants asynchronously
    background_tasks.add_task(_create_restaurants, restaurants, manager)
    # Return the created Restaurants
    return {"message": "Creating Restaurants asynchronously"}


########################################################################################################################
# Update Endpoints for Restaurant
########################################################################################################################


def _update_restaurant(
    restaurant: Restaurant, manager: RestaurantManager
) -> Restaurant:
    """Update a Restaurant helper function"""
    logging.info(f"Updating Restaurant: {str(restaurant)}")

    # Update the Restaurant, if failed raise 400
    model = manager.update(restaurant)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurant")

    # Return the updated Restaurant
    return model


@router.put("/restaurant")
def update_restaurant(
    restaurant: Restaurant, manager: RestaurantManager = Depends(get_manager)
) -> Restaurant:
    """Update a Restaurant"""
    # Call the helper function to update the Restaurant
    return _update_restaurant(restaurant, manager)


@router.put("/restaurant/async")
async def update_restaurant_async(
    restaurant: Restaurant,
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Update a Restaurant asynchronously"""
    logging.info(f"Updating Restaurant asynchronously: {str(restaurant)}")
    # Update the Restaurant asynchronously
    background_tasks.add_task(_update_restaurant, restaurant, manager)
    # Return the updated Restaurant
    return {"message": "Updating Restaurant asynchronously"}


def _update_restaurants(
    restaurants: List[Restaurant], manager: RestaurantManager
) -> List[Restaurant]:
    """Update multiple Restaurants helper function"""
    logging.info(f"Updating Restaurants: {str(restaurants)}")

    # Update the Restaurants, if failed raise 400
    models = manager.update_many(restaurants)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Restaurants")

    # Return the updated Restaurants
    return models


@router.put("/restaurants")
def update_restaurants(
    restaurants: List[Restaurant], manager: RestaurantManager = Depends(get_manager)
) -> List[Restaurant]:
    """Update multiple Restaurants"""
    # Call the helper function to update the Restaurants
    return _update_restaurants(restaurants, manager)


@router.put("/restaurants/async")
async def update_restaurants_async(
    restaurants: List[Restaurant],
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Update multiple Restaurants asynchronously"""
    logging.info(f"Updating Restaurants asynchronously: {str(restaurants)}")
    # Update the Restaurants asynchronously
    background_tasks.add_task(_update_restaurants, restaurants, manager)
    # Return the updated Restaurants
    return {"message": "Updating Restaurants asynchronously"}


########################################################################################################################
# Delete Endpoints for Restaurant
########################################################################################################################


def _delete_restaurant(restaurant_id: int, manager: RestaurantManager) -> Restaurant:
    """Delete a Restaurant helper function"""
    logging.info(f"Deleting Restaurant with id: {id}")

    # Delete the Restaurant, if failed raise 404
    model = manager.delete(restaurant_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurant")

    # Return the deleted Restaurant
    return model


@router.delete("/restaurant")
def delete_restaurant(
    restaurant_id: int, manager: RestaurantManager = Depends(get_manager)
) -> Restaurant:
    """Delete a Restaurant"""
    # Call the helper function to delete the Restaurant
    return _delete_restaurant(restaurant_id, manager)


@router.delete("/restaurant/async")
async def delete_restaurant_async(
    restaurant_id: int,
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Delete a Restaurant asynchronously"""
    logging.info(f"Deleting Restaurant asynchronously with id: {id}")
    # Delete the Restaurant asynchronously
    background_tasks.add_task(_delete_restaurant, restaurant_id, manager)
    # Return the deleted Restaurant
    return {"message": "Deleting Restaurant asynchronously"}


def _delete_restaurants(
    restaurant_ids: List[int], manager: RestaurantManager
) -> List[Restaurant]:
    """Delete multiple Restaurants helper function"""
    logging.info(f"Deleting Restaurants: {str(restaurant_ids)}")

    # Delete the Restaurants, if failed raise 404
    models = manager.delete_many(restaurant_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Restaurants")

    # Return the deleted Restaurants
    return models


@router.delete("/restaurants")
def delete_restaurants(
    restaurant_ids: List[int], manager: RestaurantManager = Depends(get_manager)
) -> List[Restaurant]:
    """Delete multiple Restaurants"""
    # Call the helper function to delete the Restaurants
    return _delete_restaurants(restaurant_ids, manager)


@router.delete("/restaurants/async")
async def delete_restaurants_async(
    restaurant_ids: List[int],
    background_tasks: BackgroundTasks,
    manager: RestaurantManager = Depends(get_manager),
):
    """Delete multiple Restaurants asynchronously"""
    logging.info(f"Deleting Restaurants asynchronously: {str(restaurant_ids)}")
    # Delete the Restaurants asynchronously
    background_tasks.add_task(_delete_restaurants, restaurant_ids, manager)
    # Return the deleted Restaurants
    return {"message": "Deleting Restaurants asynchronously"}
