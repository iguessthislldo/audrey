from django.apps import AppConfig
from django.db.models.signals import post_save

class TaskConfig(AppConfig):
    name = 'task'
    
    def ready(self):
        import task.signals
        
