import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks, HTTPException
from src.db.review_manager import get_review_manager
from src.models.models import Review, ReviewQuery

# Create instances of managers for each model

review_manager = get_review_manager()


# Define Router
router = APIRouter()


########################################################################################################################
# Query Endpoints for Review
########################################################################################################################


@router.post("/review/query")
def query_review(query: ReviewQuery) -> List[Review]:
    """Query Reviews"""
    logging.info(f"Querying Reviews with query: {str(query)}")

    # If all fields are None in the query return 400
    if not any(query.dict().values()):
        allowed_fields = ", ".join(
            [field_name for field_name in ReviewQuery.__fields__.keys()]
        )
        detail = f"Query fields cannot all be None, must have at least one field set. Allowed fields: {allowed_fields}"
        raise HTTPException(status_code=400, detail=detail)

    # Query the Reviews with the given query, if none found raise 404
    models = review_manager.query(query)
    if not models:
        raise HTTPException(status_code=404, detail=f"No Reviews found")

    # Return the Reviews
    return models


########################################################################################################################
# Get Endpoints for Review
########################################################################################################################


@router.get("/review")
def get_review(review_id: str) -> Review:
    """Get a Review"""
    logging.info(f"Getting Review with id: {id}")

    # Get the Review with the given id, if none found raise 404
    model = review_manager.get(review_id=review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")

    # Return the Review
    return model


@router.get("/reviews")
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
# Create Endpoints for Review
########################################################################################################################


def _create_review(review: Review) -> Review:
    """Create a Review helper function"""
    logging.info(f"Creating Review: {str(review)}")

    # Create the Review, if failed raise 400
    model = review_manager.create(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to create Review")

    # Return the created Review
    return model


@router.post("/review")
def create_review(review: Review) -> Review:
    """Create a Review"""
    # Call the helper function to create the Review
    return _create_review(review)


@router.post("/review/async")
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


@router.post("/reviews")
def create_reviews(reviews: List[Review]) -> List[Review]:
    """Create multiple Reviews"""
    # Call the helper function to create the Reviews
    return _create_reviews(reviews)


@router.post("/reviews/async")
def create_reviews_async(reviews: List[Review], background_tasks: BackgroundTasks):
    """Create multiple Reviews asynchronously"""
    logging.info(f"Creating Reviews asynchronously: {str(reviews)}")
    # Create the Reviews asynchronously
    background_tasks.add_task(_create_reviews, reviews)
    # Return the created Reviews
    return {"message": "Creating Reviews asynchronously"}


########################################################################################################################
# Update Endpoints for Review
########################################################################################################################


def _update_review(review: Review) -> Review:
    """Update a Review helper function"""
    logging.info(f"Updating Review: {str(review)}")

    # Update the Review, if failed raise 400
    model = review_manager.update(review)
    if not model:
        raise HTTPException(status_code=400, detail=f"Failed to update Review")

    # Return the updated Review
    return model


@router.put("/review")
def update_review(review: Review) -> Review:
    """Update a Review"""
    # Call the helper function to update the Review
    return _update_review(review)


@router.put("/review/async")
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


@router.put("/reviews")
def update_reviews(reviews: List[Review]) -> List[Review]:
    """Update multiple Reviews"""
    # Call the helper function to update the Reviews
    return _update_reviews(reviews)


@router.put("/reviews/async")
def update_reviews_async(reviews: List[Review], background_tasks: BackgroundTasks):
    """Update multiple Reviews asynchronously"""
    logging.info(f"Updating Reviews asynchronously: {str(reviews)}")
    # Update the Reviews asynchronously
    background_tasks.add_task(_update_reviews, reviews)
    # Return the updated Reviews
    return {"message": "Updating Reviews asynchronously"}


########################################################################################################################
# Delete Endpoints for Review
########################################################################################################################


def _delete_review(review_id: int) -> Review:
    """Delete a Review helper function"""
    logging.info(f"Deleting Review with id: {id}")

    # Delete the Review, if failed raise 404
    model = review_manager.delete(review_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Failed to delete Review")

    # Return the deleted Review
    return model


@router.delete("/review")
def delete_review(review_id: int) -> Review:
    """Delete a Review"""
    # Call the helper function to delete the Review
    return _delete_review(review_id)


@router.delete("/review/async")
def delete_review_async(review_id: int, background_tasks: BackgroundTasks):
    """Delete a Review asynchronously"""
    logging.info(f"Deleting Review asynchronously with id: {id}")
    # Delete the Review asynchronously
    background_tasks.add_task(_delete_review, review_id)
    # Return the deleted Review
    return {"message": "Deleting Review asynchronously"}


def _delete_reviews(review_ids: List[int]) -> List[Review]:
    """Delete multiple Reviews helper function"""
    logging.info(f"Deleting Reviews: {str(review_ids)}")

    # Delete the Reviews, if failed raise 404
    models = review_manager.delete_many(review_ids)
    if not models:
        raise HTTPException(status_code=404, detail=f"Failed to delete Reviews")

    # Return the deleted Reviews
    return models


@router.delete("/reviews")
def delete_reviews(review_ids: List[int]) -> List[Review]:
    """Delete multiple Reviews"""
    # Call the helper function to delete the Reviews
    return _delete_reviews(review_ids)


@router.delete("/reviews/async")
def delete_reviews_async(review_ids: List[int], background_tasks: BackgroundTasks):
    """Delete multiple Reviews asynchronously"""
    logging.info(f"Deleting Reviews asynchronously: {str(review_ids)}")
    # Delete the Reviews asynchronously
    background_tasks.add_task(_delete_reviews, review_ids)
    # Return the deleted Reviews
    return {"message": "Deleting Reviews asynchronously"}
