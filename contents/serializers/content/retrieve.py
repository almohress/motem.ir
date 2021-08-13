from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentRetrieveResSerilizer(serializers.Serializer):
    catagory = ser.CataogryRetrieveResSerilizer()
    files = ser.MultimediaRetrieveResSerilizer()

    class Meta:
        Model = Content
        fields = {'id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files'}
