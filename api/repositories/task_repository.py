from api.models import Task, User_Project_Task
import datetime

class TaskRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_today_tasks(user) :
        tasks = User_Project_Task.objects.filter(user=user, task__todo_date=datetime.date.today())
        return tasks

    @staticmethod
    def get_incoming_tasks(user) :
        tasks = User_Project_Task.objects.filter(user=user, task__todo_date=None)
        return tasks
    
    @staticmethod
    def get_upcoming_tasks(user) :
        tasks = User_Project_Task.objects.filter(user=user, task__todo_date__gt=datetime.date.today())
        # task = Task.objects.filter(todo_date__gt=datetime.date.today(), user=user)
        return tasks
