from django.contrib import admin

from .models import UserProfile, Project, Task, UserProjectTask

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'image', 'joined_date')
    list_display_links = ('id',)
    search_fields = ('user', 'name')
    list_editable = ('name',)
    list_filter = ('user', 'name', 'joined_date')
    
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(UserProjectTask)
