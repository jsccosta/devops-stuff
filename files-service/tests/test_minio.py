import boto3
from moto import mock_aws
import pytest
from app.api.submissions import router
from fastapi.testclient import TestClient
import sys

AWS_ACCESS_KEY_ID='testing'
AWS_SECRET_ACCESS_KEY='testing'
AWS_SECURITY_TOKEN='testing'
AWS_SESSION_TOKEN='testing'
AWS_DEFAULT_REGION='us-east-1'

client = TestClient(router)


@pytest.fixture
def s3_boto():
    """Create an S3 boto3 client and return the client object"""
    
    s3 = boto3.client('s3', region_name='us-east-1')
    return s3

# @mock_aws
# def test_ls(s3_boto):
#     """Test the custom s3 ls function mocking S3 with moto"""
    
#     bucket = "testbucket"
#     key = "testkey"
#     body = "testing"
#     s3_boto.create_bucket(Bucket=bucket)
#     s3_boto.put_object(Bucket=bucket, Key=key, Body=body)
#     ls_output = s3_ls(Bucket=bucket, Prefix=key)
#     assert len(ls_output) == 1
#     assert ls_output[0] == 'testkey'
    
################################################################

# @pytest.mark.asyncio
@mock_aws
def test_make_minio_bucket():
    response = client.post("/minio_make_bucket/mybuckettester")
    assert response.status_code == 200
    assert response.json() == {"message": "Bucket 'test-bucket' created successfully."}

# @pytest.mark.asyncio
@mock_aws
def test_upload_file():
    # Upload file
    response = client.post("/upload-file/", files={"file": ("testfile.txt", b"test file content")})
    assert response.status_code == 200
    assert response.json() == {"message": "File 'testfile.txt' uploaded successfully to bucket 'uploader'."}

# @pytest.mark.asyncio
# @mock_aws
# async def test_delete_file():
#     # Delete file
#     response = client.delete("/delete-file/testfile.txt")
#     assert response.status_code == 200
#     assert response.json() == {"message": "File 'testfile.txt' deleted successfully from bucket 'uploader'."}

# @pytest.mark.asyncio
# @mock_aws
# async def test_list_files():
#     # List files
#     response = client.get("/list-files/")
#     assert response.status_code == 200
#     assert response.json() == {"files": ["file1.txt", "file2.txt"]}