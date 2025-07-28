from pydantic import PositiveInt

from core.base_models import BaseModelV1


class UserDomainModel(BaseModelV1):
    id: PositiveInt
    first_name: str
    last_name: str
    email: str
    password: str


class CreateAuthUserRequest(BaseModelV1):
    first_name: str
    last_name: str
    email: str
    password: str
