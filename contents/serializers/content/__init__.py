from rest_framework import serializers
from ...models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified'
                  'is_published', 'category', 'files']


class ContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'last_modified',
                  'is_published', 'category', 'files']
