import json
import logging
from typing import List, Optional

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Query
from sqlalchemy.orm import Session

from ..db_config.config import get_db
from ..models.submission_models import *
from ..repository.submissions import SubmissionsRepository
from app.api.minio_client import MinioClient

logger = logging.getLogger(__name__)

router = APIRouter()

client = MinioClient()

@router.post("/bucket-create/{bucket_name}", tags=["minio"])
async def create_bucket(bucket_name: str):
    return await client.bucket_make(bucket_name=bucket_name)

@router.post("/file-upload/{bucket_name}", tags=["minio"])
async def upload_file(bucket_name: str, file: UploadFile = File(...)):
    return await client.bucket_insert_object(bucket_name=bucket_name, file=file, folder='')

@router.post("/file-upload/{bucket_name}/{folder}", tags=["minio"])
async def upload_file_to_folder(bucket_name: str, folder: str, file: UploadFile = File(...)):
    return await client.bucket_insert_object(bucket_name=bucket_name, file=file, folder=folder)

@router.delete("/file-delete/{bucket_name}/{file_name}", tags=["minio"])
async def delete_file(bucket_name: str, file_name: str):
    return await client.bucket_remove_object(bucket_name=bucket_name, objects=[file_name])

@router.delete("/bucket-delete/{bucket_name}", tags=["minio"])
async def delete_bucket(bucket_name: str, total: Optional[bool] = Query(False)):
    return await client.bucket_remove_object(bucket_name=bucket_name, total=total)

@router.get("/bucket-list-files/{bucket_name}", tags=["minio"])
async def list_files(bucket_name: str, sub_list: Optional[List[str]] = Query(None), get_links: Optional[bool] = Query(False)):
    files = await client.bucket_list_files(bucket_name=bucket_name, sub_list=sub_list, get_links=get_links)
    return files


@router.get("/bucket-list-all/", tags=["minio"])
async def list_buckets():
    return await client.buckets_list()


    
# ToDo:
#     get links to files in bucket
#     get buckets per company

"""
@router.post("/upload_for_summarization/", tags=["submissions"])
async def upload_for_summarization(file: UploadFile = File(...), sess: Session = Depends(get_db)):
    folders = ['jobs', 'reports']
    
    # repo:FilesRepository = FilesRepository(sess)
    # data = repo.get_tenant()
    
    # print("-------------------------------")
    # print(file.filename)
    # print("-------------------------------")
    # print("-------------------------------")
    # print('heres the tenant')
    # print(data)
    # print('heres the tenant')
    # print("-------------------------------")
    # print("-------------------------------")
    
    for folder in folders:
        try:
            await upload_file(folder, file)
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")
        
    # summarization
    # summarizedReport = summarize_pdf.summarize(pdf_path=file_path, output_pdf_path=parsed_pdf_path, input_json_path=pdf_json_definitions, output_json_path=output_json_path)
    # upload_file('summarizedReports', summarizedReport)
        
    # return data
    
    
    # for a given tenant create a folder if not exists
    # for a summarization check if folder exists else create it
    # for a summarization create a folder with the execution id - this likely will have to be queued
    # store pdf to summarize in this folder
    # pass in a pdf_path where the file to parse is stored
    # pdf_json_definitions = get_processed_pdf_definition_file()
    # probably add an ID to this, for queue tracking later on?

    # upload_folder_path = os.path.join(target_folder, "test_summarizer_uploads")

    # # If the folder doesn't exist, create it
    # if not os.path.exists(upload_folder_path):
    #     os.makedirs(upload_folder_path)
    #     print(f"Folder '{upload_folder_path}' created successfully.")

    # # if folder contains any content delete it
    # delete_folder_contents(upload_folder_path)
    
    # # get file path
    # file_path = os.path.join(upload_folder_path, file.filename)
    

    
    # try:
    #     # Save the uploaded file
    #     with open(file_path, "wb") as buffer:
    #         shutil.copyfileobj(file.file, buffer)
    #     # Close the file to ensure it's saved before processing
    #     file.file.close()
    #     print('log 1')
    #     current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    #     uploaded_filename = current_datetime+'_'+file.filename
    #     # need to figure out why this is needed
    #     # there's a bunch of processing happening in this file that should likely happen inside the pdf parsing 
    #     # function
    #     print('log 2')
    #     parsed_pdf_path = os.path.join(target_folder, 'structured_document.pdf')
    #     print('log 3')
    #     # If the folder doesn't exist, create it
    #     if not os.path.exists(summarized_pdf_dir):
    #         print('log 4')
    #         os.makedirs(summarized_pdf_dir) 
    #         print(f"Folder '{summarized_pdf_dir}' created successfully.")
    #     print('log 5')
    #     summarized_pdf_path = os.path.join(summarized_pdf_dir, uploaded_filename)
    #     print('log 6')
    #     output_json_path = os.path.join(target_folder, 'summary.json')
    #     print('log 7')
    #     summary = summarize_pdf.summarize(pdf_path=file_path, output_pdf_path=parsed_pdf_path,
    #                         input_json_path=pdf_json_definitions, output_json_path=output_json_path)
    #     print('log 8')
    #     print('---------------------------------------------------------------')
    #     print('---------------------------------------------------------------')
    #     print('file_path')
    #     print(file_path)
    #     print('parsed_pdf_path')
    #     print(parsed_pdf_path)
    #     print('pdf_json_definitions')
    #     print(pdf_json_definitions)
    #     print('output_json_path')
    #     print(output_json_path)
    #     print('---------------------------------------------------------------')
    #     print('---------------------------------------------------------------')
    #     print('---------------------------------------------------------------')
    #     print('---------------------------------------------------------------')
        
    #     # pdf_convertor.generate_pdf(json_data=summary, output_filepath=summarized_pdf_path)
    #     # # clean up
    #     # os.remove(file_path)
    #     # os.remove(output_json_path)
    #     # os.remove(parsed_pdf_path)
    #     # document_name = ' '.join(word.capitalize() for word in uploaded_filename.split('.')[0].split('_'))

    #     return {
    #         "summary": {
    #             # "raw": summary,
    #                     # "pdf": 'http://localhost:8000/engineering_reports/'+uploaded_filename,
    #                     # "document_name": document_name,
    #                     "summarized_at": datetime.now().strftime("%Y/%m/%d")},
    #         "status": "uploaded",
    #     }

    # except Exception as e:
    #     return JSONResponse(content={"error": str(e)}, status_code=500)
"""