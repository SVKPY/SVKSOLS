from rest_framework import serializers
from django.db import models
from models import Todo


class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name',
                  'desc',
                  'topic')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.desc = validated_data.get('desc', instance.desc)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.save()
        return instance

