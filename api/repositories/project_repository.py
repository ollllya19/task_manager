import datetime
from api.models import Task, Project, User_Project_Task

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
    def create_task(title, desc, status, user):
        try:
            task = Task(
                title=title,              
                description=desc,              
                status=status,        
                user=user,
                # todo_date=datetime.date()    # type: ignore    
            )
            task.save()
            return task
        except:
            return None

    @staticmethod
    def create_task_project_record(user, task, project_name):
        try:
            print('-------------')
            print(project_name)
            project = None
            if project_name != "":
                print('ищем проект')
                project = ProjectRepository.get_project_by_name(project_name, user)
            record = User_Project_Task(
                user=user,              
                task=task,                      
                project=project
            )
            record.save()
            return True
        except:
            return False


