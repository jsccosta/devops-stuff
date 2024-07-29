import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import submissions

python_path = os.getenv("PYTHONPATH")


app = FastAPI(title="Silas Submissions Service")

app.include_router(submissions.router, prefix="/api/v1")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("api_main:app", reload=True)
