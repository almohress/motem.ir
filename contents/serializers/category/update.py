from rest_framework import serializers
from contents.models import Category
from ..multimedia import MultimediaUpdateReqSerilizer, MultimediaUpdateResSerilizer


class CategoryUpdateReqSerializer(serializers.ModelSerializer):
    files = MultimediaUpdateReqSerilizer()

    class Meta:
        model = Category
        fields = ['name', 'title', 'description', 'files']


class CategoryUpdateResSerializer(serializers.ModelSerializer):
    files = MultimediaUpdateResSerilizer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']
