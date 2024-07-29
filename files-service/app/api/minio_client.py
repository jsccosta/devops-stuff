from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException, UploadFile
import datetime
from typing import Optional
from io import BytesIO

class MinioClient():
    def __init__(self):
        self.MINIO_URL = "192.168.49.2"
        self.MINIO_PORT = "9000"
        self.client = Minio(
            endpoint= self.MINIO_URL + ":" + self.MINIO_PORT,
            access_key="adbB9ScJ8l5atyPb",
            secret_key="XX3Ty3vuzErXeS9HxXIQ1AdmqtNsSAbv",
            region="my-region",
            secure=False  # In production, secure should be set to True for TLS/SSL
        )

    async def bucket_make(self, bucket_name:str, location = None):
        try:
            if self.client.bucket_exists(bucket_name):
                return {"message": f"Bucket '{bucket_name}' already exists."}

            self.client.make_bucket(bucket_name, location=location)
            return {"message": f"Bucket '{bucket_name}' created successfully."}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error creating bucket: {e}")

    async def bucket_remove_object(self, bucket_name:str, objects = [], total = False):
        try:
            if not self.client.bucket_exists(bucket_name):
                raise HTTPException(status_code=500, detail=f"Bucket '{bucket_name}' does not exist.")

            if total is False and objects:
                self.client.remove_objects(bucket_name, delete_object_list=objects)
                return {"message": f"Objects '{objects}' removed from Bucket '{bucket_name}' successfully."}
            
            else: self.client.remove_bucket(bucket_name=bucket_name)

        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error removing objects: {e}")

    async def bucket_insert_object(self, bucket_name:str, file: UploadFile, folder: Optional[str] = ''):
        try:
            if not self.client.bucket_exists(bucket_name):
                raise HTTPException(status_code=500, detail=f"Bucket '{bucket_name}' does not exist.")

            data = await file.read()
            data_stream = BytesIO(data)
            length = len(data)

            content_type = file.content_type
            if content_type != "application/pdf":
                raise ValueError(f"The file {file.filename} is not a PDF.")

            # Include the folder name in the object name
            object_name = f"{folder}/{file.filename}" if folder else file.filename

            result = self.client.put_object(
                bucket_name, 
                object_name, 
                data_stream, 
                length, 
                content_type=content_type,
                #num_parallel_uploads=3 #for large files 
            )

            print(f"Uploaded {object_name} with etag {result.etag}")
            return {"message": f"File uploaded to Bucket '{bucket_name}' successfully."}

        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))     
        
    async def buckets_list(self):
        try:
            buckets = self.client.list_buckets()
            if not buckets:
                raise HTTPException(status_code=404, detail="No buckets found.")
            return {"buckets": [bucket.name for bucket in buckets]}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error listing buckets: {e}")

    async def bucket_list_files(self, bucket_name, sub_list=None, get_links=False):
        try:
            if not self.client.bucket_exists(bucket_name):
                raise HTTPException(status_code=500, detail=f"Bucket '{bucket_name}' does not exist.")

            objects = self.client.list_objects(bucket_name)
            file_list = [obj.object_name for obj in objects if sub_list is None or obj.object_name in sub_list]

            if get_links:
                file_links = [self.generate_presigned_url(file_name) for file_name in file_list]
                file_URLs = [self.generate_download_url(file_link) for file_link in file_links]
                return {file_name: url for file_name, url in zip(file_list, file_URLs)}

            return {"files": file_list}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error listing files: {e}")

    async def generate_presigned_url(self, file_name):
        try:
            if not self.client.bucket_exists('reports'):
                raise HTTPException(status_code=404, detail=f"Bucket reports does not exist.")
            
            url = self.client.presigned_get_object(
                'reports',
                file_name,
                expires=datetime.timedelta(hours=1)
            )
            return url
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error generating presigned URL: {e}")

    async def generate_download_url(self, filename):
        try:
            url = f"https://192.168.49.2:9000/reports/{filename}"
            return url
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating download URL: {e}")