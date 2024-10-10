from django.urls import path
from .views import choice, eletiva_choice, register, verify, guest_evaluation, save_visit_or_anonymous_evaluation

urlpatterns = [
    path('choice/', choice, name='choice'),
    path('eletiva_choice/', eletiva_choice, name='eletiva_choice'),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('thanks/', save_visit_or_anonymous_evaluation, name='thanks'),
]
