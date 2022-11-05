from api.models import Task
import datetime

class TaskRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_today_tasks() :
        task = Task.objects.filter(deadline=datetime.date.today())
        return task

    @staticmethod
    def get_incoming_tasks() :
        task = Task.objects.filter(deadline=None)
        return task
    
    @staticmethod
    def get_upcoming_tasks() :
        task = Task.objects.filter(deadline__gt=datetime.date.today())
        return task