from rest_framework import serializers

from .models import *

class Tag_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length = TAG_NAME_MAX_LENGTH)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
