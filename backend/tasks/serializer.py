"""Rest API serializers for tasks app."""


from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""
    class Meta:
        """Meta class for serializer."""
        model = Task
        # fields = ("id", "title", "description", "done")
        fields = "__all__"
        read_only_fields = ("id",)
