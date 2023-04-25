from rest_framework import serializers
from .models import User, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "team"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name"]
