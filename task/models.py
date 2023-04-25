from django.conf import settings
from django.db import models

from common.models import DefaultTimeStampModel, SoftDeleteManager, SoftDeleteModel
from user.models import Team

User = settings.AUTH_USER_MODEL


class Task(DefaultTimeStampModel, SoftDeleteModel):
    create_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="create_user",
        verbose_name="생성한 사람",
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="task_team", verbose_name="생성한 팀"
    )
    title = models.CharField(max_length=250, verbose_name="업무")
    content = models.TextField(max_length=1000, verbose_name="내용")
    is_completed = models.BooleanField(default=False, verbose_name="완료여부")
    completed_date = models.DateTimeField(auto_now=True, verbose_name="완료일시")

    objects = SoftDeleteManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class SubTask(DefaultTimeStampModel, SoftDeleteModel):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="subtasks", verbose_name="메인 업무"
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="subtask_team", verbose_name="협업 팀"
    )
    is_completed = models.BooleanField(default=False, verbose_name="완료여부")
    completed_date = models.DateTimeField(auto_now=True, verbose_name="완료일시")

    objects = SoftDeleteManager()

    class Meta:
        ordering = ["team"]

    def __str__(self):
        return f"subtask_{self.team}"
