import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.file_handling import router


# python_path = os.getenv("PYTHONPATH")

# current_directory = os.path.dirname(os.path.abspath(__file__))
# folder_path = os.path.join(current_directory, "test")

# directory = '../test_uploads'
# static_directory = "../engineering_reports"

# # Create the directory if it doesn't exist
# if not os.path.exists(directory):
#     os.makedirs(directory)

# if not os.path.exists(static_directory):
#     os.makedirs(static_directory)

app = FastAPI(title="Silas File Handling")

app.include_router(router, prefix="/api/v1/files")  # Include the router from file_handling

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("api.main:app", reload=True)
