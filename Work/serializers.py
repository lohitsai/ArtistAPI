from rest_framework import serializers
from Work.models import WorkModel


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkModel
        fields = ["link", "workType"]
