from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from src.akkiai.crew import Akkiai
from pathlib import Path

app = FastAPI()

# Define the path for the static directory using an absolute path
#static_dir = Path(__file__).parent / "static"
#app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Define input models for endpoints
class RunInputs(BaseModel):
    BUSINESS_DETAILS: str
    PRODUCT_DESCRIPTION: str

class TrainInputs(BaseModel):
    BUSINESS_DETAILS: str
    PRODUCT_DESCRIPTION: str
    n_iterations: int
    filename: str

class TestInputs(BaseModel):
    BUSINESS_DETAILS: str
    PRODUCT_DESCRIPTION: str
    n_iterations: int
    openai_model_name: str

@app.post("/run")
async def run(inputs: RunInputs):
    
    try:
        print("Received inputs for /run:", inputs.dict())
        Akkiai().crew().kickoff(inputs=inputs.dict())
        return {"message": "Crew run successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running crew: {str(e)}")

@app.post("/train")
async def train(inputs: TrainInputs):
    try:
        Akkiai().crew().train(
            n_iterations=inputs.n_iterations,
            filename=inputs.filename,
            inputs={"BUSINESS_DETAILS": inputs.BUSINESS_DETAILS, "PRODUCT_DESCRIPTION": inputs.PRODUCT_DESCRIPTION},
        )
        return {"message": "Training completed successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error training crew: {str(e)}")

@app.post("/replay")
async def replay(task_id: str):
    try:
        Akkiai().crew().replay(task_id=task_id)
        return {"message": "Replay executed successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error replaying crew: {str(e)}")

@app.post("/test")
async def test(inputs: TestInputs):
    try:
        Akkiai().crew().test(
            n_iterations=inputs.n_iterations,
            openai_model_name=inputs.openai_model_name,
            inputs={"BUSINESS_DETAILS": inputs.BUSINESS_DETAILS, "PRODUCT_DESCRIPTION": inputs.PRODUCT_DESCRIPTION},
        )
        return {"message": "Test executed successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error testing crew: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Welcome to the CrewAI API!"}
