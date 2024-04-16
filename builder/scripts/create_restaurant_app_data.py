import argparse
import json
import random

from faker import Faker

fake = Faker()


# Helper function to generate sample data
def generate_user_samples(n: int = 5, db_type: str = "alembic"):
    """Generate sample data for Alembic or Mongo. If using MongoDB, we need to set the IDS as strings. If using Alembic, we can use integers."""
    return [
        {
            # create fake integer  id
            "id": (
                fake.random_int(min=0, max=10000)
                if db_type == "alembic"
                else str(fake.random_int(min=0, max=10000))
            ),
            "username": fake.user_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "preferences": random.choices(
                ["vegan", "italian", "mexican", "chinese", "japanese"], k=2
            ),
            "role": random.choice(["user", "admin", "restaurant_owner"]),
        }
        for _ in range(n)
    ]


def generate_restaurant_samples(n: int = 5, db_type: str = "alembic"):
    """Generate sample data for Alembic or Mongo. If using MongoDB, we need to set the IDS as strings. If using Alembic, we can use integers."""
    return [
        {
            "id": (
                fake.random_int(min=0, max=10000)
                if db_type == "alembic"
                else str(fake.random_int(min=0, max=10000))
            ),
            "name": fake.company(),
            "location": fake.address(),
            "cuisine": random.choice(
                ["Italian", "Mexican", "Chinese", "Japanese", "American"]
            ),
            "rating": round(random.uniform(1.0, 5.0), 1),
            "price_range": random.choice(["$", "$$", "$$$", "$$$$"]),
        }
        for _ in range(n)
    ]


def generate_reservation_samples(
    user_ids, restaurant_ids, n=5, db_type: str = "alembic"
):
    """Generate sample data for Alembic or Mongo. If using MongoDB, we need to set the IDS as strings. If using Alembic, we can use integers."""
    return [
        {
            "id": (
                fake.random_int(min=0, max=10000)
                if db_type == "alembic"
                else str(fake.random_int(min=0, max=10000))
            ),
            "restaurant_id": random.choice(restaurant_ids),
            "user_id": random.choice(user_ids),
            "reservation_time": fake.future_date(end_date="+30d").isoformat()
            + "T"
            + fake.time(),
            "party_size": random.randint(1, 10),
            "special_requests": random.choice(
                ["Window seat", "Birthday decoration", None]
            ),
        }
        for _ in range(n)
    ]


def generate_review_samples(user_ids, restaurant_ids, n=5, db_type: str = "alembic"):
    """Generate sample data for Alembic or Mongo. If using MongoDB, we need to set the IDS as strings. If using Alembic, we can use integers."""
    return [
        {
            "id": (
                fake.random_int(min=0, max=10000)
                if db_type == "alembic"
                else str(fake.random_int(min=0, max=10000))
            ),
            "restaurant_id": random.choice(restaurant_ids),
            "user_id": random.choice(user_ids),
            "rating": round(random.uniform(1.0, 5.0), 1),
            "comment": fake.text(max_nb_chars=200),
        }
        for _ in range(n)
    ]


def generate_data(n: int = 5, db_type: str = "alembic"):
    """Generate sample data for Alembic or Mongo. If using MongoDB, we need to set the IDS as strings. If using Alembic, we can use integers."""
    # Generating samples
    user_samples = generate_user_samples(n, db_type)
    restaurant_samples = generate_restaurant_samples(n, db_type)

    # Extracting user and alembic IDs for reservations and reviews
    user_ids = [user["id"] for user in user_samples]
    restaurant_ids = [restaurant["id"] for restaurant in restaurant_samples]

    reservation_samples = generate_reservation_samples(
        user_ids, restaurant_ids, n, db_type
    )
    review_samples = generate_review_samples(user_ids, restaurant_ids, n, db_type)
    return user_samples, restaurant_samples, reservation_samples, review_samples


def parse_args():
    parser = argparse.ArgumentParser(description="Generate sample data for Alembic")
    parser.add_argument(
        "--num-samples",
        "-n",
        type=int,
        default=5,
        help="Number of samples to generate for each data type",
    )
    parser.add_argument(
        "--db-type",
        "-d",
        type=str,
        default="alembic",
        help="Type of database to generate data for",
    )
    return parser.parse_args()


if __name__ == "__main__":
    """Generate sample data for Alembic or Mongo

    Run like:
        > poetry run python create_restaurant_app_data.py --num-samples 10 --db-type alembic
        > poetry run python create_restaurant_app_data.py --num-samples 10 --db-type mongo
    """
    # Parse command line arguments
    args = parse_args()

    # Generate sample data
    user_samples, restaurant_samples, reservation_samples, review_samples = (
        generate_data(n=args.num_samples, db_type=args.db_type)
    )

    # For each data type write as list to `data/<type>.json`
    with open(f"data/{args.db_type}/users.json", "w") as f:
        json.dump(user_samples, f, indent=2)
    with open(f"data/{args.db_type}/restaurants.json", "w") as f:
        json.dump(restaurant_samples, f, indent=2)
    with open(f"data/{args.db_type}/reservations.json", "w") as f:
        json.dump(reservation_samples, f, indent=2)
    with open(f"data/{args.db_type}/reviews.json", "w") as f:
        json.dump(review_samples, f, indent=2)
