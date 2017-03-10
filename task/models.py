from django.db import models

from tag.models import *
from tag.utils.boolean_tag import *
from tag.utils.saved import assume_saved

class Task(Tagged_Object):
    name = models.CharField(
        max_length = 256,
        default = 'Task'
    )

    description = models.TextField(default='')

    def done(self, arg = None):
        #assume_saved(self)
        meta_tag, created = Meta_Tag.objects.get_or_create(meta_tag__name = 'done')

        if arg is None:
            if created:
                self.tagging_set.get_or_create(meta_tag = meta_tag, tag = get_boolean_tag(False))[0]


    def __str__(self):
        return self.name

