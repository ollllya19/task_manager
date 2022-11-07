
from django.contrib import admin

from .models import UserProfile, Project, Task

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'image', 'joined_date')
    list_display_links = ('id',)
    search_fields = ('user', 'first_name')
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title', 'created_at')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'user', 'description', 'status', 'todo_date', 'created_at')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title', 'user', 'created_at')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
