from django.urls import path 
from .import views

urlpatterns = [
    path('feedback.form/',views.feedback_form , name = 'feedback'),
    
]
