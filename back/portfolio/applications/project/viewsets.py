from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters

from .serializers import ProjectModelSerializer

from .models import Project

from .paginators import ProjectPagination


class ProjectModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all projects in the system.

    For more details on projects please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """

    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["title", "company", "dev_year", "technologies"]
    search_fields = ["title", "company", "dev_year", "technologies"]
    ordering = ["dev_year"]

    pagination_class = ProjectPagination
