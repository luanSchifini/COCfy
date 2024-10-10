"""
business rule
"""
from django.shortcuts import render
from guest.models import Guest, Student
from guest.services import register_guest


def _get_all_data(request):
    name = request.POST['name']
    guest_cpf = request.POST['CPF']
    print('guest cpf')
    print(guest_cpf)
    student_name = request.POST['student_name']

    guest_instance = Guest.objects.filter(verification_code=guest_cpf).first()

    student_instance = Student.objects.filter(student_name=student_name).first()
    
    return name, guest_cpf, guest_instance, student_instance


def guest_instance_exists(guest_instance: Guest) -> bool:        
    if guest_instance == None:
        return False 
    
    return True


def _render_register_form(request):
    positive_context = {'already_visited': True}
    return render(request, 'register.html', positive_context)


def _display_register_form(request, common_context=None):
    return render(request, 'register.html',  common_context)


def _render_verify(request, new_guest_instance: Guest, student_instance: Student, common_context=None):
    guest_id = new_guest_instance.pk
    student_id = student_instance.pk

    success_register_context = {'user_id': guest_id, 'student_id': student_id}
    return render(request, 'thanks.html', success_register_context)


def register_guest_instance(request, common_context=None):
    name, guest_cpf, guest_instance, student_instance = _get_all_data(request)
    print('guest instance')
    print(guest_instance)

    if guest_instance_exists(guest_instance):
        print('guest exists')
        return _render_register_form(request)        
    else:        
        print('guest None')
        new_guest_instance = register_guest(name, guest_cpf)
        return _render_verify(request, new_guest_instance, student_instance)


def register(request):
    if request.method == 'POST':
        return register_guest_instance(request)
    
    return _display_register_form(request)
