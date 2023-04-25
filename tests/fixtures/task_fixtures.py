import pytest
from faker import Faker
from task.models import Task, SubTask

fake = Faker()


@pytest.fixture
def danbi_task(db, danbi_member, get_teams):
    task = Task.objects.create(
        create_user=danbi_member,
        team=danbi_member.team,
        title=fake.sentence(),
        content=fake.text(),
    )
    subtask1 = SubTask.objects.create(task=task, team=get_teams[0])
    subtask2 = SubTask.objects.create(task=task, team=get_teams[1])
    return task


@pytest.fixture
def completed_danbi_task(db, danbi_member, get_teams):
    task = Task.objects.create(
        create_user=danbi_member,
        team=danbi_member.team,
        title=fake.sentence(),
        content=fake.text(),
        is_completed=True,
    )
    subtask1 = SubTask.objects.create(task=task, team=get_teams[0], is_completed=True)
    subtask2 = SubTask.objects.create(task=task, team=get_teams[1], is_completed=True)
    return task


@pytest.fixture
def darae_task(db, darae_member, get_teams):
    task = Task.objects.create(
        create_user=darae_member,
        team=darae_member.team,
        title=fake.sentence(),
        content=fake.text(),
    )
    subtask1 = SubTask.objects.create(task=task, team=get_teams[1])

    return task
