from typing import List
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from pydantic import BaseModel

from ..db_config.config import Base

class FileSchema(BaseModel):
    filename: str
    content_type: str
    contents: bytes

class FormDataSchema(BaseModel):
    account_name: str
    domicile: str
    broker: str
    files: List[FileSchema]

class Submission(Base):
    __tablename__ = "submissions"
    __table_args__ = {"schema": "silas"}

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    underwriter = Column(String)
    domicile = Column(String)
    broker = Column(String)
    filenames = Column(String)