import logging
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.models import Group, User

# Create instances of managers for each model


# Create FastAPI App and Allow CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


##############################################
# Get Endpoints for User, Group
##############################################


##############################################
# Create Endpoints for User, Group
##############################################


##############################################
# Update Endpoints for User, Group
##############################################


##############################################
# Delete Endpoints for User, Group
##############################################


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Start the server
    uvicorn.run(app, host="localhost", port=8000)
