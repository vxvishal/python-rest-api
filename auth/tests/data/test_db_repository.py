from auth.data.abstract_repository import AbstractRepository
from auth.data.db_repository import DBRepository
from auth.domain.domain_models import UserDomainModel
from core.models import User
from core.testing import BaseDBTestCase


class TestDBRepository(BaseDBTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_repository: AbstractRepository = DBRepository()

    def tearDown(self) -> None:
        super().tearDown()

    def test_create_user(self):
        """
        Case: call create method of DBRepository with a UserDomainModel instance.
        Expected: a user is created in the database.
        """
        user = UserDomainModel(
            id=1,
            email="test@email.com",
            password="securepassword",
            first_name="Test",
            last_name="User",
        )

        # Call the method
        created_user = self.db_repository.create(user=user)

        # Assertions
        db_user = User.objects.get(id=created_user.id)
        self.assertIsNotNone(db_user)
