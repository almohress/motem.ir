from rest_framework import serializers
from contents.models import Multimedia


class MultimediaListResSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multimedia
        fields = ['id', 'file', 'last_modified', 'is_video']
