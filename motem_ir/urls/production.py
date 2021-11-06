from django.urls import path, include


urlpatterns = [
    path('',include('contents.urls')),
    path('', include('users.urls')),
]
