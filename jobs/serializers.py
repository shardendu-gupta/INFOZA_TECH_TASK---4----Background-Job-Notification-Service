from rest_framework import serializers
from .models import Jobs


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"
        read_only_fields = ["id", "status", "attempts", "max_retries", "error_message", "created_at", "updated_at", "completed_at"]


