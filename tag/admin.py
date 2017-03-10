from django.contrib import admin

from .models import *

admin.site.register(Tag)

class Tag_Inline(admin.TabularInline):
    model = Tagging

class Tagged_Object_Admin(admin.ModelAdmin):
    inlines = [
        Tag_Inline,
    ]

admin.site.register(Tagged_Object, Tagged_Object_Admin)
