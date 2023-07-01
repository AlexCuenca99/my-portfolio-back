from django.urls import include, path
from django.contrib import admin

from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        default_version="v1",
        title="Alex Cuenca Portfolio API",
        license=openapi.License(name="BSD License"),
        terms_of_service="https://www.google.com/policies/terms/",
        description="Documentation for Alex Cuenca Portfolio API",
        contact=openapi.Contact(email="alex-patricio1999@hotmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Yasg and Redoc Urls
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Base Urls
    path("admin/", admin.site.urls),
    # Local Apps Urls
    path("api/v1/", include("applications.project.routers")),
]
