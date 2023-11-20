"""Urls"""

from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views


router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls), name="index"),
    path("docs/", include_docs_urls(title="Task API"), name="docs")
]
