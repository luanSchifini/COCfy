from django.urls import path
from .views import choice, eletiva_choice, register, verify, guest_evaluation

urlpatterns = [
    path('choice/', choice, name='choice'),
    path('eletiva_choice/', eletiva_choice, name='eletiva_choice'),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),
    path('thanks/', guest_evaluation, name='thanks'),
]
