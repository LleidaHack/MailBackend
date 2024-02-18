from datetime import date
from typing import List
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from database import Base

class Template(Base):
    __tablename__='template'
    id: int = Column(Integer, primary_key=True, index=True)
    creator_id: int = Column(Integer, nullable=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String)
    html: str = Column(String, nullable=False)
    fields: List[str] # calculated

    def get_output(values):
        pass