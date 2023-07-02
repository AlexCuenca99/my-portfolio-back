from rest_framework import routers

from .viewsets import ProjectModelViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectModelViewSet, basename="project")
urlpatterns = router.urls
