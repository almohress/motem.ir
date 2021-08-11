from rest_framework import serializers
from contents.models import Category
from ..multimedia import MultimediaCreateResSerilizer


class CategoryCreateReqSerializer(serializers.modelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'title', 'description']


class CategoryCreateResSerilizer(serializers.Serializer):
    file = MultimediaCreateResSerilizer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'description', 'files']
