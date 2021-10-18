from rest_framework.filters import BaseFilterBackend
from distutils.util import strtobool
from uuid import UUID


class PublishedFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            is_published = bool(strtobool(
                request.query_params.get('is_published', None)))
            return queryset.filter(is_published=is_published)
        except ValueError:
            return queryset.filter(is_published=True)
        except AttributeError:
            return queryset.all()


class ContentCategoryFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            category_id = request.query_params.get('category_id', None)
            UUID(category_id)
            return queryset.filter(category__id=category_id)
        except ValueError:
            return queryset.all()
