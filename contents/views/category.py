from rest_framework.permissions import IsAdminUser
from djrest_wrapper.interfaces import BaseViewSet
from ..models import Category
from .. import serializers as ser


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    page_result_key = 'categories'
    serializer_action_classes = {
        'create': {
            'req': ser.CategorySerializer,
            'res': ser.CategorySerializer,
        },
        'list': {
            'res': ser.CategoryListSerializer,
        },
        'retrieve': {
            'res': ser.CategorySerializer,
        },
        'update': {
            'req': ser.CategorySerializer,
            'res': ser.CategorySerializer,
        }
    }
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
