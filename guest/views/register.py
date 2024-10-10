"""
business rule
"""
import random
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage


from guest.models import Guest, Student
from guest.services import select_students, get_guest, get_student, increment_student_visits
from guest.services import select_students, register_guest, select_eletiva_group


#### SEARCH FILTER ONLY


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




##### CODE WITHOUT VERIFICATION


# def _get_all_data(request):
#     name = request.POST['name']

#     guest_instance = Guest.objects.filter(name=name).first()
    
#     return name, guest_instance


# def guest_instance_not_exists(guest_instance: Guest) -> bool:        
#     if guest_instance is not None:
#         return True


# def _render_register_form(request, common_context):
#     positive_context = {**common_context, 'already_visited': True}
#     return render(request, 'register.html', positive_context)


# def _render_verify_url(request, new_guest_instance: Guest, eletiva_id: int, group_id: int):
#     guest_id = new_guest_instance.pk
#     success_register_context = {'user_id': guest_id, 'eletiva_id': eletiva_id, 'group_id': group_id, 'students': select_students(group_id)}
#     return render(request, 'verify.html', success_register_context)


# def register_guest_instance(request, common_context, eletiva_id, group_id):
#     name, guest_instance = _get_all_data(request)

#     if guest_instance_not_exists(guest_instance):
#         return _render_register_form(request, common_context)        
#     else:        
#         new_guest_instance = register_guest(name)
#         return _render_verify_url(request, new_guest_instance, eletiva_id, group_id)


# def _display_register_form(request, common_context):
#     return render(request, 'register.html',  common_context)


# def register(request):
#     eletiva_id = request.GET.get('eletiva_id', request.POST.get('eletiva'))
#     group_id = request.GET.get('group_id', request.POST.get('group'))

#     common_context = {'groups': select_eletiva_group(eletiva_id), 'eletiva_id': eletiva_id, 'group_id': group_id}

#     if request.method == 'POST':
#         return register_guest_instance(request, common_context, eletiva_id, group_id)
    
#     return _display_register_form(request, common_context)




#### EMAIL / VERIFICATION CODE 


# def create_verification_code() -> int:
#     return random.randint(10000, 99999)


# def _get_all_data(request):
#     name = request.POST['name']
#     guest_mail = request.POST['email']
#     code = create_verification_code()

#     guest_instance = Guest.objects.filter(email=guest_mail).first()
    
#     return name, guest_mail, code, guest_instance


# def send_mail(code: int, guest_mail: str) -> int:
#     mail_subject = 'obrigado por prestigiar nossa feira científica'
#     message = f'seu código de verificação é {code}'
#     verification_message = EmailMessage(mail_subject, message, to=[guest_mail])
#     verification_message.send()


# def guest_instance_not_exists(guest_instance: Guest) -> bool:        
#     if guest_instance is not None:
#         return True


# def _render_register_form(request, common_context):
#     positive_context = {**common_context, 'already_visited': True}
#     return render(request, 'register.html', positive_context)


# def _render_verify_url(request, new_guest_instance: Guest, eletiva_id: int, group_id: int):
#     guest_id = new_guest_instance.pk
#     success_register_context = {'user_id': guest_id, 'eletiva_id': eletiva_id, 'group_id': group_id, 'students': select_students(group_id)}
#     return render(request, 'verify.html', success_register_context)


# def register_guest_instance(request, common_context, eletiva_id, group_id):
#     name, guest_mail, code, guest_instance = _get_all_data(request)

#     if guest_instance_not_exists(guest_instance):
#         return _render_register_form(request, common_context)        
#     else:        
#         new_guest_instance = register_guest(name, guest_mail, code)
#         send_mail(code, guest_mail)
#         return _render_verify_url(request, new_guest_instance, eletiva_id, group_id)


# def _display_register_form(request, common_context):
#     return render(request, 'register.html',  common_context)


# def register(request):
#     eletiva_id = request.GET.get('eletiva_id', request.POST.get('eletiva'))
#     group_id = request.GET.get('group_id', request.POST.get('group'))

#     common_context = {'groups': select_eletiva_group(eletiva_id), 'eletiva_id': eletiva_id, 'group_id': group_id}

#     if request.method == 'POST':
#         return register_guest_instance(request, common_context, eletiva_id, group_id)
    
#     return _display_register_form(request, common_context)
