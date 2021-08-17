from rest_framework import serializers
from contents.models import Content, category
from contents import serializers as ser


class ContentCreateReqSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'body', 'last_modified',
                  'is_published', 'category', 'files']


class ContentCreateResSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'category', 'files']
