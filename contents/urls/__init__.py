from rest_framework.routers import DefaultRouter
from ..views import MultimediaViewSet, CategoryViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'multimedia', MultimediaViewSet, basename='multimedia')
router.register(r'contents', ContentViewSet, basename='content')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
