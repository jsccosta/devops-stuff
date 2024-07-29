
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .api import users, submissions, summarizer

python_path = os.getenv("PYTHONPATH")

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_directory, "test")

directory = '../test_uploads'
# engineering = '../engineering'
static_directory = "../engineering_reports"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

if not os.path.exists(static_directory):
    os.makedirs(static_directory)

app = FastAPI(title="Silas Backend")

# app.mount("/static", StaticFiles(directory=directory))
# app.mount("/engineering_reports", StaticFiles(directory=static_directory))

app.include_router(users.router, prefix="/api/v1")
app.include_router(submissions.router, prefix="/api/v1")
app.include_router(summarizer.router, prefix="/api/v1")
# app.include_router(files.router, prefix="/api/v1")

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
