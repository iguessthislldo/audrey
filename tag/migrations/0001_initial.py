# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meta_Tag',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tagged_Object',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tag.Meta_Tag')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
                ('tagged_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tagged_Object')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tagging',
            unique_together=set([('tagged_object', 'tag', 'meta_tag')]),
        ),
    ]
