from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework .permissions import IsAuthenticated

from ..serializers.task_serializers import TaskSerializer, GetTasksSerializer
from ..services.task_services import TaskService, FilterdTasksService, CreateTaskService


class CreateTaskAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = TaskSerializer       
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Adding new task """
        if CreateTaskService.create_task(request):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, *args, **kwargs) -> Response:
        """ Updating new task """
        if CreateTaskService.update_task(request):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TaskAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
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

    def put(self, request: Request, pk: int, title: str, description: str, *args, **kwargs) -> Response:
        """ Adding new task """
        if TaskService.update_task_by_id(pk, title, description):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting task by id """
        TaskService.delete_task_by_id(pk)
        return Response(status=status.HTTP_200_OK)
        

# Tasks retrieving classes for sidebar 
class IncomingTasksAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetTasksSerializer  

    def get(self, request: Request) -> Response:
        """ Getting incoming tasks of user """
        print(request.user)
        response = FilterdTasksService.get_incoming_tasks(request.user)
        print(response.data)
        return Response(data=response.data, status=status.HTTP_200_OK)


class TodayTasksAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetTasksSerializer  
    
    def get(self, request: Request) -> Response:
        """ Getting today tasks of user """
        response = FilterdTasksService.get_today_tasks(request.user)
        print(response.data)
        return Response(data=response.data)


class UpcomingTasksAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetTasksSerializer  
    
    def get(self, request: Request) -> Response:
        """ Getting upcoming tasks of user """
        response = FilterdTasksService.get_upcoming_tasks(request.user)
        print(response.data)
        return Response(data=response.data, status=status.HTTP_200_OK)
