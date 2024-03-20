from generated_src.lleida_hack_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="http://localhost:8000", token="HOL")

from generated_src.lleida_hack_api_client.models import user_get_all
from generated_src.lleida_hack_api_client.api.user import get_users
from generated_src.lleida_hack_api_client.types import Response

with client as client:
    my_data: user_get_all = get_users.sync_detailed(client=client)
    print(my_data)