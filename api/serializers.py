from app import models
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.task
        fields = '__all__'