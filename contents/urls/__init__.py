
from .category import urlpatterns as category_urls
from .multimedia import urlpatterns as multimedia_urls
from .content import urlpatterns as contents_urls


urlpatterns = category_urls+multimedia_urls+contents_urls
