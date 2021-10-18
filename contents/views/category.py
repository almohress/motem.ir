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
            'res': ser.CategoryResponseSerializer,
        },
        'list': {
            'res': ser.CategoryListSerializer,
        },
        'retrieve': {
            'res': ser.CategoryResponseSerializer,
        },
        'update': {
            'req': ser.CategorySerializer,
            'res': ser.CategoryResponseSerializer,
        },
        'partial_update': {
            'req': ser.CategorySerializer,
            'res': ser.CategoryResponseSerializer,
        }
    }
    permission_action_classes = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
