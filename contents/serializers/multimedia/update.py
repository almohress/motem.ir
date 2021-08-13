from rest_framework import serializers
from contents.models import Multimedia


class MultimediaUpdateReqSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Multimedia
        fields = {'file', 'last_modified', 'is_video'}


class MultimediaUpdateResSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {'id', 'file', 'last_modified', 'is_video'}
