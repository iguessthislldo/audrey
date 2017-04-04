from django.db import models

from tag.models import *

TASK_NAME_MAX_LENGTH = 256

class Task(Tagged_Object):
    name = models.CharField(
        max_length = TASK_NAME_MAX_LENGTH,
        default = 'Task'
    )

    done = models.BooleanField(
        default = False,
    )

    description = models.TextField(default='')

    def __str__(self):
        return self.name

