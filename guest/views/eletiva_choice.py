from django.shortcuts import render 
from guest.models import Guest
from guest.services import select_eletivas, select_eletiva_group


def _render_register_form(request, eletiva_id):
    return render(request, 'register.html', {'eletiva_id': eletiva_id, 'groups': select_eletiva_group(eletiva_id)})


def eletiva_choice(request):
    eletiva_id = request.GET.get('eletiva_id', request.POST.get('eletiva'))

    if request.method == 'POST':
        if eletiva_id is not None:
            return _render_register_form(request, eletiva_id)

    return render(request, 'eletiva_choice.html', {'eletivas': select_eletivas(), 'eletiva_id': eletiva_id})

