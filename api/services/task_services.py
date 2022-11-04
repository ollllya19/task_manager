from rest_framework.request import Request
from api.models import Task, User_Project_Task
from ..serializers import TaskSerializer, ProjectSerializer


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
    
    # to fix method
    @staticmethod
    def update_task_by_id(id: int, _title: str, _description: str) -> None:
        Task.objects.filter(id=id).update(title=_title, description=_description)
        print(f'Task {id} was updated')

    @staticmethod
    def delete_task_by_id(id: int) -> None:
        Task.objects.filter(id=id).delete()
        print(f'Task {id} was deleted')
