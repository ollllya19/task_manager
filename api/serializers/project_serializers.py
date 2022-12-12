from rest_framework import serializers
from ..models import Project, User_Project_Task


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Project
        fields = '__all__'


class ProjectTasksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_Project_Task
        
        fields = '__all__'
        depth = 1