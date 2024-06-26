import argparse
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.utils import ensure_all_tables
from src.reservation_routes import router as reservation_rotes
from src.restaurant_routes import router as restaurant_rotes
from src.review_routes import router as review_rotes
from src.user_routes import router as user_rotes

# Create FastAPI App and Allow CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add startup event to ensure all tables are created
@app.on_event("startup")
async def startup_event():
    """Startup Event"""
    await ensure_all_tables()


# Default Host and Port
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8000

# Add the API Routes
app.include_router(user_rotes, tags=["User"])
app.include_router(restaurant_rotes, tags=["Restaurant"])
app.include_router(reservation_rotes, tags=["Reservation"])
app.include_router(review_rotes, tags=["Review"])


########################################################################################################################
# Root and Health Endpoints
########################################################################################################################


@app.get("/")
async def root():
    """Root Endpoint"""
    return {"message": "Welcome to restaurant_app API"}


@app.get("/health")
async def health():
    """Health Endpoint"""
    return {"message": "Healthy"}


@app.get("/ready")
async def health():
    """Ready Endpoint"""
    return {"message": "Ready"}


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
