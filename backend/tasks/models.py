"""This file contains the models for the tasks app."""

from django.db import models

# Create your models here.


class Task(models.Model):
    """This class defines the model for a task."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
