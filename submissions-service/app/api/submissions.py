import json
import logging
from typing import List

from fastapi import HTTPException
from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..db_config.config import get_db
from ..models.submission_models import *
from ..repository.submissions import SubmissionsRepository

logger = logging.getLogger(__name__)

router = APIRouter()

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
    
