from guest.models import Student 
from django.http import JsonResponse


def list_students_as_json(request):    
    students = Student.objects.all()
    return JsonResponse([student.student_name for student in students], safe=False)

