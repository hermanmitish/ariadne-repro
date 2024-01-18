from os import getenv
import json
import os
from generated.client import Client
from generated import (
    NullableStringFieldUpdateOperationsInput,
)
from generated.input_types import UserUpdateInput


def run():
    client = Client("http://localhost/graphql")
    client.update_user(
        id="1",
        data=UserUpdateInput(name=NullableStringFieldUpdateOperationsInput(set="test")),
    )


if __name__ == "__main__":
    print("Starting test client", flush=True)
    run()
