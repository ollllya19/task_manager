from pydoc import describe
from turtle import title
from api.models import UserProfile, Project, Task, User_Project_Task
from .serializers import TaskSerializer, ProjectSerializer


class ProjectService:
    """ Class containing CRUD operations with Project model
    """
    
    @staticmethod
    def create_project(_title: str, _creator: str) -> None:
        project = Project.objects.create(
            title=_title,
            creator=_creator
        )
        project.save()
        print(f'Project {id} was created')

    @staticmethod
    def get_project_by_id(id: int) -> ProjectSerializer:
        project = Project.objects.filter(id=id).first()
        response = ProjectSerializer(project)   
        return response
    
    @staticmethod
    def get_all_projects() -> ProjectSerializer:
        projects = Project.objects.all()
        response = ProjectSerializer(projects, many=True)   
        return response
    
    @staticmethod
    def update_project_by_id(id: int) -> None:
        Project.objects.filter(id=id).first()
        print(f'Project {id} was updated')

    @staticmethod
    def delete_project_by_id(id: int) -> None:
        project = Project.objects.filter(id=id).first()
        project.delete()
        print(f'Project {id} was deleted')


class TaskService:
    """ Class containing CRUD operations with Task model
    """
    
    @staticmethod
    def create_task(_title: str, _description: str, _is_done, _status) -> None:
        task = Task.objects.create(
            title=_title,
            description=_description,
            is_done=_is_done,
            status=_status,
        )
        task.save()
        print(f'Task {task.id} was created\n')  # type: ignore
    
    @staticmethod
    def get_all_tasks() -> TaskSerializer:
        tasks = Task.objects.all()
        response = TaskSerializer(tasks, many=True)   
        return response
    
    @staticmethod
    def get_task_by_id(id: int) -> Task:
        task = Task.objects.filter(id=id).first()
        # response = TaskSerializer(task)   
        return task  # type: ignore
    
    @staticmethod
    def update_task_by_id(id: int, _title: str, _description: str) -> None:
        Task.objects.filter(id=id).update(title=_title, description=_description)
        print(f'Task {id} was updated\n')

    @staticmethod
    def delete_task_by_id(id: int) -> None:
        Task.objects.filter(id=id).delete()
        print(f'Task {id} was deleted\n')
