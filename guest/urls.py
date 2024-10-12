from django.urls import path
from .views import register, verify, save_visit_or_anonymous_evaluation

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('thanks/', save_visit_or_anonymous_evaluation, name='thanks'),
]
