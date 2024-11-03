from datetime import date
# from generated_src.lleida_hack_api_client.models.user_get_all import UserGetAll
from string import Template as TemplateUtil
from typing import List

from sqlalchemy import Boolean, Column, Date, Integer, String, func, orm

from src.utils.Base.BaseModel import BaseModel
from src.utils.CommonFields import CommonFields


class Template(BaseModel):
    __tablename__ = 'template'
    id: int = Column(Integer, primary_key=True, index=True)
    creator_id: int = Column(Integer, nullable=False)
    name: str = Column(String, nullable=False)
    description: str = Column(String)
    html: str = Column(String, nullable=False)
    created_date = Column(Date, default=func.current_date())
    is_active = Column(Boolean, default=True)
    internal = Column(Boolean, default=False)

    @orm.reconstructor
    def init_on_load(self):
        self.__template = TemplateUtil(self.html)

    @property
    def fields(self):
        return [_ for _ in self.__template.get_identifiers() if _[0] != '_']

    @property
    def common_fields(self) -> List[str]:
        return [_ for _ in self.__template.get_identifiers() if _[0] == '_']

    @property
    def common_values(self):
        return {
            _.name: _.value
            for _ in CommonFields if _.name in self.common_fields
        }

    def to_html(self, values: List[str]) -> str:
        values[len(self.fields) -
               1:] = [','.join(values[len(self.fields) - 1:])]
        if not len(self.fields) == len(values):
            raise Exception(f'fields:{self.fields}  \n  values:{values}')
        data = dict(zip(self.fields, values))
        data.update(self.common_values)
        return self.__template.substitute(data)
