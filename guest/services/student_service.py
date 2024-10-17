from typing import List
from guest.models import Student, Guest


"""
SOLID
Single responsibility principle
Open-close principle
Liskov substitution principle
Interface Segregation principle
Dependency invertion principle
"""


def get_student(student_id: str) -> Student | None:
    try:
       return Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        pass  # Handle the case where the student doesn't exist


def select_students(group_id) -> List[Student]:
    eletiva_group = get_eletiva_group(group_id)
    if eletiva_group is None:
        return Student.objects.all()
    
    return Student.objects.filter(eletiva_group=eletiva_group)


def increment_student_visits(guest: Guest, student: Student):
    guest.student_visited = student
    guest.save()
