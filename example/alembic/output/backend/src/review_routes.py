import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from src.db.review_manager import ReviewManager
from src.models.models import Review, ReviewQuery

# Define Router
router = APIRouter()


def get_manager() -> ReviewManager:
    """Get the Review Manager"""
    return ReviewManager()


########################################################################################################################
# Query Endpoints for Review
########################################################################################################################


@router.post("/review/query")
def query_review(
    query: ReviewQuery, manager: ReviewManager = Depends(get_manager)
) -> List[Review]:
    """Query Reviews"""
    logging.info(f"Querying Reviews with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.model_dump().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in ReviewQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Reviews with the given query, if none found raise 404
    models = manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reviews found")

    # Return the Reviews
    return models


########################################################################################################################
# Get Endpoints for Review
########################################################################################################################


@router.get("/review")
def get_review(review_id: str, manager: ReviewManager = Depends(get_manager)) -> Review:
    """Get a Review"""
    logging.info(f"Getting Review with id: {id}")

    # Get the Review with the given id, if none found raise 404
    model = manager.get(review_id=review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")

    # Return the Review
    return model


@router.get("/reviews")
def get_reviews(
    skip: int = 0, limit: int = 100, manager: ReviewManager = Depends(get_manager)
) -> List[Review]:
    """Get all Reviews"""
    logging.info(f"Getting all Reviews")

    # Get all Reviews, if none found raise 404
    models = manager.get_all(skip=skip, limit=limit)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reviews found")

    # Return all Reviews
    return models


########################################################################################################################
# Create Endpoints for Review
########################################################################################################################


def _create_review(review: Review, manager: ReviewManager) -> Review:
    """Create a Review helper function"""
    logging.info(f"Creating Review: {str(review)}")

    # Create the Review, if failed raise 400
    model = manager.create(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Review")

    # Return the created Review
    return model


@router.post("/review")
def create_review(
    review: Review, manager: ReviewManager = Depends(get_manager)
) -> Review:
    """Create a Review"""
    # Call the helper function to create the Review
    return _create_review(review, manager)


@router.post("/review/async")
async def create_review_async(
    review: Review,
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Create a Review asynchronously"""
    logging.info(f"Creating Review asynchronously: {str(review)}")
    # Create the Review asynchronously
    background_tasks.add_task(_create_review, review, manager)
    # Return the created Review
    return {"message": "Creating Review asynchronously"}


def _create_reviews(reviews: List[Review], manager: ReviewManager) -> List[Review]:
    """Create multiple Reviews helper function"""
    logging.info(f"Creating Reviews: {str(reviews)}")

    # Create the Reviews, if failed raise 400
    models = manager.create_many(reviews)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to create Reviews")

    # Return the created Reviews
    return models


@router.post("/reviews")
def create_reviews(
    reviews: List[Review], manager: ReviewManager = Depends(get_manager)
) -> List[Review]:
    """Create multiple Reviews"""
    # Call the helper function to create the Reviews
    return _create_reviews(reviews, manager)


@router.post("/reviews/async")
async def create_reviews_async(
    reviews: List[Review],
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Create multiple Reviews asynchronously"""
    logging.info(f"Creating Reviews asynchronously: {str(reviews)}")
    # Create the Reviews asynchronously
    background_tasks.add_task(_create_reviews, reviews, manager)
    # Return the created Reviews
    return {"message": "Creating Reviews asynchronously"}


########################################################################################################################
# Update Endpoints for Review
########################################################################################################################


def _update_review(review: Review, manager: ReviewManager) -> Review:
    """Update a Review helper function"""
    logging.info(f"Updating Review: {str(review)}")

    # Update the Review, if failed raise 400
    model = manager.update(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Review")

    # Return the updated Review
    return model


@router.put("/review")
def update_review(
    review: Review, manager: ReviewManager = Depends(get_manager)
) -> Review:
    """Update a Review"""
    # Call the helper function to update the Review
    return _update_review(review, manager)


@router.put("/review/async")
async def update_review_async(
    review: Review,
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Update a Review asynchronously"""
    logging.info(f"Updating Review asynchronously: {str(review)}")
    # Update the Review asynchronously
    background_tasks.add_task(_update_review, review, manager)
    # Return the updated Review
    return {"message": "Updating Review asynchronously"}


def _update_reviews(reviews: List[Review], manager: ReviewManager) -> List[Review]:
    """Update multiple Reviews helper function"""
    logging.info(f"Updating Reviews: {str(reviews)}")

    # Update the Reviews, if failed raise 400
    models = manager.update_many(reviews)
    if not models:
        raise HTTPException(status_code=400, detail=f"Failed to update Reviews")

    # Return the updated Reviews
    return models


@router.put("/reviews")
def update_reviews(
    reviews: List[Review], manager: ReviewManager = Depends(get_manager)
) -> List[Review]:
    """Update multiple Reviews"""
    # Call the helper function to update the Reviews
    return _update_reviews(reviews, manager)


@router.put("/reviews/async")
async def update_reviews_async(
    reviews: List[Review],
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Update multiple Reviews asynchronously"""
    logging.info(f"Updating Reviews asynchronously: {str(reviews)}")
    # Update the Reviews asynchronously
    background_tasks.add_task(_update_reviews, reviews, manager)
    # Return the updated Reviews
    return {"message": "Updating Reviews asynchronously"}


########################################################################################################################
# Delete Endpoints for Review
########################################################################################################################


def _delete_review(review_id: int, manager: ReviewManager) -> Review:
    """Delete a Review helper function"""
    logging.info(f"Deleting Review with id: {id}")

    # Delete the Review, if failed raise 404
    model = manager.delete(review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Review")

    # Return the deleted Review
    return model


@router.delete("/review")
def delete_review(
    review_id: int, manager: ReviewManager = Depends(get_manager)
) -> Review:
    """Delete a Review"""
    # Call the helper function to delete the Review
    return _delete_review(review_id, manager)


@router.delete("/review/async")
async def delete_review_async(
    review_id: int,
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Delete a Review asynchronously"""
    logging.info(f"Deleting Review asynchronously with id: {id}")
    # Delete the Review asynchronously
    background_tasks.add_task(_delete_review, review_id, manager)
    # Return the deleted Review
    return {"message": "Deleting Review asynchronously"}


def _delete_reviews(review_ids: List[int], manager: ReviewManager) -> List[Review]:
    """Delete multiple Reviews helper function"""
    logging.info(f"Deleting Reviews: {str(review_ids)}")

    # Delete the Reviews, if failed raise 404
    models = manager.delete_many(review_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reviews")

    # Return the deleted Reviews
    return models


@router.delete("/reviews")
def delete_reviews(
    review_ids: List[int], manager: ReviewManager = Depends(get_manager)
) -> List[Review]:
    """Delete multiple Reviews"""
    # Call the helper function to delete the Reviews
    return _delete_reviews(review_ids, manager)


@router.delete("/reviews/async")
async def delete_reviews_async(
    review_ids: List[int],
    background_tasks: BackgroundTasks,
    manager: ReviewManager = Depends(get_manager),
):
    """Delete multiple Reviews asynchronously"""
    logging.info(f"Deleting Reviews asynchronously: {str(review_ids)}")
    # Delete the Reviews asynchronously
    background_tasks.add_task(_delete_reviews, review_ids, manager)
    # Return the deleted Reviews
    return {"message": "Deleting Reviews asynchronously"}
