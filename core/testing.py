from django.test import testcases


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
