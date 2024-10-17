"""
business rule 
"""
from django.shortcuts import render
from guest.models import Guest, Student 
from guest.services import get_guest, increment_student_visits
from .student_list_view import StudentListView


def _get_all_data(request):
    guest_id = request.POST.get('user_id')
    guest_instance = get_guest(guest_id)

    student_name = request.POST['student_name']
    student_instance = Student.objects.filter(student_name=student_name).first()
    student_id = student_instance.pk

    return guest_id, guest_instance, student_instance, student_id


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


def _render_thanks(request, guest_id, student_id, common_context=None):
    return render(request, 'thanks.html', {"user_id": guest_id, "student_id": student_id})


def _increment_visit_and_render(guest_instance: Guest, student_instance: Student):
    return increment_student_visits(guest_instance, student_instance)


def _verify_student_visit(request, guest_instance, guest_id, student_instance, student_id, common_context=None):
    if not _is_visit_valid(student_instance, guest_instance):
        return _render_register(request, guest_id, common_context)
    
    _increment_visit_and_render(guest_instance, student_instance)
    return _render_thanks(request, guest_id, student_id)

def verify(request):
    guest_id, guest_instance, student_instance, student_id = _get_all_data(request)
    
    if request.method == 'POST':
        _verify_student_visit(request, guest_instance, guest_id, student_instance, student_id)
        return StudentListView.as_view()

    return _render_register(request, guest_id)
