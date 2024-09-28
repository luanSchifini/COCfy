from typing import List
from guest.models import Group
from .eletiva_service import get_eletiva

def get_eletiva_group(group_id: int) -> Group | None:
    return Group.objects.filter(pk=group_id).first()


def select_eletiva_group(eletiva_id) -> List[Group]:
    eletiva = get_eletiva(eletiva_id)
    if eletiva is None:
        return Group.objects.all()
    
    return Group.objects.filter(eletiva=eletiva)
