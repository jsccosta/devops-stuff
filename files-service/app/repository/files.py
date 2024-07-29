from sqlalchemy.orm import Session
from ..models.submission_models import *

from ..db_config.config import Base


class Tenants(Base):
    __tablename__ = "tenants"
    __table_args__ = {"schema": "silas"}
    id = Column(Integer, primary_key=True)
    tenant = Column(String)
    bucket = Column(String)

class FilesRepository: 
    def __init__(self, sess:Session):
        self.sess:Session = sess
        
    def get_tenant(self):
        return self.sess.query(Tenants).all() 
    
    # def get_submission(self, submission_id: int):
    #     return self.sess.query(Submission).filter(Submission.id == submission_id).all()
    
    # def insert_submission(self, sub: Submission) -> bool: 
    #     try:
    #         self.sess.add(sub)
    #         self.sess.commit()
    #     except: 
    #         return False 
    #     return True