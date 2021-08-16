from djrest_wrapper.interfaces import BaseViewSet
from .. import serializers as ser


class MultimediaViewSet(BaseViewSet):
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
