from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer, ProjectSerializer, UserProjectTaskSerializer
from .services import TaskService, ProjectService, ProjectTaskService


class TaskAPIView(GenericAPIView):
    serializer_class = TaskSerializer       
    
    def get(self, request: Request) -> Response:
        """ Getting all tasks """
        response = TaskService.get_all_tasks()
        return Response(data=response.data)
    

    def get(self, request: Request, pk: int) -> Response:
        """ Getting task by id  """
        response = TaskService.get_task_by_id(pk)
        return Response(data=response.data)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Adding new task """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting task by id  """
        TaskService.delete_task_by_id(pk)
        return Response(status=status.HTTP_201_CREATED)


class ProjectAPIView(GenericAPIView):
    serializer_class = ProjectSerializer
    
    def get(self, request: Request) -> Response:
        """ Getting all projects """
        response = ProjectService.get_all_tasks()
        return Response(data=response.data)

    def get(self, request: Request, pk: int) -> Response:
        """ Getting project by id  """
        response = TaskService.get_task_by_id(pk)
        return Response(data=response.data)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Adding new project """
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int) -> Response:
        """ Deleting project by id """
        ProjectService.delete_project_by_id(pk)
        return Response(status=status.HTTP_200_OK)
