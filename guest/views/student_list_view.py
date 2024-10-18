from django.views.generic import ListView
from guest.models import Student


class StudentListView(ListView):    
    model = Student
    template_name = 'verify.html'

    