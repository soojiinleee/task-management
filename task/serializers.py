from rest_framework import serializers

from user.serializers import UserSerializer, TeamSerializer
from user.models import Team
from .models import Task, SubTask


class SubTaskListSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = SubTask
        fields = [
            "id",
            "team",
            "is_completed",
            "completed_date",
            "created_at",
        ]


class SubTaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ["id", "is_completed"]

    def update(self, instance: SubTask, validated_data: dict):
        instance = super().update(instance, validated_data)

        related_subtasks = SubTask.objects.filter(
            task_id=instance.task.id, is_completed=False
        ).exists()

        if not related_subtasks:
            instance.task.is_completed = True
            instance.task.save()

        return instance


class TaskListSerializer(serializers.ModelSerializer):
    create_user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    subtasks = SubTaskListSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "create_user",
            "team",
            "title",
            "content",
            "is_completed",
            "completed_date",
            "created_at",
            "subtasks",
        ]


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskListSerializer(read_only=True, many=True)
    subtask_team_ids = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=True, write_only=True
    )

    class Meta:
        model = Task
        fields = ["id", "title", "content", "subtasks", "subtask_team_ids"]

    def validate_subtask_team_ids(self, value):
        if value:
            for team_id in value:
                if not Team.objects.filter(id=team_id).exists():
                    raise serializers.ValidationError("team_id를 확인해주세요")

        return value

    def create(self, validated_data: dict):
        create_user = self.context["request"].user
        team = create_user.team
        subtask_team_ids = validated_data.pop("subtask_team_ids", None)

        task = Task.objects.create(create_user=create_user, team=team, **validated_data)

        if subtask_team_ids:
            subtasks = [
                SubTask(task=task, team_id=team_id) for team_id in subtask_team_ids
            ]
            SubTask.objects.bulk_create(subtasks)

        return task

    def update(self, instance: Task, validated_data: dict):
        instance = super().update(instance, validated_data)

        updated_subtask_team = validated_data.get("subtask_team_ids", None)
        not_completed_subtasks = instance.subtasks.filter(
            is_completed=False
        ).values_list("team", flat=True)

        if updated_subtask_team is None:
            not_completed_subtasks.update(is_deleted=True)

        else:
            if set(not_completed_subtasks) != set(updated_subtask_team):
                not_completed_subtasks.update(is_deleted=True)
                new_subtasks = [
                    SubTask(task=instance, team_id=team_id)
                    for team_id in updated_subtask_team
                ]
                SubTask.objects.bulk_create(new_subtasks)

        return instance
