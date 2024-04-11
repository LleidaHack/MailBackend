from datetime import date
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, Date
from src.utils.database import Base
# from generated_src.lleida_hack_api_client.models.user_get_all import UserGetAll
from string import Template as TemplateUtil
from sqlalchemy import orm

class Template(Base):
    __tablename__ = 'template'
    id: int = Column(Integer, primary_key=True, index=True)
    creator_id: int = Column(Integer, nullable=False)
    name: str = Column(String, nullable=False)
    description: str = Column(String)
    html: str = Column(String, nullable=False)
    created_date = Column(Date)
    is_active = Column(Boolean, default=True)
    # __template: TemplateUtil

    @orm.reconstructor
    def init_on_load(self):
        self.__template = TemplateUtil(self.html)
        
    @property
    def fields(self) -> List[str]:
        return self.__template.get_identifiers()

    def add_base_values():
        pass
    
    def to_html(self, values: list[str]) -> str:
        if not len(self.fields) == len(values):
            raise Exception()
        data = dict(zip(self.fields, values))
        return self.__template.substitute(data)
