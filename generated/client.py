from typing import Any, Dict

from .base_client import BaseClient
from .input_types import UserUpdateInput
from .update_user import UpdateUser


def gql(q: str) -> str:
    return q


class Client(BaseClient):
    def update_user(self, id: str, data: UserUpdateInput, **kwargs: Any) -> UpdateUser:
        query = gql(
            """
            mutation UpdateUser($id: String!, $data: UserUpdateInput!) {
              updateOneUser(where: {id: $id}, data: $data) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "data": data}
        response = self.execute(
            query=query, operation_name="UpdateUser", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateUser.model_validate(data)
