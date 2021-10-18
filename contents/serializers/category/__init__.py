from rest_framework import serializers
from ..multimedia import MultimediaSerializer
from ...models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']


class CategoryResponseSerializer(serializers.ModelSerializer):
    files = MultimediaSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'files']
