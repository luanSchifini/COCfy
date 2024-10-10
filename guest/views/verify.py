"""
business rule 
"""
# from guest.views.thanks import guest_evaluation
from django.shortcuts import render
from guest.models import Guest, Student 
from guest.services import get_guest, get_student, increment_student_visits


#### SEARCH FILTER ONLY


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



#### WITHOUT VERIFICATION 


# def _is_visit_valid(student_instance: Student, guest_instance: Guest) -> bool:
#     is_any_required_info_missing = (
#         student_instance is None or
#         guest_instance is None 
#     )
#     if is_any_required_info_missing:
#         return False

#     return True
 
# def _get_all_data(request):
#     guest_id = request.POST.get('user_id')
#     guest_instance = get_guest(guest_id)

#     student_id = request.POST.get('student')   
#     student_instance = get_student(student_id)

#     return student_instance, guest_instance, guest_id


# def _render_verify_form(request, common_context, guest_id):
#     negative_context = {**common_context, 'was_success': False, "user_id": guest_id}
#     return render(request, 'verify.html', negative_context)


# def _increment_visit_and_render(request, common_context, student_instance: Student, guest_instance: Guest, guest_id: int):
#     increment_student_visits(guest_instance, student_instance)

#     positive_context = {**common_context, 'student_name': student_instance.student_name, 'guest_name': guest_instance.name, 'user_id': guest_id}
#     return render(request, 'thanks.html', positive_context)


# def _verify_student_visit(request, common_context):
#     student_instance, guest_instance, guest_id= _get_all_data(request)

#     if not _is_visit_valid(student_instance, guest_instance):
#         return _render_verify_form(request, common_context, guest_id)

#     return _increment_visit_and_render(request, common_context, student_instance, guest_instance, guest_id)


# def _display_visit_form(request, common_context):
#     return render(request, 'verify.html', common_context)


# def verify(request):
#     eletiva_id = request.POST.get('eletiva')
#     group_id = request.POST.get('group')

#     common_context = {'students': select_students(group_id), 'group_id': group_id, 'eletiva_id': eletiva_id}

#     if request.method == 'POST':
#         return _verify_student_visit(request, common_context)

#     return _display_visit_form(request, common_context)




#### EMAIL / VEFIFICATION CODE


# def _is_visit_valid(student_instance: Student, guest_instance: Guest, verification_code: str) -> bool:
#     is_any_required_info_missing = (
#         student_instance is None or
#         guest_instance is None or
#         verification_code is None or verification_code == ''
#     )
#     if is_any_required_info_missing:
#         return False

#     is_received_code_correct = verification_code == guest_instance.verification_code
#     return is_received_code_correct

 
# def _get_all_data(request):
#     verification_code = request.POST.get('verification_code')

#     guest_mail = request.POST.get('guest_mail')
#     guest_id = request.POST.get('user_id')
#     guest_instance = get_guest(guest_id)

#     student_id = request.POST.get('student')   
#     student_instance = get_student(student_id)

#     return student_instance, guest_instance, verification_code, guest_id, guest_mail


# def _render_verify_form(request, common_context, guest_id):
#     negative_context = {**common_context, 'was_success': False, "user_id": guest_id}
#     return render(request, 'verify.html', negative_context)


# def _increment_visit_and_render(request, common_context, student_instance: Student, guest_instance: Guest, guest_id: int):
#     increment_student_visits(guest_instance, student_instance)

#     positive_context = {**common_context, 'student_name': student_instance.student_name, 'guest_name': guest_instance.name, 'user_id': guest_id, 'guest_mail': guest_instance.email}
#     return render(request, 'thanks.html', positive_context)


# def _verify_student_visit(request, common_context):
#     student_instance, guest_instance, verification_code, guest_id, guest_mail = _get_all_data(request)

#     if not _is_visit_valid(student_instance, guest_instance, verification_code):
#         return _render_verify_form(request, common_context, guest_id)

#     return _increment_visit_and_render(request, common_context, student_instance, guest_instance, guest_id)


# def _display_visit_form(request, common_context):
#     return render(request, 'verify.html', common_context)


# def verify(request):
#     eletiva_id = request.POST.get('eletiva')
#     group_id = request.POST.get('group')

#     common_context = {'students': select_students(group_id), 'group_id': group_id, 'eletiva_id': eletiva_id}

#     if request.method == 'POST':
#         return _verify_student_visit(request, common_context)

#     return _display_visit_form(request, common_context)
