from email.policy import default
from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    """ Table containing information about User
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='uploads/', 
        blank=True, 
        null=True)
    thumbnail = models.ImageField(
        upload_to='uploads/', 
        blank=True, 
        null=True)
    joined_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.first_name
    
    def get_image(self) -> str:
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self) -> str:
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumnail(self, image, size=(300, 200)) -> File:
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail = File(thumb_io, name=image.name) 
        
        return thumbnail


class Project(models.Model):
    """ Table containing information about a project
    """
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    """ Table containing information about a task
    """    
    # status types of task
    TODO = 1
    DOING = 2
    DONE = 3
    STATUSES = [(TODO, 1), (DOING, 2), (DONE, 3)]
    
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True
    )
    description = models.CharField(max_length=255)
    status = models.IntegerField(
        choices=STATUSES,
        default=TODO
    )
    todo_date = models.DateField(null=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL, 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.title
