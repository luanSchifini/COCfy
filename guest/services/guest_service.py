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
        # name=name,
        verification_code=guest_cpf
    )


# def register_guest(name, guestMail, code) -> Guest:
#     return Guest.objects.create(
#         name=name,
#         email=guestMail,
#         verification_code=code, 
#     )