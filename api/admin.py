
from django.contrib import admin

from .models import UserProfile, Project, Task, UserProjectTask

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'image', 'joined_date')
    list_display_links = ('id',)
    search_fields = ('user', 'name')
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'member_count', 'created_at')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title', 'created_at')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'description', 'is_done', 'created_date')
    list_display_links = ('id',)
    search_fields = ('title',)
    list_filter = ('title', 'creator', 'created_date')

class UserProfileTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'task')
    list_display_links = ('id',)
    list_filter = ('user', 'project', 'task')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProjectTask, UserProfileTaskAdmin)