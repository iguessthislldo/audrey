from django.db.models.signals import post_save
from django.dispatch import receiver

from task.models import Task
from tag.models import Meta_Tag

@receiver(post_save, sender=Task)
def task_post_save(sender, **kw):
    they = kw['instance']
    they.done(False)

