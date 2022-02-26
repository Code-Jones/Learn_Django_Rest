from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', include('vehicleApi.urls')),
    path('health', views.health_test)
]




