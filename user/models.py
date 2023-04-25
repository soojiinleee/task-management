from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, verbose_name="직원 이름")
    password = models.CharField(max_length=250, verbose_name="비밀번호")
    team = models.ForeignKey(
        "Team",
        on_delete=models.SET_NULL,
        related_name="team",
        blank=True,
        null=True,
        verbose_name="소속팀",
    )
    first_name = None
    last_name = None

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="팀 이름")

    def __str__(self):
        return self.name
