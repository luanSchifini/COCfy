from guest.services import get_guest, get_student
from django.shortcuts import render
from guest.views.verify import verify


def _get_all_data(request):
    guest_id = request.POST.get('user_id')
    guest_instance = get_guest(guest_id)

    student_id = request.POST.get('student_id')   
    if student_id == '':
        student_instance = None
    else: 
        student_instance = get_student(student_id)

    return guest_id, guest_instance, student_id, student_instance   


def guest_evaluation(request):
    guest_id = request.POST.get('user_id')
    guest_instance = get_guest(guest_id)

    guest_instance.evaluation = request.POST['evaluation']
    guest_instance.save()

    return render(request, 'choice.html')


def _render_choice(request):
    return render(request, 'choice.html')


def save_visit_or_anonymous_evaluation(request):
    guest_id, guest_instance, student_id, student_instance = _get_all_data(request)
    
    if request.method == 'POST':
        verify(request, student_instance, guest_instance, guest_id)
        guest_evaluation(request)
        return _render_choice(request)

    return render((request, 'thanks.html', {"user_id": guest_id})) 
