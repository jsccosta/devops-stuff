import os
import shutil
import logging
from typing import List
from datetime import datetime

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from ..documet_processors.pdf_summarizing import summarize_pdf, pdf_convertor

logger = logging.getLogger(__name__)
router = APIRouter()

def get_processed_pdf_definition_file():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    processor_folder_path = os.path.join(os.path.dirname(current_dir), "pdf_process_helpers")
    summary_template_path = os.path.join(processor_folder_path, "summary_template.json")

    # Check if the file exists
    if os.path.exists(summary_template_path):
        return summary_template_path
    else:
        print("summary_template.json file not found in the 'processor' folder.")
        return None


def list_files_in_folder(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files

# A new endpoint for summarizing and returning document summary as JSON.
# @router.get("/get_summaries/", tags=["submissions"])
# def summarize_document():
#     upload_folder = os.path.join(os.path.dirname(os.getcwd()), 'engineering_reports')
    
#     files = list_files_in_folder(upload_folder)
#     file_objects = []
#     for filename in files:
#         file_objects.append({
#             "filename": filename, 
#             "processed_at": datetime.strptime(filename[:14], "%Y%m%d%H%M%S").strftime("%Y/%m/%d %H:%M:%S"),
#             "file_path": 'http://localhost:8000/engineering_reports/'+filename
#             })
    
#     return file_objects

def delete_folder_contents(folder_path):
    try:
        # Iterate over the files and subdirectories in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if the path is a file or a directory
            if os.path.isfile(file_path):
                # If it's a file, delete it
                os.remove(file_path)
            elif os.path.isdir(file_path):
                # If it's a directory, delete it recursively
                shutil.rmtree(file_path)
        print(f"Deleted all contents within the folder: {folder_path}")
    except Exception as e:
        print(f"An error occurred while deleting contents: {e}")

@router.post("/summarize_document/", tags=["submissions"])
def summarize_document(file: UploadFile = File(...)):
    # for a given tenant create a folder if not exists
    # for a summarization check if folder exists else create it
    # for a summarization create a folder with the execution id - this likely will have to be queued
    # store pdf to summarize in this folder
    # pass in a pdf_path where the file to parse is stored
    pdf_json_definitions = get_processed_pdf_definition_file()
    target_folder = "/submission_data"
    summarized_pdf_dir = "/summarized_documents"
    upload_folder_path = os.path.join(target_folder, "test_summarizer_uploads")

    # If the folder doesn't exist, create it
    if not os.path.exists(upload_folder_path):
        os.makedirs(upload_folder_path)
        print(f"Folder '{upload_folder_path}' created successfully.")

    # if folder contains any content delete it
    delete_folder_contents(upload_folder_path)
    
    # get file path
    file_path = os.path.join(upload_folder_path, file.filename)
    

    
    try:
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Close the file to ensure it's saved before processing
        file.file.close()
        print('log 1')
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        uploaded_filename = current_datetime+'_'+file.filename
        # need to figure out why this is needed
        # there's a bunch of processing happening in this file that should likely happen inside the pdf parsing 
        # function
        print('log 2')
        parsed_pdf_path = os.path.join(target_folder, 'structured_document.pdf')
        print('log 3')
        # If the folder doesn't exist, create it
        if not os.path.exists(summarized_pdf_dir):
            print('log 4')
            os.makedirs(summarized_pdf_dir) 
            print(f"Folder '{summarized_pdf_dir}' created successfully.")
        print('log 5')
        summarized_pdf_path = os.path.join(summarized_pdf_dir, uploaded_filename)
        print('log 6')
        output_json_path = os.path.join(target_folder, 'summary.json')
        print('log 7')
        summary = summarize_pdf.summarize(pdf_path=file_path, output_pdf_path=parsed_pdf_path,
                            input_json_path=pdf_json_definitions, output_json_path=output_json_path)
        print('log 8')
        print('---------------------------------------------------------------')
        print('---------------------------------------------------------------')
        print('file_path')
        print(file_path)
        print('parsed_pdf_path')
        print(parsed_pdf_path)
        print('pdf_json_definitions')
        print(pdf_json_definitions)
        print('output_json_path')
        print(output_json_path)
        print('---------------------------------------------------------------')
        print('---------------------------------------------------------------')
        print('---------------------------------------------------------------')
        print('---------------------------------------------------------------')
        
        # pdf_convertor.generate_pdf(json_data=summary, output_filepath=summarized_pdf_path)
        # # clean up
        # os.remove(file_path)
        # os.remove(output_json_path)
        # os.remove(parsed_pdf_path)
        # document_name = ' '.join(word.capitalize() for word in uploaded_filename.split('.')[0].split('_'))

        return {
            "summary": {
                # "raw": summary,
                        # "pdf": 'http://localhost:8000/engineering_reports/'+uploaded_filename,
                        # "document_name": document_name,
                        "summarized_at": datetime.now().strftime("%Y/%m/%d")},
            "status": "uploaded",
        }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
