from sqlalchemy import create_engine
from src.db.constants import get_url
from src.db.models import DBReservation, DBRestaurant, DBReview, DBUser


async def ensure_all_tables():
    """Create all tables if they do not exist"""
    engine = create_engine(get_url())
    # Create the tables

    print(f"Ensuring table for DBUser")
    DBUser.metadata.create_all(engine)

    print(f"Ensuring table for DBRestaurant")
    DBRestaurant.metadata.create_all(engine)

    print(f"Ensuring table for DBReservation")
    DBReservation.metadata.create_all(engine)

    print(f"Ensuring table for DBReview")
    DBReview.metadata.create_all(engine)
