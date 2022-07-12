from django.urls import path

from api.core import views

urlpatterns = [
    path("version/", views.VersionView.as_view(), name="version"),
    path("health/", views.HealthCheckView.as_view(), name="health"),
]
