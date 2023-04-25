import pytest
from faker import Faker
from user.models import User, Team

fake = Faker()


@pytest.fixture
def get_teams(db):
    team_list = ["단비", "다래", "블라블라"]
    team_data = [Team(name=name) for name in team_list]
    teams = Team.objects.bulk_create(team_data)

    return teams


@pytest.fixture
def create_new_user_factory(db):
    def create_user(username: str, team_id: int = None):
        user = User.objects.create_user(username=username, team_id=team_id)
        return user

    return create_user


@pytest.fixture
def danbi_member(db, create_new_user_factory):
    danbi_member = create_new_user_factory(username=fake.name(), team_id=1)

    return danbi_member


@pytest.fixture
def darae_member(db, create_new_user_factory):
    darae_member = create_new_user_factory(username=fake.name(), team_id=2)

    return darae_member


@pytest.fixture
def blabla_member(db, create_new_user_factory):
    blabla_member = create_new_user_factory(username=fake.name(), team_id=3)

    return blabla_member
