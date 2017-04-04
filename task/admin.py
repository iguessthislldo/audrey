from django.contrib import admin

from .models import *
from tag.admin import *

#admin.site.register(Tag)
#admin.site.register(Meta_Tag)

class Task_Admin(admin.ModelAdmin):
    inlines = [
        Tag_Inline,
    ]

admin.site.register(Task, Task_Admin)

# Register your models here.
