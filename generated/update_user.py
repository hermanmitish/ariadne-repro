from typing import Optional

from .base_model import BaseModel


class UpdateUser(BaseModel):
    updateOneUser: Optional["UpdateUserUpdateOneUser"]


class UpdateUserUpdateOneUser(BaseModel):
    id: str
