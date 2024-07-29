from sqlalchemy.orm import Session
from ..models.submission_models import *

class SubmissionsRepository: 
    def __init__(self, sess:Session):
        self.sess:Session = sess
        
    def get_all_submissions(self):
        return self.sess.query(Submission).all() 
    
    def get_submission(self, submission_id: int):
        return self.sess.query(Submission).filter(Submission.id == submission_id).all()
    
    def insert_submission(self, sub: Submission) -> bool: 
        try:
            self.sess.add(sub)
            self.sess.commit()
        except: 
            return False 
        return True