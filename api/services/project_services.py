from rest_framework.request import Request
from api.models import Project
from ..serializers import ProjectSerializer


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
    
    # to fix
    @staticmethod
    def update_project_by_id(id: int) -> None:
        Project.objects.filter(id=id).first()
        print(f'Project {id} was updated')

    @staticmethod
    def delete_project_by_id(id: int) -> None:
        Project.objects.filter(id=id).delete()
        print(f'Project {id} was deleted')