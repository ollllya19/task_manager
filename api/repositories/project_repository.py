from api.models import Task, Project
import datetime

class ProjectRepository:
    """ Class containing CRUD operations with Task model
    """
    @staticmethod
    def get_project_by_name(project: str) :
        project = Project.objects.filter(title=project).first()  # type: ignore
        return project

    @staticmethod
    def get_project_tasks(project: str) :
        task = Task.objects.filter(deadline=datetime.date.today())
        return task