from guest.models import Guest


def get_guest(guest_id: str) -> Guest | None:
    try:
       return Guest.objects.get(pk=guest_id)
    except Guest.DoesNotExist:
        pass  # Handle the case where the student doesn't exist


def register_guest(name) -> Guest:
    return Guest.objects.create(
        name=name,
    )


# def register_guest(name, guestMail, code) -> Guest:
#     return Guest.objects.create(
#         name=name,
#         email=guestMail,
#         verification_code=code, 
#     )