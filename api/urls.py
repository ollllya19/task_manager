from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .views.views import TaskAPIView, IncomingTasksAPIView, TodayTasksAPIView, UpcomingTasksAPIView
from .views.project_view import ProjectAPIView, ProejctTasksAPIView

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="Task Manager API",
        terms_of_service="https://example.com",
        contact=openapi.Contact(email="contact@mail.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('task/<int:pk>', TaskAPIView.as_view()),
    # date filtered tasks
    path('tasks/incoming', IncomingTasksAPIView.as_view()),
    path('tasks/today', TodayTasksAPIView.as_view()),
    path('tasks/upcoming', UpcomingTasksAPIView.as_view()),
    # projects api
    path('project/<str:project_name>', ProejctTasksAPIView.as_view()),
    # swagger api
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]