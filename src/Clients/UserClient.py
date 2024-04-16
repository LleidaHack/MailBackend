from ast import List
from typing import Any
from configuration.Configuration import Configuration
from generated_src.lleida_hack_api_client.api.user import get_user, get_users
from generated_src.lleida_hack_api_client.models.user_get import UserGet
from src.utils.Base.BaseClient import BaseClient

from generated_src.lleida_hack_api_client.models.user_get_all import UserGetAll
from generated_src.lleida_hack_api_client.types import Response


class UserClient(BaseClient):
    name = 'user_client'

    def __init__(self, url=Configuration.client.url, token=Configuration.client.service_token) -> Any:
        super().__init__(url, token)

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
