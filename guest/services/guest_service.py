from guest.models import Guest


def get_guest(guest_id: str) -> Guest | None:
    try:
       return Guest.objects.get(id=guest_id)
    except Guest.DoesNotExist:
        pass  # Handle the case where the student doesn't exist
 

def check_if_guest_exists(guest_cpf: str) -> Guest | None:
    return Guest.objects.filter(cpf=guest_cpf)


def register_guest(guest_cpf: str) -> Guest:
    return Guest.objects.create(
        cpf=guest_cpf
    )
