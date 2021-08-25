from rest_framework.permissions import IsAdminUser
from djrest_wrapper.interfaces import BaseViewSet
from ..models import Multimedia
from .. import serializers as ser


class MultimediaViewSet(BaseViewSet):
    queryset = Multimedia.objects.all()
    page_result_key = 'multimedia'
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
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
