from rest_framework import serializers
from ...models import Content


class ContentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body',
                  'is_published', 'category', 'files']


class ContentListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'last_modified',
                  'is_published', 'category', 'files']
