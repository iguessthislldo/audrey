# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('tagged_object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tag.Tagged_Object')),
                ('name', models.CharField(default='Task', max_length=256)),
                ('description', models.TextField(default='')),
            ],
            bases=('tag.tagged_object',),
        ),
    ]