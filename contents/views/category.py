from djrest_wrapper.interfaces import BaseViewSet
from ..models import Category
from .. import serializers as ser


class CategoryViewSet(BaseViewSet):
    queryset=Category.objects.all()
    page_result_key = 'categories'
    serializer_action_classes = {
        'create': {
            'req': ser.CategoryCreateReqSerializer,
            'res': ser.CategoryCreateResSerilizer,
        },
        'list': {
            'res': ser.CategoryListResSerializer,
        },
        'retrieve': {
            'res': ser.CategoryRetrieveResSerializer,
        },
        'update': {
            'req': ser.CategoryUpdateReqSerializer,
            'res': ser.CategoryUpdateResSerializer,
        }
    }
