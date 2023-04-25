from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('task/', include('task.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="DanbiEdu Assignment Server API",
        default_version='v1',
        description="API for danbiEdu assignment server",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    )

urlpatterns += [
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
            )
]
