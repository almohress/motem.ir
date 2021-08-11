
from .category import urlpatterns as category_urls
from .content import urlpatterns as content_urls


urlpatterns = category_urls+content_urls
