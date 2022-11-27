from api.models import Task, Project

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
        tasks = Task.objects.filter(project=project)
        return tasks

    @staticmethod
    def get_all_project(user) :
        projects = Project.objects.filter(user=user)
        return projects