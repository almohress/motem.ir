from rest_framework.filters import BaseFilterBackend


class PublishedFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser:
            return queryset.all()
        else:
            return queryset.filter(is_published=True)
