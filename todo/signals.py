from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.models import Task
from tag.models import Meta_Tag
from tag.utils.boolean_tag import *

DONE_TAG_NAME = 'done'

def get_done_tag():
    return Meta_Tag.objects.get_or_create(name = DONE_TAG_NAME)[0]

@receiver(post_save, sender=Task)
def task_post_save(sender, **kw):
    they = kw['instance']
    if not they.tagging_set.filter(meta_tag__name = DONE_TAG_NAME).exists():
        they.tagging_set.create(
            meta_tag = get_done_tag(),
            tag = get_boolean_tag(False),
        )

