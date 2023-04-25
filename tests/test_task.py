from django.urls import reverse
from rest_framework import status


class TestTaskViewSet:
    def test_success_get_task_list(
        self, api_client, danbi_member, danbi_task, darae_task
    ):
        url = reverse("task-list")
        api_client.force_authenticate(user=danbi_member)

        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_get_empty_task_list_no_tasks_on_user_team(
        self, api_client, blabla_member, danbi_task, darae_task
    ):
        url = reverse("task-list")
        api_client.force_authenticate(user=blabla_member)

        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    def test_get_task_detail(self, api_client, danbi_member, danbi_task):
        url = reverse("task-detail", args=[danbi_task.id])
        api_client.force_authenticate(user=danbi_member)

        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["subtasks"]) == 2

    def test_success_update_task_with_creator(
        self, api_client, danbi_member, danbi_task
    ):
        url = reverse("task-detail", args=[danbi_task.id])
        api_client.force_authenticate(user=danbi_member)

        data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "subtask_team_ids": [1, 2],
        }
        response = api_client.patch(url, data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_failure_update_task_with_no_creator(
        self, api_client, darae_member, danbi_task
    ):
        url = reverse("task-detail", args=[danbi_task.id])
        api_client.force_authenticate(user=darae_member)

        data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "subtask_team_ids": [1, 2],
        }
        response = api_client.patch(url, data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_success_update_task_and_subtask(
        self, api_client, danbi_member, danbi_task
    ):
        url = reverse("task-detail", args=[danbi_task.id])
        api_client.force_authenticate(user=danbi_member)

        data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "subtask_team_ids": [],
        }
        response = api_client.patch(url, data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_success_delete_task(self, api_client, danbi_member, danbi_task):
        url = reverse("task-detail", args=[danbi_task.id])
        api_client.force_authenticate(user=danbi_member)

        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_failure_delete_with_completed_task(
        self, api_client, danbi_member, completed_danbi_task
    ):
        url = reverse("task-detail", args=[completed_danbi_task.id])
        api_client.force_authenticate(user=danbi_member)

        response = api_client.delete(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_success_create_task(self, api_client, blabla_member, danbi_task):
        url = reverse("task-list")
        api_client.force_authenticate(user=blabla_member)
        data = {
            "title": "New Task",
            "content": "New Content",
            "subtask_team_ids": [1, 2],
        }

        response = api_client.post(url, data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "New Task"

    def test_failure_create_task_wrong_team_id(
        self, api_client, blabla_member, danbi_task
    ):
        url = reverse("task-list")
        api_client.force_authenticate(user=blabla_member)
        data = {"title": "New Task", "content": "New Content", "subtask_team_ids": [9]}

        response = api_client.post(url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestSubTaskViewSet:
    def test_success_update_subtask_status(self, api_client, danbi_member, danbi_task):
        danbi_subtask = danbi_task.subtasks.all().first()

        url = reverse("subtask-detail", args=[danbi_subtask.id])
        api_client.force_authenticate(user=danbi_member)

        data = {"is_completed": True}
        response = api_client.patch(url, data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_failure_update_subtask_status_with_not_member(
        self, api_client, danbi_member, danbi_task
    ):
        darae_subtask = danbi_task.subtasks.last()

        url = reverse("subtask-detail", args=[darae_subtask.id])
        api_client.force_authenticate(user=danbi_member)

        data = {"is_completed": True}
        response = api_client.patch(url, data=data)

        assert response.status_code == status.HTTP_403_FORBIDDEN
