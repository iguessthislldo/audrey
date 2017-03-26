from django.db import models

from tag.models import *

DONE_TAG_NAME = 'done'
TASK_NAME_MAX_LENGTH = 256

class Task(Tagged_Object):
    name = models.CharField(
        max_length = TASK_NAME_MAX_LENGTH,
        default = 'Task'
    )

    description = models.TextField(default='')

    def done(self, arg = None):
        ts = None
        done_tag = self.get_done_tag()
        query = self.tagging_set.filter(meta_tag = done_tag)

        if query.exists():
            ts = query.get()
            if arg is not None:
                ts.tag = Boolean_Tag.get(arg)
                ts.save()
        else:
            ts = self.tagging_set.create(
                meta_tag = done_tag,
                tag = Boolean_Tag.get(arg),
            )

        return ts.tag.boolean_tag.value

    def __str__(self):
        return self.name

    @staticmethod
    def get_done_tag():
        return Meta_Tag.objects.get_or_create(name = DONE_TAG_NAME)[0]

