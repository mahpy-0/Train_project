from rest_framework import serializers

from trains.serializers import TrainSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    trains = TrainSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = "__all__"