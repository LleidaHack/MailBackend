from ast import List
from typing import Any

from generated_src.lleida_hack_api_client.api.user import get_user, get_users
from generated_src.lleida_hack_api_client.models.user_get import UserGet
from generated_src.lleida_hack_api_client.models.user_get_all import UserGetAll
from generated_src.lleida_hack_api_client.types import Response

from src.configuration.Settings import settings
from src.utils.Base.BaseClient import BaseClient


class UserClient(BaseClient):
    name = 'user_client'

    def __init__(self,
                 url=settings.client.url,
                 token=settings.client.service_token) -> None:
        # super().__init__(url, token)
        pass

    def get_all(self) -> List:
        with self.client as client:
            data: List[UserGet] = get_users.sync(client=client)
            return data

    def get_by_id(self, id: int) -> List:
        with self.client as client:
            data: UserGetAll = get_user.sync(id, client=client)
            if data is None:
                raise Exception()
            return data
