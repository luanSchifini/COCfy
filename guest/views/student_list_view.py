from django.shortcuts import render
from django.views.generic import ListView
from models import Student
import json 


class StudentListView(ListView):
    model = Student
    template_name = 'clara coloca o nome do tamplate aqui'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Student.objects.name)) 
        return context