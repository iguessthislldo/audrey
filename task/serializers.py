from rest_framework import serializers

from tag.serializers import Tagged_Object_Serializer
from .models import *

class Task_Serializer(Tagged_Object_Serializer):
    name = serializers.CharField(
        required = True,
        allow_blank = False,
        max_length = TASK_NAME_MAX_LENGTH
    )

    description = serializers.CharField(
        required = True,
        allow_blank = True,
    )

    done = serializers.BooleanField(
        required = True,
    )

    def create(self, validated_data):
        instance = Task.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description= validated_data.get(
            'description', instance.description
        )
        instance.done = validated_data.get('done', instance.done)
        return instance

