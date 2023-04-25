from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from common.permissions import IsCreatorOrReadOnly, IsTeamMemberOrReadOnly
from .serializers import (
    TaskListSerializer,
    TaskSerializer,
    SubTaskStatusSerializer,
)
from .models import Task, SubTask


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(
            Q(team=user.team) | Q(subtasks__team=user.team)
        ).distinct()
        return tasks

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TaskListSerializer
        if self.action in ("create", "update", "partial_update", "destroy"):
            return TaskSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        is_completed = instance.is_completed

        if is_completed:
            return Response(
                {"error": "완료된 업무는 삭제 할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubTaskViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = SubTaskStatusSerializer
    permission_classes = (IsTeamMemberOrReadOnly,)

    def get_queryset(self):
        queryset = SubTask.objects.all()
        return queryset
