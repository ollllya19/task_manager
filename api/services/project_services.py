from rest_framework.request import Request
from api.models import Project
from ..serializers.task_serializers import TaskSerializer
from ..serializers.project_serializers import ProjectSerializer, ProjectTasksSerializer
from ..repositories.project_repository import ProjectRepository


class ProjectService:
    """ Class containing CRUD operations with Project model
    """
    @staticmethod
    def get_project_by_id(id: int) -> ProjectSerializer:
        project = Project.objects.filter(id=id).first()
        response = ProjectSerializer(project)   
        return response
    
    @staticmethod
    def create_project(request: Request) -> bool:
        serializer = ProjectSerializer(data=request.data)  # type: ignore
        if serializer.is_valid():
            serializer.save()
            print(f'Project was created') 
            return True
        print(f'Error in creating')
        return False
    
    # to fixoijm
    @staticmethod
    def update_project_by_id(id: int) -> None:
        Project.objects.filter(id=id).first()
        print(f'Project {id} was updated')

    @staticmethod
    def delete_project_by_id(id: int) -> None:
        Project.objects.filter(id=id).delete()
        print(f'Project {id} was deleted')


class ProejctTasksService:
    
    @staticmethod
    def get_project_tasks(project: str, user) -> ProjectTasksSerializer:
        project_tasks = ProjectRepository.get_project_tasks(project, user)
        response = ProjectTasksSerializer(project_tasks, many=True)   
        print(f'Getting {project} project tasks and users') 
        return response

    @staticmethod
    def get_all_projects(user) -> ProjectSerializer:
        projects = ProjectRepository.get_all_project(user)
        response = ProjectSerializer(projects, many=True)   
        print(f'Getting all projects') 
        return response

