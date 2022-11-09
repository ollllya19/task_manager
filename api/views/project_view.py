from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework .permissions import IsAuthenticated

from ..serializers.project_serializers import ProjectSerializer
from ..serializers.task_serializers import TaskSerializer
from ..services.project_services import ProjectService, ProejctTasksService


class ProjectAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get(self, request: Request, pk: int) -> Response:
        """ Getting project by id """
        response = ProjectService.get_project_by_id(pk)
        return Response(data=response.data, status=status.HTTP_200_OK)

    def post(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """ Adding new project """
        if ProjectService.create_project(request):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting project by id """
        ProjectService.delete_project_by_id(pk)
        return Response(status=status.HTTP_200_OK)


class ProejctTasksAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get(self, request: Request, project_name: str) :
        """ Getting all tasks of the project """
        response = ProejctTasksService.get_project_tasks(project_name, request.user)
        return Response(data=response.data, status=status.HTTP_200_OK)