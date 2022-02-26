from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('vehicles/', views.All_Vehicles.as_view()),
    path('vehicle/<str:pk>', views.Vehicle_Detail.as_view()),
    path('vehicle/<str:pk>/distance', views.Mileage_Counter, name='pk'),
    path('vehicle/<str:pk>/history', views.Mileage_Details.as_view({'get': 'list'})),
])
