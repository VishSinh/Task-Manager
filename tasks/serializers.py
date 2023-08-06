from rest_framework import serializers

from .models import Tasks

class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'due_date']

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'due_date']
