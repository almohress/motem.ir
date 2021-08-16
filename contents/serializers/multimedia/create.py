from rest_framework import serializers
from contents.models import Multimedia


class MultimediaCreateReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = ['file', 'last_modified']


class MultimediaCreateResSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multimedia
        fields = ['id', 'file', 'last_modified', 'is_video']
