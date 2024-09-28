from typing import List
from guest.models import Eletiva


def select_eletivas() -> List[Eletiva]:
    return Eletiva.objects.all()

def get_eletiva(eletiva_id: int) -> Eletiva | None:
    return Eletiva.objects.filter(pk=eletiva_id).first()

