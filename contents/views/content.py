from rest_framework.permissions import IsAdminUser
from djrest_wrapper.interfaces import BaseViewSet
from .. import serializers as ser
from ..models import Content


class ContentViewSet(BaseViewSet):
    queryset = Content.objects.all()
    page_result_key = 'contents'
    serializer_action_classes = {
        'create': {
            'req': ser.ContentSerilizer,
            'res': ser.ContentSerilizer,
        },
        'list': {
            'res': ser.ContentListSerilizer,
        },
        'retrieve': {
            'res': ser.ContentSerilizer,
        },
        'update': {
            'req': ser.ContentSerilizer,
            'res': ser.ContentSerilizer,
        },
        'partial_update': {
            'req': ser.ContentSerilizer,
            'res': ser.ContentSerilizer,
        }
    }
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
