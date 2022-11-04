from asyncio import tasks
from turtle import title
from django.test import TestCase

from .models import Task
from .services.project_services import ProjectService
from .services.task_services import TaskService


class TestTaskService(TestCase):
    
    # def setUp(self):
    #     TaskService().create_task(
    #         _title='Заголовок',
    #         _description='Описание',
    #         _is_done=True,
    #         _status=1)
    #     TaskService().create_task(
    #         _title='Заголовок2',
    #         _description='Описание2',
    #         _is_done=True,
    #         _status=1)
        
    def test_get_task(self):
        """ Testing of getting task by id """
        task = Task.objects.get(id=1)
        self.assertIsNotNone(task)  

    def test_delete_task(self):
        """ Testing of deleting task by id """
        TaskService().delete_task_by_id(id=1)
        result = TaskService().get_task_by_id(id=1)  
        self.assertIsNone(result) 
    
    def test_update_task(self):
        """ Testing if updating task by id """
        TaskService().update_task_by_id(2, 'новый заголовок', 'новое описание')
        task = Task.objects.get(id=2)
        self.assertTrue(task.title == 'новый заголовок')  
        self.assertTrue(task.description == 'новое описание') 
