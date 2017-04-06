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

class Tagged_Object_Serializer(serializers.Serializer):
    id = serializers.UUIDField(
        read_only=True,
    )

    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        return instance.tags_str()

    def create(self, validated_data):
        tags = validated_data['tags']
        validated_data.pop('tags')

        tagged_object = Tagged_Object.create(**validated_data)
        tagged_object.tag(tags)

        return tagged_object

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
