from django.utils.regex_helper import contains
from .settings import DEBUG
from django.urls import path, include

urls = [
    path('',include('contents.urls')),
    path('', include('users.urls')),
]

if DEBUG:
    from djrest_wrapper.permissions import AllowAnyPerm
    from django.conf.urls import url
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    schema_view = get_schema_view(
        openapi.Info(
            title="motem.ir API",
            default_version='v1',
            description="motem.ir API",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[AllowAnyPerm],
    )

    urlpatterns = [
        url(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
    ]

    urlpatterns += urls
else:
    urlpatterns = urls
