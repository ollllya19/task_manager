from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-manager/', include('api.urls')),
    # jwt authorization
    path('task-manager/auth/', include('djoser.urls')),
    re_path(r'^task-manager/', include('djoser.urls.authtoken')),
]