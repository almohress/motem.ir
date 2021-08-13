from rest_framework import serializers
from contents.models import Content
from contents import serializers as ser


class ContentCreateReqSerilizer(serializers.Serializer):
    catagory = ser.CataogryCreateReqSerilizer()
    files = ser.MultimediaCreateReqSerilizer()

    class Meta:
        Model = Content
        fields = {'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files'}


class ContentCreateResSerilizer(serializers.Serializer):
    catagory = ser.CataogryCreateResSerilizer()
    files = ser.MultimediaCreateResSerilizer()

    class Meta:
        Model = Content
        fields = {'id', 'title', 'body', 'last_modified',
                  'is_published', 'catagory', 'files'}
