from core.base_models import BaseModelV1


class UserDomainModel(BaseModelV1):
    first_name: str
    last_name: str
    email: str
    password: str
