from djrest_wrapper.interfaces import BaseViewSet
from ..services import ContentService
from .. import serializers as ser
from ..models import Content


class ContentViewSet(BaseViewSet):
    service = ContentService(Content)
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
