import json
import logging
from typing import List

from minio import Minio
from minio.error import S3Error
import datetime

from fastapi import HTTPException
from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..db_config.config import get_db
from ..models.submission_models import *
from ..repository.submissions import SubmissionsRepository

logger = logging.getLogger(__name__)

router = APIRouter()

# Create client with access and secret key.
client = Minio("s3.amazonaws.com", "ACCESS-KEY", "SECRET-KEY")

# Create client with access key and secret key with specific region.
MINIO_URL="http://192.168.49.2"
MINIO_PORT="9000"

MINIO_PATH = f"{MINIO_URL.split('//')[1]}:{MINIO_PORT}"

# Minio Client: List of objects Bucket
client = Minio(
    MINIO_PATH,
    access_key="9DcrjfBuZn6QVB5F",
    secret_key="h7g79N1TpMgvAjL8MmbOKOFdAJL2p0OJ",
    region="my-region",
    # this connects not using TLS - definitely not what we want in production
    secure=False
)

# http://192.168.49.2:9001/login

# Create client with custom HTTP client using proxy server.

# client = Minio(
#     "SERVER:PORT",
#     access_key="ACCESS_KEY",
#     secret_key="SECRET_KEY",
#     secure=True,
#     http_client=urllib3.ProxyManager(
#         "https://PROXYSERVER:PROXYPORT/",
#         timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
#         cert_reqs="CERT_REQUIRED",
#         retries=urllib3.Retry(
#             total=5,
#             backoff_factor=0.2,
#             status_forcelist=[500, 502, 503, 504],
#         ),
#     ),
# )

# this bucket name should be inferred from the client name 
# this is something that will have to exist in the session information
MINIO_BUCKET_NAME='uploader'

# End-point to list existing buckets
# Prints existing buckets and their creation date
# Returns: buckets list
@router.get("/minio/", tags=["minio"])
async def get_minio_buckets():
    buckets = client.list_buckets()
    for bucket in buckets:
        print(bucket.name, bucket.creation_date)
    return buckets

# End-point to create a Minio Bucket
# Checks wheter the bucket already exists, 
#   if it does: returnes message
#   if it doens't: creates bucket, returns message
#   if neither is possible: raises error
@router.post("/minio_make_bucket/{bucket_name}", tags=["minio"])
async def make_minio_bucket(bucket_name: str):
    try:
        # Check if the bucket already exists
        if client.bucket_exists(bucket_name):
            return {"message": f"Bucket '{bucket_name}' already exists."}
        
        # client.make_bucket(bucket_name, "us-west-1")
        # consider whether as we later want to consider adding regions when creating the buckets
        client.make_bucket(bucket_name)
        
        return {"message": f"Bucket '{bucket_name}' created successfully."}
        
    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Error creating bucket: {e}")

# End-point to Upload files
# VERIFIY: there is a condition for the creation of a bucket if this one doesn't exist
# Assuming the user is uploading a file, a registry of this user must have been done
# if that's the case, a creation of a bucket for that user should already be in place
# thus this condition is unecessary and can lead to the overcreation of buckets
@router.post("/upload-file/", tags=["minio"])
async def upload_file(file: UploadFile = File(...)):
    try:
        # Check if the bucket exists, create if not
        if not client.bucket_exists(MINIO_BUCKET_NAME):
            client.make_bucket(MINIO_BUCKET_NAME)

        # Upload the file to MinIO directly
        client.put_object(
            MINIO_BUCKET_NAME,
            file.filename,
            file.file,
            length=-1,  # Use -1 if you don't know the file length
            part_size=10*1024*1024  # 10MB part size for multipart upload
        )

        return {"message": f"File '{file.filename}' uploaded successfully to bucket '{MINIO_BUCKET_NAME}'."}

    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")

