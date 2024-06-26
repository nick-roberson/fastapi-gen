import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from src.db.reservation_manager import ReservationManager
from src.models.models import Reservation, ReservationQuery

# Define Router
router = APIRouter()


def get_manager() -> ReservationManager:
    """Get the Reservation Manager"""
    return ReservationManager()


########################################################################################################################
# Query Endpoints for Reservation
########################################################################################################################


@router.post("/reservation/query")
def query_reservation(
    query: ReservationQuery, manager: ReservationManager = Depends(get_manager)
) -> List[Reservation]:
    """Query Reservations"""
    logging.info(f"Querying Reservations with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.model_dump().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in ReservationQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Reservations with the given query, if none found raise 404
    models = manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reservations found")

    # Return the Reservations
    return models


########################################################################################################################
# Get Endpoints for Reservation
########################################################################################################################


@router.get("/reservation")
def get_reservation(
    reservation_id: str, manager: ReservationManager = Depends(get_manager)
) -> Reservation:
    """Get a Reservation"""
    logging.info(f"Getting Reservation with id: {id}")

    # Get the Reservation with the given id, if none found raise 404
    model = manager.get(reservation_id=reservation_id)
    if not model:
        raise HTTPException(
            status_code=404, detail=f"Reservation with id {id} not found"
        )

    # Return the Reservation
    return model


@router.get("/reservations")
def get_reservations(
    skip: int = 0, limit: int = 100, manager: ReservationManager = Depends(get_manager)
) -> List[Reservation]:
    """Get all Reservations"""
    logging.info(f"Getting all Reservations")

    # Get all Reservations, if none found raise 404
    models = manager.get_all(skip=skip, limit=limit)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reservations found")

    # Return all Reservations
    return models


########################################################################################################################
# Create Endpoints for Reservation
########################################################################################################################


def _create_reservation(
    reservation: Reservation, manager: ReservationManager
) -> Reservation:
    """Create a Reservation helper function"""
    logging.info(f"Creating Reservation: {str(reservation)}")

    # Create the Reservation, if failed raise 400
    model = manager.create(reservation)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservation")

    # Return the created Reservation
    return model


@router.post("/reservation")
def create_reservation(
    reservation: Reservation, manager: ReservationManager = Depends(get_manager)
) -> Reservation:
    """Create a Reservation"""
    # Call the helper function to create the Reservation
    return _create_reservation(reservation, manager)


@router.post("/reservation/async")
async def create_reservation_async(
    reservation: Reservation,
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Create a Reservation asynchronously"""
    logging.info(f"Creating Reservation asynchronously: {str(reservation)}")
    # Create the Reservation asynchronously
    background_tasks.add_task(_create_reservation, reservation, manager)
    # Return the created Reservation
    return {"message": "Creating Reservation asynchronously"}


def _create_reservations(
    reservations: List[Reservation], manager: ReservationManager
) -> List[Reservation]:
    """Create multiple Reservations helper function"""
    logging.info(f"Creating Reservations: {str(reservations)}")

    # Create the Reservations, if failed raise 400
    models = manager.create_many(reservations)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Reservations")

    # Return the created Reservations
    return models


@router.post("/reservations")
def create_reservations(
    reservations: List[Reservation], manager: ReservationManager = Depends(get_manager)
) -> List[Reservation]:
    """Create multiple Reservations"""
    # Call the helper function to create the Reservations
    return _create_reservations(reservations, manager)


@router.post("/reservations/async")
async def create_reservations_async(
    reservations: List[Reservation],
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Create multiple Reservations asynchronously"""
    logging.info(f"Creating Reservations asynchronously: {str(reservations)}")
    # Create the Reservations asynchronously
    background_tasks.add_task(_create_reservations, reservations, manager)
    # Return the created Reservations
    return {"message": "Creating Reservations asynchronously"}


########################################################################################################################
# Update Endpoints for Reservation
########################################################################################################################


def _update_reservation(
    reservation: Reservation, manager: ReservationManager
) -> Reservation:
    """Update a Reservation helper function"""
    logging.info(f"Updating Reservation: {str(reservation)}")

    # Update the Reservation, if failed raise 400
    model = manager.update(reservation)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservation")

    # Return the updated Reservation
    return model


@router.put("/reservation")
def update_reservation(
    reservation: Reservation, manager: ReservationManager = Depends(get_manager)
) -> Reservation:
    """Update a Reservation"""
    # Call the helper function to update the Reservation
    return _update_reservation(reservation, manager)


@router.put("/reservation/async")
async def update_reservation_async(
    reservation: Reservation,
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Update a Reservation asynchronously"""
    logging.info(f"Updating Reservation asynchronously: {str(reservation)}")
    # Update the Reservation asynchronously
    background_tasks.add_task(_update_reservation, reservation, manager)
    # Return the updated Reservation
    return {"message": "Updating Reservation asynchronously"}


def _update_reservations(
    reservations: List[Reservation], manager: ReservationManager
) -> List[Reservation]:
    """Update multiple Reservations helper function"""
    logging.info(f"Updating Reservations: {str(reservations)}")

    # Update the Reservations, if failed raise 400
    models = manager.update_many(reservations)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Reservations")

    # Return the updated Reservations
    return models


@router.put("/reservations")
def update_reservations(
    reservations: List[Reservation], manager: ReservationManager = Depends(get_manager)
) -> List[Reservation]:
    """Update multiple Reservations"""
    # Call the helper function to update the Reservations
    return _update_reservations(reservations, manager)


@router.put("/reservations/async")
async def update_reservations_async(
    reservations: List[Reservation],
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Update multiple Reservations asynchronously"""
    logging.info(f"Updating Reservations asynchronously: {str(reservations)}")
    # Update the Reservations asynchronously
    background_tasks.add_task(_update_reservations, reservations, manager)
    # Return the updated Reservations
    return {"message": "Updating Reservations asynchronously"}


########################################################################################################################
# Delete Endpoints for Reservation
########################################################################################################################


def _delete_reservation(
    reservation_id: int, manager: ReservationManager
) -> Reservation:
    """Delete a Reservation helper function"""
    logging.info(f"Deleting Reservation with id: {id}")

    # Delete the Reservation, if failed raise 404
    model = manager.delete(reservation_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservation")

    # Return the deleted Reservation
    return model


@router.delete("/reservation")
def delete_reservation(
    reservation_id: int, manager: ReservationManager = Depends(get_manager)
) -> Reservation:
    """Delete a Reservation"""
    # Call the helper function to delete the Reservation
    return _delete_reservation(reservation_id, manager)


@router.delete("/reservation/async")
async def delete_reservation_async(
    reservation_id: int,
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Delete a Reservation asynchronously"""
    logging.info(f"Deleting Reservation asynchronously with id: {id}")
    # Delete the Reservation asynchronously
    background_tasks.add_task(_delete_reservation, reservation_id, manager)
    # Return the deleted Reservation
    return {"message": "Deleting Reservation asynchronously"}


def _delete_reservations(
    reservation_ids: List[int], manager: ReservationManager
) -> List[Reservation]:
    """Delete multiple Reservations helper function"""
    logging.info(f"Deleting Reservations: {str(reservation_ids)}")

    # Delete the Reservations, if failed raise 404
    models = manager.delete_many(reservation_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reservations")

    # Return the deleted Reservations
    return models


@router.delete("/reservations")
def delete_reservations(
    reservation_ids: List[int], manager: ReservationManager = Depends(get_manager)
) -> List[Reservation]:
    """Delete multiple Reservations"""
    # Call the helper function to delete the Reservations
    return _delete_reservations(reservation_ids, manager)


@router.delete("/reservations/async")
async def delete_reservations_async(
    reservation_ids: List[int],
    background_tasks: BackgroundTasks,
    manager: ReservationManager = Depends(get_manager),
):
    """Delete multiple Reservations asynchronously"""
    logging.info(f"Deleting Reservations asynchronously: {str(reservation_ids)}")
    # Delete the Reservations asynchronously
    background_tasks.add_task(_delete_reservations, reservation_ids, manager)
    # Return the deleted Reservations
    return {"message": "Deleting Reservations asynchronously"}
