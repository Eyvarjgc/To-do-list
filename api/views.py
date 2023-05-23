from rest_framework import viewsets,permissions
from app import models
from . import serializers

class TaskViewset(viewsets.ModelViewSet):
    queryset = models.task.objects.all()
    serializer_class = serializers.TaskSerializers
    permission_classes = [permissions.AllowAny]