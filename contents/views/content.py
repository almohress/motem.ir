from rest_framework.permissions import IsAdminUser
from djrest_wrapper.interfaces import BaseViewSet
from .. import serializers as ser
from ..models import Content
from ..filters import PublishedFilterBackend, ContentCategoryFilterBackend


class ContentViewSet(BaseViewSet):
    queryset = Content.objects.all()
    page_result_key = 'contents'
    filter_backends = [PublishedFilterBackend, ContentCategoryFilterBackend]
    serializer_action_classes = {
        'create': {
            'req': ser.ContentSerializer,
            'res': ser.ContentSerializer,
        },
        'list': {
            'res': ser.ContentListSerializer,
        },
        'retrieve': {
            'res': ser.ContentSerializer,
        },
        'update': {
            'req': ser.ContentSerializer,
            'res': ser.ContentSerializer,
        },
        'partial_update': {
            'req': ser.ContentSerializer,
            'res': ser.ContentSerializer,
        }
    }
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
