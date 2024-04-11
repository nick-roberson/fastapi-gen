import argparse
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.reservation_routes import router as ReservationRoutes
from routes.restaurant_routes import router as RestaurantRoutes
from routes.review_routes import router as ReviewRoutes
from routes.user_routes import router as UserRoutes

# Create FastAPI App and Allow CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Default Host and Port
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8000

# Add the API Routes
app.include_router(UserRoutes, tags=["User"])
app.include_router(RestaurantRoutes, tags=["Restaurant"])
app.include_router(ReservationRoutes, tags=["Reservation"])
app.include_router(ReviewRoutes, tags=["Review"])


########################################################################################################################
# Root and Health Endpoints
########################################################################################################################


@app.get("/")
async def root():
    """Root Endpoint"""
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    """Health Endpoint"""
    return {"message": "Healthy"}


########################################################################################################################
# Logging
########################################################################################################################


def init_logging():
    """Initialize Logging"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)


########################################################################################################################
# Parse Command Line Arguments
########################################################################################################################


def parse_args():
    """Parse Command Line Arguments"""
    parser = argparse.ArgumentParser(description="Run the FastAPI Server")
    parser.add_argument(
        "--host", "-h", type=str, default=DEFAULT_HOST, help="Host to run the server on"
    )
    parser.add_argument(
        "--port", "-p", type=int, default=DEFAULT_PORT, help="Port to run the server on"
    )
    return parser.parse_args()


########################################################################################################################
# Run the Server
########################################################################################################################


if __name__ == "__main__":
    # Initialize Logging
    init_logging()
    # Parse Command Line Arguments
    args = parse_args()
    # Start the server
    uvicorn.run(app, host=args.host, port=args.port)
