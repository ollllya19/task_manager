from api.models import Task
import datetime

class TaskRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_today_tasks(user) :
        task = Task.objects.filter(todo_date=datetime.date.today(), user=user)
        return task

    @staticmethod
    def get_incoming_tasks(user) :
        task = Task.objects.filter(todo_date=None, user=user)
        return task
    
    @staticmethod
    def get_upcoming_tasks(user) :
        task = Task.objects.filter(todo_date__gt=datetime.date.today(), user=user)
        return task