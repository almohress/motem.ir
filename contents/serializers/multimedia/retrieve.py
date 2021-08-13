from rest_framework import serializers
from contents.models import Multimedia


class MultimediaRetrieveResSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Multimedia
        fields = {'id', 'file', 'last_modified', 'is_video'}