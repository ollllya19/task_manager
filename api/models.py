from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20, blank=True)
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
        return self.name
    
    def get_image(self):
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
    
    
class Team(models.Model):
    name = models.CharField(max_length=30)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # to make automatically 
    member_count = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.name
    

class TeamUser(models.Model):
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "TeamUser"
        verbose_name_plural = "TeamUsers"
        ordering = ["-id"]
        
        unique_together = ('member', 'team')
        
    def __str__(self):
        return f'{self.memeber} - {self.team}'
    

class Task(models.Model):
    name = models.CharField(max_length=30)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["-id"]
        
    def __str__(self) -> str:
        return self.name
