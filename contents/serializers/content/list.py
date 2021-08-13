from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentListResSerilizer(serializers.Serializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files']
