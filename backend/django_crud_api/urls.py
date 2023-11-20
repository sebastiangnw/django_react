"""
URL configuration for django_crud_api project.

"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls"), name="tasks")
]
