from django.views.generic import ListView
from guest.models import Student
from django.utils.safestring import mark_safe
import json

class StudentListView(ListView):
    model = Student
    template_name = 'verify.html'
    
    