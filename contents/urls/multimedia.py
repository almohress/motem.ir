from rest_framework.routers import DefaultRouter
from ..views import MultimediaViewSet

router = DefaultRouter()
router.register(r'multimedia', MultimediaViewSet, basename='multimedia')
urlpatterns = router.urls