# End-point to deletion of a Minio Bucket
# Checks wheter the bucket exists, 
#   if it doens't: raises error with message 
#   if it does: removes bucket from Minio and returns message
#   if neither is possible: raises error
@router.delete("/delete-file/{file_name}", tags=["minio"])
async def delete_file(file_name: str):
    try:
        # Check if the bucket exists
        if not client.bucket_exists(MINIO_BUCKET_NAME):
            raise HTTPException(status_code=404, detail=f"Bucket '{MINIO_BUCKET_NAME}' does not exist.")

        # Remove the file from the bucket
        client.remove_object(MINIO_BUCKET_NAME, file_name)
        return {"message": f"File '{file_name}' deleted successfully from bucket '{MINIO_BUCKET_NAME}'."}

    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {e}")

# End-point to list files in a Minio Bucket
# Checks wheter the bucket exists, 
#   if it does, lists the files and returns their names
#   if it doensn't, raises error
#   if neither is possible: raises error

# possible edition -> 
"""
@router.get("/list-files/", tags=["minio"])
async def list_files(sub_list=None, get_links=False):
    try:
        # Check if the bucket exists
        if not client.bucket_exists(MINIO_BUCKET_NAME):
            raise HTTPException(status_code=404, detail=f"Bucket '{MINIO_BUCKET_NAME}' does not exist.")

        # List files in the bucket
        objects = client.list_objects(MINIO_BUCKET_NAME)
        
        # Check if sub_list is provided and is a list
        if sub_list is not None and isinstance(sub_list, list):
            file_list = [obj.object_name for obj in objects if obj.object_name in sub_list]
        else:
            file_list = [obj.object_name for obj in objects]
        
        # Generate presigned URLs if get_links is True
        if get_links:
            file_links = [generate_presigned_url(file_name) for file_name in file_list]
            return {"files": file_list, "links": file_links}
        return {"files": file_list}

    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Error listing files: {e}")
"""
@router.get("/list-files/", tags=["minio"])
async def list_files():
    try:
        # Check if the bucket exists
        if not client.bucket_exists(MINIO_BUCKET_NAME):
            raise HTTPException(status_code=404, detail=f"Bucket '{MINIO_BUCKET_NAME}' does not exist.")

        # List files in the bucket
        objects = client.list_objects(MINIO_BUCKET_NAME)
        file_list = [obj.object_name for obj in objects]
        return {"files": file_list}

    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Error listing files: {e}")
    

# ToDo:
#     get links to files in bucket
#     get buckets per company



# async def generate_presigned_url(file_name: str):
#     try:
#         # Check if the bucket exists
#         if not client.bucket_exists(MINIO_BUCKET_NAME):
#             raise HTTPException(status_code=404, detail=f"Bucket '{MINIO_BUCKET_NAME}' does not exist.")
        
#         # Generate a presigned URL valid for 1 hour
#         url = client.presigned_get_object(
#             MINIO_BUCKET_NAME,
#             file_name,
#             expires=datetime.timedelta(hours=1)
#         )
#         return {"url": url}

#     except S3Error as e:
#         raise HTTPException(status_code=500, detail=f"Error generating presigned URL: {e}")


@router.get("/submissions/", tags=["submissions"])
def get_all_submissions(sess: Session = Depends(get_db)):
    repo:SubmissionsRepository = SubmissionsRepository(sess)
    data = repo.get_all_submissions()
    return data

@router.get("/submission", tags=["submissions"])
def get_submission(submission_id: int, sess: Session = Depends(get_db)):
    repo:SubmissionsRepository = SubmissionsRepository(sess)
    data = repo.get_submission(submission_id)
    return data

@router.post("/submission/", tags=["submissions"])
async def add_submission(
    account_name: str = Form(...),
    underwriter: str = Form(...),
    domicile: str = Form(...),
    broker: str = Form(...),
    files: List[UploadFile] = File(...),
    sess: Session = Depends(get_db)
):
    filenames = [file.filename for file in files]
    filenames_json = json.dumps({"filenames": filenames})
    repo:SubmissionsRepository = SubmissionsRepository(sess)
    
    submission = Submission(
        account_name=account_name,
        underwriter=underwriter,
        domicile=domicile,
        broker=broker,
        filenames=filenames_json,
    )
    
    result = repo.insert_submission(submission)
    
    if result == True:
        return {
        "status_code": 200,
        "message": "Submission Received",
        "filenames": filenames,
    }
    else: 
        return JSONResponse(content={'message':'problem creating submission encountered'}, status_code=500) 
    
