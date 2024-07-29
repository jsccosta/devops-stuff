from fastapi import APIRouter, File, UploadFile

import os
import shutil
from typing import Dict, Set

from pdf_processing import pdf_utils

router = APIRouter()


@router.post("/upload/", tags=["files"])
async def upload_documents(
    previous_document_version: UploadFile = File(...),
    current_document_version: UploadFile = File(...),
):

    # ToDo: drive this from configs
    # Get the parent directory
    parent_directory = os.path.dirname(os.getcwd())
    upload_folder = parent_directory+"/test_uploads"
    
    os.makedirs(upload_folder, exist_ok=True)

    # Save the uploaded file to the upload folder
    with open(
        os.path.join(upload_folder, previous_document_version.filename), "wb"
    ) as buffer1, open(
        os.path.join(upload_folder, current_document_version.filename), "wb"
    ) as buffer2:
        shutil.copyfileobj(previous_document_version.file, buffer1)
        shutil.copyfileobj(current_document_version.file, buffer2)

    previous_doc = upload_folder + "/" + previous_document_version.filename
    current_doc = upload_folder + "/" + current_document_version.filename

    doc_diffs = pdf_utils.extract_differences(previous_doc, current_doc)

    # Invoke the text_extraction function
    results = pdf_utils.text_extraction([previous_doc, current_doc])
    # Destructure the results into variables
    pdf1_dic = results[previous_doc]
    pdf2_dic = results[current_doc]

    current_directory = os.getcwd()
    # Get the parent directory
    parent_directory = os.path.dirname(current_directory)
    upload_folder = parent_directory+"/test_uploads"  

    # ToDo: Rewrite this function
    pdf_utils.comparison_writer(pdf_index = '1', file_path = previous_doc,  results = doc_diffs,  upload_folder = upload_folder)
    pdf_utils.comparison_writer(pdf_index = '2', file_path = current_doc, results = doc_diffs,  upload_folder = upload_folder)

    return {
        "filepaths": {
            "original_file": 'http://localhost:8000/static/'+os.path.splitext(previous_document_version.filename)[0]+'_previous.pdf',
            "new_file": 'http://localhost:8000/static/'+os.path.splitext(current_document_version.filename)[0]+'_current.pdf'
        },
        "parsedFiles": {"original": pdf1_dic, "current": pdf2_dic},
        "status": "uploaded",
    }
    
