from rest_framework.request import Request
from api.models import Task
from ..serializers.task_serializers import TaskSerializer, GetTasksSerializer
from ..repositories.task_repository import TaskRepository


class TaskService:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_task_by_id(id: int) -> TaskSerializer:
        task = Task.objects.filter(id=id).first()
        response = TaskSerializer(task)   
        print(f'Getting task {id}') 
        return response
    
    @staticmethod
    def create_task(request: Request) -> bool:
        serializer = TaskSerializer(data=request.data)  # type: ignore
        if serializer.is_valid():
            serializer.save()
            print(f'Task was created') 
            return True
        print(f'Error in creating')
        return False
    
    # fix me (make with the help of serializator)
    @staticmethod
    def update_task_by_id(id: int, _title: str, _description: str) -> None:
        Task.objects.filter(id=id).update(title=_title, description=_description)
        print(f'Task {id} was updated')

    @staticmethod
    def delete_task_by_id(id: int) -> None:
        Task.objects.filter(id=id).delete()
        print(f'Task {id} was deleted')


class FilterdTasksService:
    
    @staticmethod
    def get_incoming_tasks(user) -> GetTasksSerializer:
        tasks = TaskRepository.get_incoming_tasks(user)
        response = GetTasksSerializer(tasks, many=True)   
        print(f'Getting incoming tasks') 
        return response
    
    @staticmethod
    def get_today_tasks(user) -> GetTasksSerializer:
        tasks = TaskRepository.get_today_tasks(user)
        response = GetTasksSerializer(tasks, many=True)   
        print(f'Getting today tasks') 
        return response
    
    @staticmethod
    def get_upcoming_tasks(user) -> TaskSerializer:
        tasks = TaskRepository.get_upcoming_tasks(user)
        response = TaskSerializer(tasks, many=True)   
        print(f'Getting upcoming tasks') 
        return response
