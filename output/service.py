import logging

# FastAPI Imports
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Output Imports
from models.models import Task, Input, Output

# Pydantic Imports
from pydantic import BaseModel
from typing import List

# Manager Imports
from task_manager import TaskManager
from input_manager import InputManager
from output_manager import OutputManager


# Create instances of managers for each model

task_manager = TaskManager()

input_manager = InputManager()

output_manager = OutputManager()


logger = logging.getLogger(__name__)

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
# Get Endpoints for Task, Input, Output
##############################################


@app.get("/task")
def get_task(task_id: str):
    logging.info(f"Getting Task with id: {id}")
    return task_manager.get(task_id=task_id)


@app.get("/tasks")
def get_tasks() -> List[Task]:
    logging.info(f"Getting all Tasks")
    return task_manager.get_all()


@app.get("/input")
def get_input(input_id: str):
    logging.info(f"Getting Input with id: {id}")
    return input_manager.get(input_id=input_id)


@app.get("/inputs")
def get_inputs() -> List[Input]:
    logging.info(f"Getting all Inputs")
    return input_manager.get_all()


@app.get("/output")
def get_output(output_id: str):
    logging.info(f"Getting Output with id: {id}")
    return output_manager.get(output_id=output_id)


@app.get("/outputs")
def get_outputs() -> List[Output]:
    logging.info(f"Getting all Outputs")
    return output_manager.get_all()


##############################################
# Create Endpoints for Task, Input, Output
##############################################


@app.post("/task")
def create_task(task: Task):
    logging.info(f"Creating Task: {str(task)}")
    return task_manager.create(task)


@app.post("/input")
def create_input(input: Input):
    logging.info(f"Creating Input: {str(input)}")
    return input_manager.create(input)


@app.post("/output")
def create_output(output: Output):
    logging.info(f"Creating Output: {str(output)}")
    return output_manager.create(output)


##############################################
# Update Endpoints for Task, Input, Output
##############################################


@app.put("/task")
def update_task(task: Task):
    logging.info(f"Updating Task: {str(task)}")
    return task_manager.update(task)


@app.put("/input")
def update_input(input: Input):
    logging.info(f"Updating Input: {str(input)}")
    return input_manager.update(input)


@app.put("/output")
def update_output(output: Output):
    logging.info(f"Updating Output: {str(output)}")
    return output_manager.update(output)


##############################################
# Delete Endpoints for Task, Input, Output
##############################################


@app.delete("/task/id")
def delete_task(task_id: str):
    return task_manager.delete(task_id=task_id)


@app.delete("/input/id")
def delete_input(input_id: str):
    return input_manager.delete(input_id=input_id)


@app.delete("/output/id")
def delete_output(output_id: str):
    return output_manager.delete(output_id=output_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5000)
