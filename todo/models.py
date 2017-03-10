from django.db import models

from tag.models import *

class Task(Tagged_Object):
    name = models.CharField(
        max_length = 256,
        default = 'Task'
    )

    description = models.TextField(default='')

    def __str__(self):
        return self.name

