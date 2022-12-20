import datetime
from api.models import Task, Project, User_Project_Task

from django.contrib.auth import get_user_model
User = get_user_model()

class ProjectRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_project_by_name(project_name: str, user) :
        project = Project.objects.filter(title=project_name, user=user).first()  # type: ignore
        return project

    @staticmethod
    def get_project_tasks(project_name: str, user) :
        project = ProjectRepository.get_project_by_name(project_name, user)
        project_tasks = User_Project_Task.objects.filter(project=project)
        return project_tasks

    @staticmethod
    def get_all_project(user) :
        projects = Project.objects.filter(user=user)
        return projects

    @staticmethod
    def create_task(title, desc, status, user, todo_date):
        date = None
        if todo_date != "":
            date = datetime.datetime.strptime(todo_date, "%d.%m.%Y").date() # type: ignore  
        print(date)
        try:
            task = Task(
                title=title,              
                description=desc,              
                status=status,        
                user=user,
                todo_date=date   
            )
            task.save()
            return task
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def create_task_project_record(creator, user, task, project_name):
        try:
            project = None
            if project_name != "":
                project = ProjectRepository.get_project_by_name(project_name, creator)
            record = User_Project_Task(
                user=user,              
                task=task,                      
                project=project
            )
            record.save()
            return True
        except:
            return False


class UserRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_user_by_name(user_name: str) :
        user = User.objects.filter(username=user_name).first()  # type: ignore
        return user
