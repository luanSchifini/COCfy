from django.shortcuts import render

from guest.models import Guest


def choice(request):
    if request.method == 'POST':
        anonymous_guest = Guest.objects.create()
        return render(request, 'thanks.html', {'user_id':anonymous_guest.pk})  

    return render(request, 'choice.html')
