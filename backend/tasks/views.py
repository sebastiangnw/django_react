"""This file contains the views for the tasks app."""

# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for Task model."""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
