from django.urls import path 
from .import views
urlpatterns = [
    path("", views.exam_registration, name = "exam-registration"),
    path("sucess/", views.sucess, name = "sucess"),
]
