import pytest

pytestmark = pytest.mark.django_db

pytest_plugins = [
    "tests.fixtures.api_client",
    "tests.fixtures.user_fixtures",
    "tests.fixtures.task_fixtures",
]
