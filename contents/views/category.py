from djrest_wrapper.interfaces import BaseViewSet
from ..services import CategoryService
from .. import serializers as ser
from ..models import Category
from djrest_wrapper import permissions as perm


class CategoryViewSet(BaseViewSet):
    service = CategoryService(Category)
    page_result_key = 'Categories'
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
    permission_action_classes = {
        'create': [perm.IsAdminUserPerm],
        'update': [perm.IsAdminUserPerm],
        'destroy': [perm.IsAdminUserPerm]
    }
