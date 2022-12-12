from rest_framework.request import Request
from api.models import Task, User_Project_Task
from ..serializers.task_serializers import TaskSerializer, GetTasksSerializer
from ..repositories.task_repository import TaskRepository
from ..repositories.project_repository import ProjectRepository
from ..serializers.project_serializers import ProjectTasksSerializer


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
    def get_incoming_tasks(user) -> ProjectTasksSerializer:
        tasks = TaskRepository.get_incoming_tasks(user)
        response = ProjectTasksSerializer(tasks, many=True)   
        print(f'Getting incoming tasks') 
        return response
    
    @staticmethod
    def get_today_tasks(user) -> ProjectTasksSerializer:
        tasks = TaskRepository.get_today_tasks(user)
        response = ProjectTasksSerializer(tasks, many=True)   
        print(f'Getting today tasks') 
        return response
    
    @staticmethod
    def get_upcoming_tasks(user) -> ProjectTasksSerializer:
        tasks = TaskRepository.get_upcoming_tasks(user)
        response = ProjectTasksSerializer(tasks, many=True)   
        print(f'Getting upcoming tasks') 
        return response


class CreateTaskService:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def create_task(request: Request) -> bool:

        # tring to create task object
        task = ProjectRepository.create_task(
                title=request.data['title'],           # type: ignore      
                desc=request.data['desc'],     # type: ignore          
                status=request.data['status'],          # type: ignore  
                user=request.user)
        if task is None:
            print('task error')
            print(f'Error in creating')
            return False

        #  tring to create task-project connection
        print(request.data)
        print(request.data['project'])             # type: ignore  
        task_record = ProjectRepository.create_task_project_record(
            user=request.user,
            task=task,
            project_name=request.data['project']             # type: ignore  
        )
        if task_record:
            print(f'Task was created') 
            return True
        print('record error')
        print(f'Error in creating')
        return False
