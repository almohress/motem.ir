from djrest_wrapper.interfaces import BaseViewSet
from ..services import MultimediaService
from .. import serializers as ser
from ..models import Multimedia
from rest_framework.response import Response

class MultimediaViewSet(BaseViewSet):
    service = MultimediaService(Multimedia)
    serializer_action_classes = {
        'create': {
            'req': ser.MultimediaCreateReqSerializer,
            'res': ser.MultimediaCreateResSerializer,
        },
        'list': {
            'res': ser.MultimediaListResSerializer,
        },
        'retrieve': {
            'res': ser.MultimediaRetrieveResSerializer,
        },
        'update': {
            'req': ser.MultimediaUpdateReqSerializer,
            'res': ser.MultimediaUpdateResSerializer,
        }
    }
    def create(self, request, *args, **kwargs):
        file_uploaded = request.FILES.get('file')
        content_type = file_uploaded.content_type
        request_json = request.data
        self.service.create_model(file=file_uploaded,fields=request_json)
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
