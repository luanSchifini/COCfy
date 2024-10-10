"""
business rule 
"""
from django.shortcuts import render
from guest.models import Guest, Student 
from guest.services import increment_student_visits


def _is_visit_valid(student_instance: Student, guest_instance: Guest) -> bool:
    is_any_required_info_missing = (
        student_instance is None or
        guest_instance is None 
    )
    if is_any_required_info_missing:
        return False

    return True
 

def _render_register(request, guest_id, common_context=None):
    return render(request, 'register.html', {"user_id": guest_id})


def _increment_visit(request, guest_instance: Guest, student_instance: Student):
    return increment_student_visits(guest_instance, student_instance)


def _verify_student_visit(request, student_instance, guest_instance, guest_id, common_context=None):
    if not _is_visit_valid(student_instance, guest_instance):
        return _render_register(request, common_context, guest_id)

    return _increment_visit(request, guest_instance, student_instance)


def verify(request, student_instance, guest_instance, guest_id):
    if request.method == 'POST':
        return _verify_student_visit(request, student_instance, guest_instance, guest_id)

    return _render_register(request)
