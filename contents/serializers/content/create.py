from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentCreateReqSerilizer(serializers.Serializer):

    class Meta:
        model = Content
        fields = ['title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files']


class ContentCreateResSerilizer(serializers.Serializer):

    class Meta:
        Mmdel = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files']
