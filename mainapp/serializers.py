from rest_framework import serializers

from mainapp.models import (
    Entity, Property
    )


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ("id", "key", "value")


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ("id", "modified_by", "value", "properties")
        
        read_only_fields = ("modified_by",)


class EntityGetSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(read_only=True, many=True)
    class Meta:
        model = Entity
        fields = ("id", "modified_by", "value", "properties")


