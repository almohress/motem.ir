from djrest_wrapper.interfaces import BaseViewSet
from djrest_wrapper.decorators import serializer_validation, create_model, list_model, retrieve_model, update_model, delete_model
from ..services import CategoryService
from .. import serializers as ser
from ..models import Category
from djrest_wrapper import permissions as perm


class CategoryViewSet(BaseViewSet):
    service = CategoryService(Category)
    page_result_key = 'Category'
    serializer_action_classes = {
        'create': {
            'req': ser.CataogryCreateReqSerilizer,
            'res': ser.CataogryCreateResSerilizer,
        },
        'list': {
            'res': ser.CataogryListResSerilizer,
        },
        'retrieve': {
            'res': ser.CataogryRetrieveResSerilizer,
        },
        'update': {
            'req': ser.CataogryUpdateReqSerilizer,
            'res': ser.CataogryUpdateResSerilizer,
        }
    }
    permission_action_classes = {
        'update': [perm.IsAdminUserPerm],
        'destroy': [perm.IsAdminUserPerm],
    }
