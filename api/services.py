
from api.models import UserProfile, Project, Task, User_Project_Task


class ProjectService:
    """ Class containing CRUD operations with Project model
    """
    
    @staticmethod
    def create_project(_title, _creator) -> None:
        project = Project.objects.create(
            title=_title,
            creator=_creator
        )
        project.save()
        print(f'Project {id} was saved')

    @staticmethod
    def get_project_by_id(id) -> None:
        project = Project.objects.filter(id=id).first()
        return project
    
    @staticmethod
    def update_project_by_id(id) -> None:
        Project.objects.filter(id=id).first()
        print(f'Project {id} was updated')

    @staticmethod
    def delete_project_by_id(id) -> None:
        Project.objects.filter(id=id).first().delete()
        print(f'Project {id} was deleted')


class TaskService:
    """ Class containing CRUD operations with Task model
    """
    
    @staticmethod
    def create_task(_title, _creator, _description, _is_done, _status, _deadline) -> None:
        task = Task.objects.create(
            title=_title,
            creator=_creator,
            description=_description,
            is_done=_is_done,
            status=_status,
            deadline=_deadline
        )
        task.save()
    
    @staticmethod
    def get_task_by_id(id) -> None:
        task = Task.objects.filter(id=id).first()
        return task

    @staticmethod
    def delete_task_by_id(id) -> None:
        Task.objects.filter(id=id).first().delete()
        print(f'Task {id} was deleted')


class ProjectTaskService:
    """ Class containing CRUD operations with ProjectTask model
    """
    
    @staticmethod
    def create_record(_user, _project, _task) -> None:
        record= User_Project_Task.objects.create(
            user=_user,
            project=_project,
            task=_task
        )
        record.save()
        print(f'Record {id} was saved')

    @staticmethod
    def get_record_by_id(id) -> None:
        record = User_Project_Task.objects.filter(id=id).first()
        return record

    @staticmethod
    def delete_record_by_id(id) -> None:
        User_Project_Task.objects.filter(id=id).first().delete()
        print(f'Record {id} was deleted')