from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("", include("api.core.urls")),
    path("admin/", admin.site.urls),
    path("v1/", include("urls.v1.public_urls")),
]

if settings.ENVIRONMENT in ["local", "development"]:
    urlpatterns += [
        path("__debuig__/", include("debug_toolbar.urls")),
    ]
