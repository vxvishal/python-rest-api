from auth.data.abstract_repository import AbstractRepository
from auth.data.db_repository import DBRepository
from auth.domain.domain_models import CreateAuthUserRequest, UserDomainModel


class CreateAuthUserUseCase:
    def __init__(self, db_repository: AbstractRepository | None = None):
        self.db_repository = db_repository or DBRepository()

    def execute(self, request: CreateAuthUserRequest) -> UserDomainModel:
        return self.db_repository.create(
            user=UserDomainModel(
                id=1,
                first_name=request.first_name,
                last_name=request.last_name,
                email=request.email,
                password=request.password,
            )
        )
