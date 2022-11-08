from rest_framework import serializers
from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Task
        fields = '__all__'


class GetTasksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        exclude = ['user', 'created_at']
