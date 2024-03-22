from django.urls import path
from . import views

urlpatterns = [
    path('travel-booking/', views.travel_booking, name='travel_booking'),
]