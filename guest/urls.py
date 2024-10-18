from django.urls import path
from .views import register, verify, save_visit_or_anonymous_evaluation, list_students_as_json, StudentListView

urlpatterns = [
    path('', register, name='register'),
    path('students/', list_students_as_json, name='students'),
    path('verify/', verify, name='verify'),
    path('thanks/', save_visit_or_anonymous_evaluation, name='thanks'),
]
