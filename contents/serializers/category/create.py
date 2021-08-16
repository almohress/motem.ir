from rest_framework import serializers
from contents.models import Category


class CategoryCreateReqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'title', 'description', 'files']


class CategoryCreateResSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']
