from django.http import HttpResponse
from guest.models import Guest 
from guest.services import get_guest
from django.shortcuts import render

def guest_evaluation(request):
    guest_id = request.POST.get('user_id')
    guest_instance = get_guest(guest_id)

    guest_instance.evaluation = request.POST['evaluation']
    guest_instance.save()

    return render(request, 'choice.html')


# def restart_button(request):
#      return render(request, 'choice.html')