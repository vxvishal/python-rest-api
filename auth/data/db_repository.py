from auth.data.abstract_repository import AbstractRepository
from auth.domain.domain_models import UserDomainModel
from core.models import User


class DBRepository(AbstractRepository):
    def create(self, user: UserDomainModel) -> UserDomainModel:
        created_user = User.objects.create_user(
            username=user.email,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        return UserDomainModel.from_orm(created_user)
