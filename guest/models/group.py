from  django.db import models
from .eletiva import Eletiva

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    eletiva = models.ForeignKey(Eletiva, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'{self.group_name} -> {self.eletiva} '

