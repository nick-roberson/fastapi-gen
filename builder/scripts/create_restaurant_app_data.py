import json
import random

from faker import Faker

fake = Faker()


# Helper function to generate sample data
def generate_user_samples(n=5):
    return [
        {
            # create fake integer  id
            "id": fake.random_int(min=0, max=10000),
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


def generate_restaurant_samples(n=5):
    return [
        {
            "id": fake.random_int(min=0, max=10000),
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


def generate_reservation_samples(user_ids, restaurant_ids, n=5):
    return [
        {
            "id": fake.random_int(min=0, max=10000),
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


def generate_review_samples(user_ids, restaurant_ids, n=5):
    return [
        {
            "id": fake.random_int(min=0, max=10000),
            "restaurant_id": random.choice(restaurant_ids),
            "user_id": random.choice(user_ids),
            "rating": round(random.uniform(1.0, 5.0), 1),
            "comment": fake.text(max_nb_chars=200),
        }
        for _ in range(n)
    ]


def generate_data(n=5):
    # Generating samples
    user_samples = generate_user_samples(n)
    restaurant_samples = generate_restaurant_samples(n)

    # Extracting user and alembic IDs for reservations and reviews
    user_ids = [user["id"] for user in user_samples]
    restaurant_ids = [restaurant["id"] for restaurant in restaurant_samples]

    reservation_samples = generate_reservation_samples(user_ids, restaurant_ids, n)
    review_samples = generate_review_samples(user_ids, restaurant_ids, n)
    return user_samples, restaurant_samples, reservation_samples, review_samples


if __name__ == "__main__":
    # Generate sample data
    user_samples, restaurant_samples, reservation_samples, review_samples = (
        generate_data(n=20)
    )
    # For each data type write as list to `data/<type>.json`
    with open("data/users.json", "w") as f:
        json.dump(user_samples, f, indent=2)
    with open("data/restaurants.json", "w") as f:
        json.dump(restaurant_samples, f, indent=2)
    with open("data/reservations.json", "w") as f:
        json.dump(reservation_samples, f, indent=2)
    with open("data/reviews.json", "w") as f:
        json.dump(review_samples, f, indent=2)
