from rest_framework.permissions import IsAdminUser
from djrest_wrapper.interfaces import BaseViewSet
from .. import serializers as ser
from ..models import Content


class ContentViewSet(BaseViewSet):
    queryset=Content.objects.all()
    page_result_key='contents'
    serializer_action_classes = {
        'create': {
            'req': ser.ContentCreateReqSerilizer,
            'res': ser.ContentCreateResSerilizer,
        },
        'list': {
            'res': ser.ContentListResSerilizer,
        },
        'retrieve': {
            'res': ser.ContentRetrieveResSerilizer,
        },
        'update': {
            'req': ser.ContentUpdateReqSerilizer,
            'res': ser.ContentUpdateResSerilizer,
        }
    }
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
