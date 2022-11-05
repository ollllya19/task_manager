from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer, ProjectSerializer
from .services.task_services import TaskService, FilterdTasksService
from .services.project_services import ProjectService


class TaskAPIView(GenericAPIView):
    serializer_class = TaskSerializer       
    
    def get(self, request: Request, pk: int) -> Response:
        """ Getting task by id """
        response = TaskService.get_task_by_id(pk)
        return Response(data=response.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """ Adding new task """
        if TaskService.create_task(request):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting task by id """
        TaskService.delete_task_by_id(pk)
        return Response(status=status.HTTP_200_OK)



class ProjectAPIView(GenericAPIView):
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


class IncomingTasksAPIView(RetrieveAPIView):

    def get(self, request: Request):
        response = FilterdTasksService.get_incoming_tasks()
        return Response(data=response.data, status=status.HTTP_200_OK)

class TodayTasksAPIView(RetrieveAPIView):
    
    def get(self, request: Request):
        response = FilterdTasksService.get_today_tasks()
        return Response(data=response.data, status=status.HTTP_200_OK)

class UpcomingTasksAPIView(RetrieveAPIView):
    
    def get(self, request: Request):
        response = FilterdTasksService.get_upcoming_tasks()
        return Response(data=response.data, status=status.HTTP_200_OK)