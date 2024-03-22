from ast import List
from typing import Any
from src.utils.Base.BaseClient import BaseClient
from generated_src.lleida_hack_api_client import AuthenticatedClient

from generated_src.lleida_hack_api_client.models import user_get_all
from generated_src.lleida_hack_api_client.api.user import get_users, get_user
from generated_src.lleida_hack_api_client.types import Response


class UserClient(BaseClient):
    name = 'user_client'

    def __init__(self, url='', token='HOLA') -> Any:
        super().__init__(url, token)

    def get_all(self) -> List:
        with self.client as client:
            data: user_get_all = get_users.sync_detailed(client=client)
            return data

    def get_by_id(self, id: int) -> List:
        with self.client as client:
            data: user_get_all = get_user.sync_detailed(id, client=client)
            return data