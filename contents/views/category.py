from djrest_wrapper.decorators import serializer_validation
from rest_framework.viewsets import ModelViewSet
from ..services import CategoryService
from .. import serializers as ser
from ..models import Category
from djrest_wrapper import permissions as perm


class CategoryViewSet(ModelViewSet):
    service = CategoryService(Category)
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
    permission_action_classes = {
        'create': [perm.IsAdminUserPerm],
        'update': [perm.IsAdminUserPerm],
        'destroy': [perm.IsAdminUserPerm]
    }

    @serializer_validation
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @serializer_validation
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)