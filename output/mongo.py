import sys
import os
import certifi

from pymongo.mongo_client import MongoClient
from pymongo.errors import ConfigurationError

MONGO_URI: str = os.environ.get("MONGO_URI")


def get_client():
    """Gets MongoDB client"""
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
        client.admin.command("ping")
    except ConfigurationError:
        print(
            "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
        )
        sys.exit(1)
    return client


def get_collection(client, collection_name):
    db = client.myDatabase
    return db[collection_name]
