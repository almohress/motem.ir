from rest_framework import serializers
from contents.models import Category


class CategoryRetrieveResSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']
