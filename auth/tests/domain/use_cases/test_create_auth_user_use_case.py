from unittest.mock import Mock

from auth.data.db_repository import DBRepository
from auth.domain.domain_models import CreateAuthUserRequest, UserDomainModel
from auth.domain.use_cases.create_auth_user_use_case import CreateAuthUserUseCase
from core.testing import BaseUseCaseTestCase


class TestCreateAuthUserUseCase(BaseUseCaseTestCase):
    def setUp(self):
        super().setUp()
        self.mocked_db_repository = Mock(DBRepository)
        self.create_auth_user_use_case = CreateAuthUserUseCase(
            db_repository=self.mocked_db_repository
        )

    def tearDown(self):
        super().tearDown()

    def test_execute(self):
        """
        Case: call execute with a valid request.
        Expected: the create DB method is called.
        """
        request = CreateAuthUserRequest(
            first_name="Test",
            last_name="User",
            email="test@email.com",
            password="securepassword",
        )

        # Call the use case
        user = self.create_auth_user_use_case.execute(request=request)

        # Assert
        self.mocked_db_repository.create.assert_called_once_with(
            user=UserDomainModel(
                id=1,
                first_name=request.first_name,
                last_name=request.last_name,
                email=request.email,
                password=request.password,
            )
        )
