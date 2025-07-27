from django.test import SimpleTestCase, testcases


class BaseDBTestCase(testcases.TestCase):
    """
    Base test class from which all database-related test cases should inherit.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    def tearDown(self) -> None:
        super().tearDown()


class BaseUseCaseTestCase(SimpleTestCase):
    """
    Base use case test class from which all use case test cases should inherit.
    This class will not allow database calls.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    def tearDown(self) -> None:
        super().tearDown()
