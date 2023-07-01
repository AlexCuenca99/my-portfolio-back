from rest_framework import viewsets

from .serializers import ProjectModelSerializer

from .models import Project


class ProjectModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all projects in the system.

    For more details on projects please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """

    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
