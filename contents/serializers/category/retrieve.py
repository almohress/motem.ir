from rest_framework import serializers
from contents.models import Category
from multimedia import MultimediaRetrieveResSerilizer


class CategoryRetrieveResSerializer(serializers.ModelSerializer):
    files = MultimediaRetrieveResSerilizer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']
