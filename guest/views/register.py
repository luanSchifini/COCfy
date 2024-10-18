"""
business rule
"""
from django.shortcuts import render
from guest.models import Guest
from guest.services import register_guest


def _get_all_data(request):
    guest_cpf = request.POST['CPF']
    guest_instance = Guest.objects.filter(cpf=guest_cpf).first()

    return guest_cpf, guest_instance


def guest_instance_exists(guest_instance: Guest) -> bool:        
    if guest_instance == None:
        return False 
    
    return True


def _render_register_form(request):
    positive_context = {'already_visited': True}
    return render(request, 'register.html', positive_context)


def _display_register_form(request, common_context=None):
    return render(request, 'register.html',  common_context)


def _render_verify(request, new_guest_instance: Guest, common_context=None):
    guest_id = new_guest_instance.pk
    print('guest_id')
    print(guest_id)
    success_register_context = {'user_id': guest_id}
    return render(request, 'verify.html', success_register_context)


def register_guest_instance(request, common_context=None):
    guest_cpf, guest_instance = _get_all_data(request)

    if guest_instance_exists(guest_instance):
        print('guest exists')
        return _render_register_form(request)        
    else:        
        print('guest == None')
        new_guest_instance = register_guest(guest_cpf)
        print('new_guest_instance')
        print(new_guest_instance)
        return _render_verify(request, new_guest_instance)


def register(request):
    if request.method == 'POST':
        return register_guest_instance(request)
    
    return _display_register_form(request)
