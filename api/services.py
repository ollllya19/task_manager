
from api.models import UserProfile, Project, Task, User_Project_Task


class ProjectService:
    
    @staticmethod
    def create_project(**args) -> None:
        project = Project.objects.create()
        project.save()

    @staticmethod
    def update_project_by_id(id) -> None:
        project = Project.objects.filter(id=id).first()

    @staticmethod
    def delete_project_by_id(id) -> None:
        project = Project.objects.filter(id=id).first().delete()


class TaskService:
        
    @staticmethod
    def create_task(**args) -> None:
        task = Task.objects.create()
        task.save()
    
    @staticmethod
    def update_task_by_id(id) -> None:
        task = Task.objects.filter(id=id).first()
