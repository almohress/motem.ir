from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentUpdateReqSerilizer(serializers.Serializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files']


class ContentUpdateResSerilizer(serializers.Serializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files']
