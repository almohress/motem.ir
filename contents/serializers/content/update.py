from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentUpdateReqSerilizer(serializers.Serializer):
    catagory = ser.CataogryUpdateReqSerilizer()
    files = ser.MultimediaUpdateReqSerilizer()

    class Meta:
        Model = Content
        fields = {'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files'}


class ContentUpdateResSerilizer(serializers.Serializer):
    catagory = ser.CataogryUpdateResSerilizer()
    files = ser.MultimediaUpdateResSerilizer()

    class Meta:
        fields = {'id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files'}
