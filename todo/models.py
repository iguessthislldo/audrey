from django.db import models

from tag.models import *

class Task(TaggedObject):
    name = models.CharField(
        max_length = 256,
        default = 'Task'
    )
    description = models.TextField(default='')
