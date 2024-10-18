from guest.services import get_guest
from django.shortcuts import render


def _get_all_data(request):
    guest_id = request.POST.get('user_id')
      
    return guest_id


def guest_evaluation(request, guest_id):
    guest_instance = get_guest(guest_id)

    guest_instance.evaluation = request.POST['evaluation']
    guest_instance.save()

    return _render_register(request)


def _render_choice(request):
    return render(request, 'choice.html')


def _render_register(request):
    return render(request, 'register.html')


def _render_thanks(request, guest_id):
    return render(request, 'thanks.html', {"user_id": guest_id})


def save_visit_or_anonymous_evaluation(request):
    guest_id = _get_all_data(request)
    
    if request.method == 'POST':
        guest_evaluation(request, guest_id)
        return _render_register(request)

    return _render_thanks(request, guest_id) 
