# Generated by Django 4.2 on 2023-04-25 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일시"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="변경일시"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="삭제여부"
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, default=None, null=True, verbose_name="삭제일시"
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="업무")),
                ("content", models.TextField(max_length=1000, verbose_name="내용")),
                (
                    "is_completed",
                    models.BooleanField(default=False, verbose_name="완료여부"),
                ),
                (
                    "completed_date",
                    models.DateTimeField(auto_now=True, verbose_name="완료일시"),
                ),
                (
                    "create_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="create_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="생성한 사람",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_team",
                        to="user.team",
                        verbose_name="생성한 팀",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="SubTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일시"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="변경일시"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="삭제여부"
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, default=None, null=True, verbose_name="삭제일시"
                    ),
                ),
                (
                    "is_completed",
                    models.BooleanField(default=False, verbose_name="완료여부"),
                ),
                (
                    "completed_date",
                    models.DateTimeField(auto_now=True, verbose_name="완료일시"),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subtasks",
                        to="task.task",
                        verbose_name="메인 업무",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subtask_team",
                        to="user.team",
                        verbose_name="협업 팀",
                    ),
                ),
            ],
            options={
                "ordering": ["team"],
            },
        ),
    ]
