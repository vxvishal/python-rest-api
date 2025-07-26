import abc

from auth.domain.domain_models import UserDomainModel


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, user: UserDomainModel) -> UserDomainModel:
        """
        This method will create a new user.
        """
        pass
