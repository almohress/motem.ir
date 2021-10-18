from rest_framework import serializers
from ...models import Content
from ..multimedia import MultimediaSerializer


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'category', 'files']


class ContentResponseSerializer(serializers.ModelSerializer):
    files = MultimediaSerializer(many=True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'category', 'files']


class ContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'last_modified',
                  'is_published', 'category', 'files']
